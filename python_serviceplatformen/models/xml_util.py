from datetime import datetime, date
from dataclasses import is_dataclass, fields
import os
from xml.etree import ElementTree

import xmlschema

from python_serviceplatformen.date_helper import format_date, format_datetime


def dataclass_to_xml(obj: object, namespaces: dict[str, str] | None = None) -> ElementTree.Element:
    """Recursively convert a dataclass object to an xml tree.
    This only support dataclasses which fields are either
    other dataclasses, lists/tuples, datetimes/dates or
    values which can be converted to strings.

    Args:
        obj: The dataclass object to convert.

    Returns:
        An Element object representing the xml.
    """
    if namespaces:
        for k, v in namespaces.items():
            ElementTree.register_namespace(k, v)

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


def validate_memo(element: ElementTree.Element) -> None:
    """Validate an xml element object against the MeMo schema.

    Args:
        element: The xml element to validate.

    Raises:
        XMLSchemaValidationError: If the xml element doesn't match the schema.
    """
    xml_string = ElementTree.tostring(element, encoding="utf8").decode()

    dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir, "Memo_SChema", "MeMo_core.xsd")

    schema = xmlschema.XMLSchema11(path)
    schema.validate(xml_string)
