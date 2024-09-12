from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://motorregister.skat.dk/"


@dataclass
class ChassisNumber:
    class Meta:
        name = "chassisNumber"
        namespace = "https://motorregister.skat.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class LicenseNumber:
    class Meta:
        name = "licenseNumber"
        namespace = "https://motorregister.skat.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 7,
        },
    )


@dataclass
class MotorVehicle:
    class Meta:
        namespace = "https://motorregister.skat.dk/"

    license_number: LicenseNumber = field(
        metadata={
            "name": "licenseNumber",
            "type": "Element",
            "required": True,
        },
    )
    chassis_number: Optional[ChassisNumber] = field(
        default=None,
        metadata={
            "name": "chassisNumber",
            "type": "Element",
        },
    )
