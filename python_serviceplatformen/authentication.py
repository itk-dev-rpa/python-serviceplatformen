"""This module contains the KombitAccess class used to authenticate against the
Kombit API.
"""

from datetime import datetime, timedelta
from dataclasses import dataclass

import requests
from requests.exceptions import HTTPError
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


@dataclass
class Token:
    """Dataclass representing a token with an expiry time."""
    value: str
    expiry_time: datetime


# pylint: disable-next=too-few-public-methods
class KombitAccess:
    """An object that handles access to the Kombit api."""
    cvr: str
    cert_path: str
    _access_tokens: dict[str, Token]
    _saml_tokens: dict[str, Token]
    test: bool
    environment: str

    def __init__(self, cvr: str, cert_path: str, test: bool = False) -> None:
        """Create a new Kombit Access object.

        Args:
            cvr: The cvr number of the organisation making the calls.
            cert_path: The path to the certificate in unified pem-format.
            test: Whether to use the test environment or not.
        """
        self.cvr = cvr
        self.cert_path = cert_path
        self._access_tokens = {}
        self._saml_tokens = {}
        self.test = test

        if test:
            self.environment = "https://exttest.serviceplatformen.dk"
        else:
            self.environment = "https://prod.serviceplatformen.dk"

    def get_access_token(self, entity_id: str) -> str:
        """Get an access token to the api endpoint with the given entity id.
        If an access token already exists for the endpoint it is reused.

        Args:
            entity_id: The entity id of the endpoint.

        Returns:
            An access token to be used in api calls.

        Raises:
            ValueError: If an access token couldn't be obtained for the given entity id.
        """
        if entity_id in self._access_tokens and datetime.now() < self._access_tokens[entity_id].expiry_time:
            return self._access_tokens[entity_id].value

        try:
            saml_token = self.get_saml_token(entity_id)
            access_token = _get_access_token(saml_token, self.cert_path, test=self.test)
            self._access_tokens[entity_id] = access_token
            return access_token.value
        except HTTPError as exc:
            raise ValueError(f"Couldn't obtain access token for {entity_id}: {exc.response.text}") from exc

    def get_saml_token(self, entity_id: str) -> str:
        """Get a SAML to the api endpoint with the given entity id.
        If a valid SAML token already exists for the endpoint it is reused.

        Args:
            entity_id: The entity id of the endpoint.

        Raises:
            ValueError: If a SAML token couldn't be obtained for the given entity id.

        Returns:
            The SAML token as a string
        """
        if entity_id in self._saml_tokens and datetime.now() < self._saml_tokens[entity_id].expiry_time:
            return self._saml_tokens[entity_id].value

        try:
            saml_token = _get_saml_token(self.cvr, self.cert_path, entity_id, test=self.test)
            self._saml_tokens[entity_id] = saml_token
            return saml_token.value
        except HTTPError as exc:
            raise ValueError(f"Couldn't obtain SAML token for {entity_id}: {exc.response.text}") from exc


def _get_saml_token(cvr: str, cert_path: str, entity_id: str, test: bool) -> Token:
    """Get a SAML token for the endpoint with the given entity id.

    Args:
        cvr: The cvr number of the organisation making the calls.
        cert_path: The path to the certificate in unified pem-format.
        entity_id: The entity id of the endpoint.
        test: Whether to use the test api or not.

    Returns:
        A tuple of the SAML token as a string and the expiry time.
    """
    use_key = _extract_first_certificate(cert_path)

    if test:
        url = "https://n2adgangsstyring.eksterntest-stoettesystemerne.dk/runtime/api/rest/wstrust/v1/issue"
    else:
        url = "https://n2adgangsstyring.stoettesystemerne.dk/runtime/api/rest/wstrust/v1/issue"

    payload = {
        "TokenType": "http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLV2.0",
        "RequestType": "http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue",
        "KeyType": "http://docs.oasis-open.org/ws-sx/ws-trust/200512/PublicKey",
        "AnvenderKontekst": {
            "Cvr": cvr
        },
        "UseKey": use_key,
        "AppliesTo": {
            "EndpointReference": {
                "Address": entity_id
            }
        },
        "OnBehalfOf": None
    }

    response = requests.post(url, json=payload, cert=cert_path, timeout=10)
    response.raise_for_status()
    response = response.json()

    saml_token = response['RequestedSecurityToken']['Assertion']
    expiry_time = datetime.strptime(response["Lifetime"], "%m/%d/%Y %H:%M:%S") - timedelta(minutes=5)

    return Token(saml_token, expiry_time)


def _get_access_token(saml_token: str, cert_path: str, test: bool) -> Token:
    """Get an access token for the given SAML context.

    Args:
        saml_token: The SAML token to get the access token for.
        cert_path: The path to the certificate in unified pem-format.
        test: Whether to use the test api or not.

    Returns:
        The access token as a string and the expiry datetime of the token.
    """
    if test:
        url = "https://exttest.serviceplatformen.dk/service/AccessTokenService_1/token"
    else:
        url = "https://prod.serviceplatformen.dk/service/AccessTokenService_1/token"

    payload = {
        "saml-token": saml_token
    }

    response = requests.post(url, data=payload, cert=cert_path, timeout=10)
    response.raise_for_status()
    response = response.json()

    access_token = f"{response['token_type']} {response['access_token']}"
    expiry_time = datetime.now() + timedelta(seconds=response['expires_in']) - timedelta(minutes=5)

    return Token(access_token, expiry_time)


def _extract_first_certificate(pem_file: str) -> str:
    """Extract the first certificate from a certificate file.

    Args:
        pem_file: The path of the pem certificate.

    Raises:
        ValueError: If the certificate couldn't be parsed.

    Returns:
        The first certificate in the file as a single line string.
    """
    with open(pem_file, "rb") as f:
        pem_data = f.read()

    try:
        cert = x509.load_pem_x509_certificate(pem_data, default_backend())
        first_cert = cert.public_bytes(encoding=serialization.Encoding.PEM).decode("utf-8")
        first_cert_single_line = "".join(first_cert.splitlines()[1:-1])
        return first_cert_single_line
    except Exception as e:
        raise ValueError("Error parsing certificate") from e
