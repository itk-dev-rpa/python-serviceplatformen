"""This moduel contains helper functions to use the SF1601 Kombit API.
https://digitaliseringskataloget.dk/integration/sf1601
"""

import urllib.parse
import uuid
from datetime import datetime
from typing import Literal

import requests

from python_serviceplatformen.authentication import KombitAccess
from python_serviceplatformen.date_helper import format_datetime


def is_registered(cpr: str, service: Literal['digitalpost', 'nemsms'], kombit_access: KombitAccess) -> bool:
    """Check if the person with the given cpr number is registered for
    either Digital Post or NemSMS.

    Args:
        cpr: The cpr number of the person to look up.
        service: The service to look up for.
        kombit_access: The KombitAccess object used to authenticate.

    Returns:
        True if the person is registered for the selected service.
    """
    url = urllib.parse.urljoin(kombit_access.environment, "service/PostForespoerg_1/")
    url = urllib.parse.urljoin(url, service)

    parameters = {
        "cprNumber": cpr
    }

    headers = {
        "X-TransaktionsId": str(uuid.uuid4()),
        "X-TransaktionsTid": format_datetime(datetime.now()),
        "authorization": kombit_access.get_access_token("http://entityid.kombit.dk/service/postforespoerg/1")
    }

    response = requests.get(url, params=parameters, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()['result']
