"""This module contains helper functions to use the SF1601 Kombit API.
https://digitaliseringskataloget.dk/integration/sf1601
"""

import urllib.parse
import uuid
from datetime import datetime
from typing import Literal
from xml.etree import ElementTree

import requests

from python_serviceplatformen.authentication import KombitAccess
from python_serviceplatformen.date_helper import format_datetime
from python_serviceplatformen.models import xml_util
from python_serviceplatformen.models.message import Message


def is_registered(id_: str, service: Literal['digitalpost', 'nemsms'], kombit_access: KombitAccess) -> bool:
    """Check if the entity with the given id number is registered for
    either Digital Post or NemSMS.

    Args:
        id_: The id number of the entity to look up.
        service: The service to look up for.
        kombit_access: The KombitAccess object used to authenticate.

    Returns:
        True if the person is registered for the selected service.
    """
    url = urllib.parse.urljoin(kombit_access.environment, "service/PostForespoerg_1/")
    url = urllib.parse.urljoin(url, service)

    identifier = "cprNumber" if len(id_) == 10 else "cvrNumber"
    parameters = {
        identifier: id_
    }

    headers = {
        "X-TransaktionsId": str(uuid.uuid4()),
        "X-TransaktionsTid": format_datetime(datetime.now()),
        "authorization": kombit_access.get_access_token("http://entityid.kombit.dk/service/postforespoerg/1")
    }

    response = requests.get(url, params=parameters, headers=headers, cert=kombit_access.cert_path, timeout=10)
    response.raise_for_status()
    return response.json()['result']


def send_message(message_type: Literal['Digital Post', 'NemSMS'],
                 message: Message, kombit_access: KombitAccess) -> str:
    """Send a Message object as Digital Post or NemSMS.

    Args:
        message_type: The type of message to send.
        message: The Message object to send.
        kombit_access: The KombitAccess objet used to authenticate.

    Returns:
        The uuid of the transaction to trace the message later.
    """
    url = urllib.parse.urljoin(kombit_access.environment, "service/KombiPostAfsend_1/memos")

    transaction_id = str(uuid.uuid4())

    headers = {
        "X-TransaktionsId": transaction_id,
        "X-TransaktionsTid": format_datetime(datetime.now()),
        "authorization": kombit_access.get_access_token("http://entityid.kombit.dk/service/kombipostafsend/1"),
        "Content-Type": "application/xml"
    }

    message_xml = xml_util.dataclass_to_xml(message)

    element = ElementTree.Element("kombi_request")
    ElementTree.SubElement(element, "KombiValgKode").text = message_type
    element.append(message_xml)

    xml_body = ElementTree.tostring(element, encoding="utf8").decode()

    response = requests.post(url=url, headers=headers, data=xml_body, cert=kombit_access.cert_path, timeout=10)
    response.raise_for_status()

    return transaction_id
