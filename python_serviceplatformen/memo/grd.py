from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://data.gov.dk/model/core/"


@dataclass
class AddressLabel:
    class Meta:
        name = "addressLabel"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class City:
    class Meta:
        name = "city"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Co:
    class Meta:
        name = "co"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class CompanyName:
    class Meta:
        name = "companyName"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Country:
    class Meta:
        name = "country"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class CprNumber:
    class Meta:
        name = "cprNumber"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class CvrNumber:
    class Meta:
        name = "cvrNumber"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Door:
    class Meta:
        name = "door"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class EId2:
    class Meta:
        name = "eID"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Floor:
    class Meta:
        name = "floor"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class GeographicEastingMeasure:
    class Meta:
        name = "geographicEastingMeasure"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class GeographicHeightMeasure:
    class Meta:
        name = "geographicHeightMeasure"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class GeographicNorthingMeasure:
    class Meta:
        name = "geographicNorthingMeasure"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class HouseNumber:
    class Meta:
        name = "houseNumber"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Id:
    class Meta:
        name = "id"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Label:
    class Meta:
        name = "label"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Name:
    class Meta:
        name = "name"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class ProductionUnitName:
    class Meta:
        name = "productionUnitName"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class ProductionUnitNumber:
    class Meta:
        name = "productionUnitNumber"
        namespace = "https://data.gov.dk/model/core/"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 9999999999,
        },
    )


@dataclass
class PropertyNumber2:
    class Meta:
        name = "propertyNumber"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class SeNumber2:
    class Meta:
        name = "seNumber"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Unstructured:
    class Meta:
        name = "unstructured"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class ZipCode:
    class Meta:
        name = "zipCode"
        namespace = "https://data.gov.dk/model/core/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class AddressPoint:
    class Meta:
        namespace = "https://data.gov.dk/model/core/"

    geographic_easting_measure: Optional[GeographicEastingMeasure] = field(
        default=None,
        metadata={
            "name": "geographicEastingMeasure",
            "type": "Element",
        },
    )
    geographic_northing_measure: Optional[GeographicNorthingMeasure] = field(
        default=None,
        metadata={
            "name": "geographicNorthingMeasure",
            "type": "Element",
        },
    )
    geographic_height_measure: Optional[GeographicHeightMeasure] = field(
        default=None,
        metadata={
            "name": "geographicHeightMeasure",
            "type": "Element",
        },
    )


@dataclass
class Cprdata:
    class Meta:
        name = "CPRdata"
        namespace = "https://data.gov.dk/model/core/"

    cpr_number: CprNumber = field(
        metadata={
            "name": "cprNumber",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Cvrdata:
    class Meta:
        name = "CVRdata"
        namespace = "https://data.gov.dk/model/core/"

    cvr_number: CvrNumber = field(
        metadata={
            "name": "cvrNumber",
            "type": "Element",
            "required": True,
        },
    )
    company_name: Optional[CompanyName] = field(
        default=None,
        metadata={
            "name": "companyName",
            "type": "Element",
        },
    )


@dataclass
class Eid1:
    class Meta:
        name = "EID"
        namespace = "https://data.gov.dk/model/core/"

    e_id: EId2 = field(
        metadata={
            "name": "eID",
            "type": "Element",
            "required": True,
        },
    )
    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ProductionUnit:
    class Meta:
        namespace = "https://data.gov.dk/model/core/"

    production_unit_number: ProductionUnitNumber = field(
        metadata={
            "name": "productionUnitNumber",
            "type": "Element",
            "required": True,
        },
    )
    production_unit_name: Optional[ProductionUnitName] = field(
        default=None,
        metadata={
            "name": "productionUnitName",
            "type": "Element",
        },
    )


@dataclass
class PropertyNumber1:
    class Meta:
        name = "PropertyNumber"
        namespace = "https://data.gov.dk/model/core/"

    property_number: PropertyNumber2 = field(
        metadata={
            "name": "propertyNumber",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Senumber1:
    class Meta:
        name = "SEnumber"
        namespace = "https://data.gov.dk/model/core/"

    se_number: SeNumber2 = field(
        metadata={
            "name": "seNumber",
            "type": "Element",
            "required": True,
        },
    )
    company_name: Optional[CompanyName] = field(
        default=None,
        metadata={
            "name": "companyName",
            "type": "Element",
        },
    )


@dataclass
class UnstructuredAddress:
    class Meta:
        namespace = "https://data.gov.dk/model/core/"

    unstructured: Unstructured = field(
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Address:
    class Meta:
        namespace = "https://data.gov.dk/model/core/"

    id: Optional[Id] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address_label: Optional[AddressLabel] = field(
        default=None,
        metadata={
            "name": "addressLabel",
            "type": "Element",
        },
    )
    house_number: Optional[HouseNumber] = field(
        default=None,
        metadata={
            "name": "houseNumber",
            "type": "Element",
        },
    )
    door: Optional[Door] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    floor: Optional[Floor] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    co: Optional[Co] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    zip_code: Optional[ZipCode] = field(
        default=None,
        metadata={
            "name": "zipCode",
            "type": "Element",
        },
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address_point: Optional[AddressPoint] = field(
        default=None,
        metadata={
            "name": "AddressPoint",
            "type": "Element",
        },
    )
