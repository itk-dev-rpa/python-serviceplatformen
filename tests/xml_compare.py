"""Shared helpers for comparing XML element trees in tests."""

from xml.etree import ElementTree


def xml_compare(x1: ElementTree.Element, x2: ElementTree.Element, path="") -> None:
    """Compare two xml elements recursively.

    Args:
        x1: The first element to compare.
        x2: The second element to compare.
        path: The path to the elements used in error messages. Defaults to "".

    Raises:
        ValueError: If the elements or their children don't match.
    """
    main_error = ValueError(f"Elements {x1.tag} and {x2.tag} doesn't match. Path: {path}")
    if x1.tag != x2.tag:
        raise ValueError(f"Tags do not match: {x1.tag} != {x2.tag}") from main_error

    for name, value in x1.attrib.items():
        value_2 = x2.attrib.get(name)
        if value_2 != value:
            raise ValueError(f"Attribute {name} do not match: {value} != {value_2}") from main_error

    for name in x2.attrib.keys():
        if name not in x1.attrib:
            raise ValueError(f"x2 has an attribute x1 is missing: {name}") from main_error

    if not text_compare(x1.text, x2.text):
        raise ValueError(f"Text value doesn't match: {x1.text} != {x2.text}") from main_error

    if not text_compare(x1.tail, x2.tail):
        raise ValueError(f"Tail doesn't match: {x1.tail} != {x2.tail}") from main_error

    if len(x1) != len(x2):
        l1 = (t.tag for t in x1)
        l2 = (t.tag for t in x2)
        diff = set(l1) ^ set(l2)
        raise ValueError(f"Children length differs {len(x1)} != {len(x2)} - Diff: {'; '.join(diff)}") from main_error

    for c1, c2 in zip(x1, x2):
        xml_compare(c1, c2, f"{path} -> {x1.tag}")


def text_compare(s1: str | None, s2: str | None) -> bool:
    """Compare two strings that might be None.
    Ignores leading and trailing whitespace.

    Args:
        s1: The first string to compare.
        s2: The second string to compare.

    Returns:
        True if the strings match.
    """
    return (s1 or "").strip() == (s2 or "").strip()
