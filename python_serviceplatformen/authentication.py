"""This module contains the KombitAccess class used to authenticate against the
Kombit API.
"""

from datetime import datetime, timedelta

import requests
from requests.exceptions import HTTPError
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


# pylint: disable-next=too-few-public-methods
class KombitAccess:
    """An object that handles access to the Kombit api."""
    cvr: str
    cert_path: str
    _access_tokens: dict[str, (str, datetime)]
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
            test: Whether to use the test api or not.

        Returns:
            An access token to be used in api calls.

        Raises:
            HTTPError: If an access token couldn't be obtained for the given entity id.
        """
        if entity_id in self._access_tokens and datetime.now() < self._access_tokens[entity_id][1]:
            return self._access_tokens[entity_id][0]

        try:
            saml_token = _get_saml_token(self.cvr, self.cert_path, entity_id, test=self.test)
            access_token = _get_access_token(saml_token, self.cert_path, test=self.test)
            self._access_tokens[entity_id] = access_token
            return access_token[0]
        except HTTPError as exc:
            raise ValueError(f"Couldn't obtain access token for {entity_id}") from exc


def _get_saml_token(cvr: str, cert_path: str, entity_id: str, test: bool) -> str:
    """Get a SAML token for the endpoint with the given entity id.

    Args:
        cvr: The cvr number of the organisation making the calls.
        cert_path: The path to the certificate in unified pem-format.
        entity_id: The entity id of the endpoint.
        test: Whether to use the test api or not.

    Returns:
        A SAML token as a string.
    """
    use_key = _extract_first_certificate(cert_path)

    if test:
        url = "https://adgangsstyring.eksterntest-stoettesystemerne.dk/runtime/api/rest/wstrust/v1/issue"
    else:
        url = "https://adgangsstyring.stoettesystemerne.dk/runtime/api/rest/wstrust/v1/issue"

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

    return response.json()['RequestedSecurityToken']['Assertion']


def _get_access_token(saml_token: str, cert_path: str, test: bool) -> tuple[str, datetime]:
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

    return access_token, expiry_time


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
