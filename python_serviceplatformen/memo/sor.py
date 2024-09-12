from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://services.nsi.dk/en/Services/SOR"


@dataclass
class EntryName:
    class Meta:
        name = "entryName"
        namespace = "https://services.nsi.dk/en/Services/SOR"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class SorIdentifier:
    class Meta:
        name = "sorIdentifier"
        namespace = "https://services.nsi.dk/en/Services/SOR"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Sordata:
    class Meta:
        name = "SORdata"
        namespace = "https://services.nsi.dk/en/Services/SOR"

    sor_identifier: SorIdentifier = field(
        metadata={
            "name": "sorIdentifier",
            "type": "Element",
            "required": True,
        },
    )
    entry_name: Optional[EntryName] = field(
        default=None,
        metadata={
            "name": "entryName",
            "type": "Element",
        },
    )
