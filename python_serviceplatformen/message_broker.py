"""This module contains helper function to Kombit's Beskedfordeler SF1461.
https://digitaliseringskataloget.dk/integration/sf1461
"""

import base64
import ssl
from collections.abc import Generator

import pika
from pika.credentials import ExternalCredentials

from python_serviceplatformen.authentication import KombitAccess

PORT = 5671
VIRTUAL_HOST = "BF"
PROD_HOST = "beskedfordeler.stoettesystemerne.dk"
TEST_HOST = "beskedfordeler.eksterntest-stoettesystemerne.dk"


class TokenCredentials(ExternalCredentials):
    """A class for handling AMQP authorization using an
    external token.
    """
    def __init__(self, token: bytes):
        super().__init__()
        self.token = token

    def response_for(self, start):
        """Handle AMQP auth challenge."""
        return self.TYPE, self.token


def _setup_pika_params(kombit_access: KombitAccess) -> pika.ConnectionParameters:
    """Setup parameters used by Pika to connect to the AMQP server.

    Args:
        kombit_access: The KombitAccess object used to authenticate.

    Returns:
        A pika.ConnectionsParameters object that can be used to connect.
    """
    saml_token = kombit_access.get_saml_token("http://entityid.kombit.dk/service/bfo_modtag/2")
    saml_decoded = base64.b64decode(saml_token)

    if kombit_access.test:
        host = TEST_HOST
    else:
        host = PROD_HOST

    ssl_context = ssl.create_default_context()
    ssl_options = pika.SSLOptions(context=ssl_context, server_hostname=host)
    credentials = TokenCredentials(token=saml_decoded)

    return pika.ConnectionParameters(
        host=host,
        port=PORT,
        virtual_host=VIRTUAL_HOST,
        ssl_options=ssl_options,
        credentials=credentials
    )


def iterate_queue_messages(queue_id: str, kombit_access: KombitAccess, auto_acknowledge: bool = True) -> Generator[bytes]:
    """Iterate over message in the given queue.
    Messages are retrieved one at a time from the queue server.
    If auto_acknowledge is true messages are removed from the queue server
    and cannot be retrieved again.

    Args:
        queue_id: The id of the queue to get messages from. Most likely a UUID.
        kombit_access: The KombitAccess object used for authentication.
        auto_acknowledge: Whether to mark messages as read after receiving them. Defaults to True.

    Yields:
        The message body as bytes.
    """
    params = _setup_pika_params(kombit_access)

    with pika.BlockingConnection(parameters=params) as connection:
        channel = connection.channel()

        while True:
            method_frame, header_frame, body = channel.basic_get(queue_id, auto_ack=auto_acknowledge)
            if not any((method_frame, header_frame, body)):
                return  # Queue is empty

            yield body
