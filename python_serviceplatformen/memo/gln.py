from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://www.gs1.dk/gs1-standarder/identifikation/gln-global-location-number/"


@dataclass
class GlobalLocationNumber2:
    class Meta:
        name = "globalLocationNumber"
        namespace = "https://www.gs1.dk/gs1-standarder/identifikation/gln-global-location-number/"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 9999999999999,
        },
    )


@dataclass
class Location:
    class Meta:
        name = "location"
        namespace = "https://www.gs1.dk/gs1-standarder/identifikation/gln-global-location-number/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class GlobalLocationNumber1:
    class Meta:
        name = "GlobalLocationNumber"
        namespace = "https://www.gs1.dk/gs1-standarder/identifikation/gln-global-location-number/"

    global_location_number: GlobalLocationNumber2 = field(
        metadata={
            "name": "globalLocationNumber",
            "type": "Element",
            "required": True,
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
