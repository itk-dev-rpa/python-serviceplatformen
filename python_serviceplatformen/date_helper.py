"""This module contains functions to help with dates and datetimes in the Kombit API."""

from datetime import datetime, date


def format_datetime(datetime_: datetime) -> str:
    """Convert a datetime object to a string with the format:
    %Y-%m-%dT%H:%M:%SZ
    """
    return datetime_.strftime('%Y-%m-%dT%H:%M:%SZ')


def format_date(date_: date) -> str:
    """Convert a date object to a string with the format:
    %Y-%m-%d
    """
    return date_.strftime('%Y-%m-%d')
