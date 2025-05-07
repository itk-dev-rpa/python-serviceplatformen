"""This module contains helper functions to work with xml."""

from datetime import datetime, date
from dataclasses import is_dataclass, fields
from xml.etree import ElementTree

from python_serviceplatformen.date_helper import format_date, format_datetime


def dataclass_to_xml(obj: object) -> ElementTree.Element:
    """Recursively convert a dataclass object to an xml tree.
    This only support dataclasses which fields are either
    other dataclasses, lists/tuples, datetimes/dates or
    values which can be converted to strings.

    Args:
        obj: The dataclass object to convert.

    Returns:
        An Element object representing the xml.
    """
    namespace = obj.__namespace__
    attributes = getattr(obj, "__attributes__", {})
    element = ElementTree.Element(f"{{{namespace}}}{obj.__class__.__name__}", attributes)

    def process_value(value):
        if is_dataclass(value):
            element.append(dataclass_to_xml(value))
        elif value is not None:
            if isinstance(value, datetime):
                text = format_datetime(value)
            elif isinstance(value, date):
                text = format_date(value)
            elif isinstance(value, bool):
                text = str(value).lower()
            else:
                text = str(value)

            ElementTree.SubElement(element, f"{{{namespace}}}{field.name}").text = text

    for field in fields(obj):
        value = getattr(obj, field.name)

        if isinstance(value, (list, tuple)):
            for v in value:
                process_value(v)
        else:
            process_value(value)

    return element


def dataclass_to_xml_string(obj: object) -> str:
    """Recursively convert a dataclass object to an xml string.
    This only support dataclasses which fields are either
    other dataclasses, lists/tuples, datetimes/dates or
    values which can be converted to strings.

    Args:
        obj: The dataclass object to convert.

    Returns:
        An xml string representation of the given object.
    """
    return ElementTree.tostring(dataclass_to_xml(obj)).decode()
