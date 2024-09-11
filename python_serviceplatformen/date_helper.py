"""This module contains function to help with datetimes in the Kombit API."""

from datetime import datetime


def format_datetime(_datetime: datetime) -> str:
    """Convert a datetime object to a string with the format:
    %Y-%m-%dT%H:%M:%SZ
    """
    return _datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
