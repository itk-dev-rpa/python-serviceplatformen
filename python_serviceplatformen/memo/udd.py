from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/elevregister-2/udd#"


@dataclass
class EducationCode:
    class Meta:
        name = "educationCode"
        namespace = "https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/elevregister-2/udd#"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class EducationName:
    class Meta:
        name = "educationName"
        namespace = "https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/elevregister-2/udd#"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Education:
    class Meta:
        namespace = "https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/elevregister-2/udd#"

    education_code: EducationCode = field(
        metadata={
            "name": "educationCode",
            "type": "Element",
            "required": True,
        },
    )
    education_name: Optional[EducationName] = field(
        default=None,
        metadata={
            "name": "educationName",
            "type": "Element",
        },
    )
