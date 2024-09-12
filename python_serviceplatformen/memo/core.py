from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from python_serviceplatformen.memo.data_types import MemoMessageType
from python_serviceplatformen.memo.dmv import MotorVehicle
from python_serviceplatformen.memo.form import Formdata
from python_serviceplatformen.memo.gln import GlobalLocationNumber1
from python_serviceplatformen.memo.grd import (
    Address,
    Cprdata,
    Cvrdata,
    Eid1,
    ProductionUnit,
    PropertyNumber1,
    Senumber1,
    UnstructuredAddress,
)
from python_serviceplatformen.memo.kle import Kledata
from python_serviceplatformen.memo.sor import Sordata
from python_serviceplatformen.memo.udd import Education

__NAMESPACE__ = "https://DigitalPost.dk/MeMo-1"


@dataclass
class AdditionalContentData:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    content_data_name: str = field(
        metadata={
            "name": "contentDataName",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    content_data_value: str = field(
        metadata={
            "name": "contentDataValue",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    content_data_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentDataType",
            "type": "Element",
            "max_length": 256,
        },
    )

@dataclass
class AdditionalReplyData:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    label: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    value: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class AttentionPerson:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    person_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "personID",
            "type": "Element",
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )


@dataclass
class CaseId:
    class Meta:
        name = "CaseID"
        namespace = "https://DigitalPost.dk/MeMo-1"

    case_id: str = field(
        metadata={
            "name": "caseID",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    case_system: str = field(
        metadata={
            "name": "caseSystem",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class ContactInfo:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    label: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    value: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class ContentResponsible:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    content_responsible_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentResponsibleID",
            "type": "Element",
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )


@dataclass
class Email:
    class Meta:
        name = "EMail"
        namespace = "https://DigitalPost.dk/MeMo-1"

    email_address: str = field(
        metadata={
            "name": "emailAddress",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    related_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "relatedAgent",
            "type": "Element",
            "max_length": 256,
        },
    )


@dataclass
class EntryPoint:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    url: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class File:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    encoding_format: str = field(
        metadata={
            "name": "encodingFormat",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    filename: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    language: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 2,
        },
    )
    content: bytes = field(
        metadata={
            "type": "Element",
            "required": True,
            "format": "base64",
        },
    )


@dataclass
class ForwardData:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    message_uuid: str = field(
        metadata={
            "name": "messageUUID",
            "type": "Element",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[aAbB89][a-fA-F0-9]{3}-[a-fA-F0-9]{12}",
        },
    )
    original_message_date_time: str = field(
        metadata={
            "name": "originalMessageDateTime",
            "type": "Element",
            "required": True,
            "pattern": r".+Z",
        },
    )
    original_sender: str = field(
        metadata={
            "name": "originalSender",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    original_content_responsible: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalContentResponsible",
            "type": "Element",
            "max_length": 256,
        },
    )
    contact_point_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPointID",
            "type": "Element",
            "max_length": 256,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 512,
        },
    )


@dataclass
class GeneratingSystem:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    generating_system_id: str = field(
        metadata={
            "name": "generatingSystemID",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )


@dataclass
class Reservation:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    reservation_uuid: str = field(
        metadata={
            "name": "reservationUUID",
            "type": "Element",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[aAbB89][a-fA-F0-9]{3}-[a-fA-F0-9]{12}",
        },
    )
    abstract: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    location: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    start_date_time: str = field(
        metadata={
            "name": "startDateTime",
            "type": "Element",
            "required": True,
            "pattern": r".+Z",
        },
    )
    end_date_time: str = field(
        metadata={
            "name": "endDateTime",
            "type": "Element",
            "required": True,
            "pattern": r".+Z",
        },
    )
    organizer_mail: Optional[str] = field(
        default=None,
        metadata={
            "name": "organizerMail",
            "type": "Element",
            "max_length": 256,
        },
    )
    organizer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "organizerName",
            "type": "Element",
            "max_length": 256,
        },
    )


@dataclass
class Telephone:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    telephone_number: str = field(
        metadata={
            "name": "telephoneNumber",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    related_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "relatedAgent",
            "type": "Element",
            "max_length": 256,
        },
    )


@dataclass
class Action:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    label: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    action_code: str = field(
        metadata={
            "name": "actionCode",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    start_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "startDateTime",
            "type": "Element",
            "pattern": r".+Z",
        },
    )
    end_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "endDateTime",
            "type": "Element",
            "pattern": r".+Z",
        },
    )
    reservation: Optional[Reservation] = field(
        default=None,
        metadata={
            "name": "Reservation",
            "type": "Element",
        },
    )
    entry_point: Optional[EntryPoint] = field(
        default=None,
        metadata={
            "name": "EntryPoint",
            "type": "Element",
        },
    )


@dataclass
class AttentionData:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    attention_person: Optional[AttentionPerson] = field(
        default=None,
        metadata={
            "name": "AttentionPerson",
            "type": "Element",
        },
    )
    production_unit: Optional[ProductionUnit] = field(
        default=None,
        metadata={
            "name": "ProductionUnit",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    global_location_number: Optional[GlobalLocationNumber1] = field(
        default=None,
        metadata={
            "name": "GlobalLocationNumber",
            "type": "Element",
            "namespace": "https://www.gs1.dk/gs1-standarder/identifikation/gln-global-location-number/",
        },
    )
    email: Optional[Email] = field(
        default=None,
        metadata={
            "name": "EMail",
            "type": "Element",
        },
    )
    senumber: Optional[Senumber1] = field(
        default=None,
        metadata={
            "name": "SEnumber",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    telephone: Optional[Telephone] = field(
        default=None,
        metadata={
            "name": "Telephone",
            "type": "Element",
        },
    )
    eid: Optional[Eid1] = field(
        default=None,
        metadata={
            "name": "EID",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    content_responsible: Optional[ContentResponsible] = field(
        default=None,
        metadata={
            "name": "ContentResponsible",
            "type": "Element",
        },
    )
    generating_system: Optional[GeneratingSystem] = field(
        default=None,
        metadata={
            "name": "GeneratingSystem",
            "type": "Element",
        },
    )
    sordata: Optional[Sordata] = field(
        default=None,
        metadata={
            "name": "SORdata",
            "type": "Element",
            "namespace": "https://services.nsi.dk/en/Services/SOR",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    unstructured_address: Optional[UnstructuredAddress] = field(
        default=None,
        metadata={
            "name": "UnstructuredAddress",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )


@dataclass
class ContactPoint:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    contact_point_id: str = field(
        metadata={
            "name": "contactPointID",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    contact_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactGroup",
            "type": "Element",
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    contact_info: List[ContactInfo] = field(
        default_factory=list,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "max_occurs": 2,
        },
    )


@dataclass
class ContentData:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    cprdata: Optional[Cprdata] = field(
        default=None,
        metadata={
            "name": "CPRdata",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    cvrdata: Optional[Cvrdata] = field(
        default=None,
        metadata={
            "name": "CVRdata",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    motor_vehicle: Optional[MotorVehicle] = field(
        default=None,
        metadata={
            "name": "MotorVehicle",
            "type": "Element",
            "namespace": "https://motorregister.skat.dk/",
        },
    )
    property_number: Optional[PropertyNumber1] = field(
        default=None,
        metadata={
            "name": "PropertyNumber",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    case_id: Optional[CaseId] = field(
        default=None,
        metadata={
            "name": "CaseID",
            "type": "Element",
        },
    )
    kledata: Optional[Kledata] = field(
        default=None,
        metadata={
            "name": "KLEdata",
            "type": "Element",
            "namespace": "http://kle-online.dk/",
        },
    )
    formdata: Optional[Formdata] = field(
        default=None,
        metadata={
            "name": "FORMdata",
            "type": "Element",
            "namespace": "http://www.form-online.dk/",
        },
    )
    production_unit: Optional[ProductionUnit] = field(
        default=None,
        metadata={
            "name": "ProductionUnit",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    education: Optional[Education] = field(
        default=None,
        metadata={
            "name": "Education",
            "type": "Element",
            "namespace": "https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/elevregister-2/udd#",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    unstructured_address: Optional[UnstructuredAddress] = field(
        default=None,
        metadata={
            "name": "UnstructuredAddress",
            "type": "Element",
            "namespace": "https://data.gov.dk/model/core/",
        },
    )
    additional_content_data: List[AdditionalContentData] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalContentData",
            "type": "Element",
            "max_occurs": 10,
        },
    )


@dataclass
class ReplyData:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    message_uuid: str = field(
        metadata={
            "name": "messageUUID",
            "type": "Element",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[aAbB89][a-fA-F0-9]{3}-[a-fA-F0-9]{12}",
        },
    )
    message_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "messageID",
            "type": "Element",
            "max_length": 256,
        },
    )
    reply_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "replyUUID",
            "type": "Element",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[aAbB89][a-fA-F0-9]{3}-[a-fA-F0-9]{12}",
        },
    )
    sender_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "senderID",
            "type": "Element",
            "max_length": 256,
        },
    )
    recipient_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "recipientID",
            "type": "Element",
            "max_length": 256,
        },
    )
    case_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "caseID",
            "type": "Element",
            "max_length": 256,
        },
    )
    contact_point_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactPointID",
            "type": "Element",
            "max_length": 256,
        },
    )
    generating_system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "generatingSystemID",
            "type": "Element",
            "max_length": 256,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 512,
        },
    )
    additional_reply_data: List[AdditionalReplyData] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalReplyData",
            "type": "Element",
            "max_occurs": 4,
        },
    )


@dataclass
class TechnicalDocument:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    technical_document_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "technicalDocumentID",
            "type": "Element",
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    file: List[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class AdditionalDocument:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    additional_document_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "additionalDocumentID",
            "type": "Element",
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    file: List[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    action: List[Action] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )


@dataclass
class MainDocument:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    main_document_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "mainDocumentID",
            "type": "Element",
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    file: List[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    action: List[Action] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )


@dataclass
class Recipient:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    recipient_id: str = field(
        metadata={
            "name": "recipientID",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    id_type: str = field(
        metadata={
            "name": "idType",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    id_type_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "idTypeLabel",
            "type": "Element",
            "max_length": 256,
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    attention_data: Optional[AttentionData] = field(
        default=None,
        metadata={
            "name": "AttentionData",
            "type": "Element",
        },
    )
    contact_point: Optional[ContactPoint] = field(
        default=None,
        metadata={
            "name": "ContactPoint",
            "type": "Element",
        },
    )


@dataclass
class Sender:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    sender_id: str = field(
        metadata={
            "name": "senderID",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    id_type: str = field(
        metadata={
            "name": "idType",
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    label: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    id_type_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "idTypeLabel",
            "type": "Element",
            "max_length": 256,
        },
    )
    attention_data: Optional[AttentionData] = field(
        default=None,
        metadata={
            "name": "AttentionData",
            "type": "Element",
        },
    )
    contact_point: Optional[ContactPoint] = field(
        default=None,
        metadata={
            "name": "ContactPoint",
            "type": "Element",
        },
    )


@dataclass
class MessageBody:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    created_date_time: str = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "required": True,
            "pattern": r".+Z",
        },
    )
    main_document: MainDocument = field(
        metadata={
            "name": "MainDocument",
            "type": "Element",
            "required": True,
        },
    )
    additional_document: List[AdditionalDocument] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDocument",
            "type": "Element",
        },
    )
    technical_document: List[TechnicalDocument] = field(
        default_factory=list,
        metadata={
            "name": "TechnicalDocument",
            "type": "Element",
        },
    )


@dataclass
class MessageHeader:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    message_type: MemoMessageType = field(
        metadata={
            "name": "messageType",
            "type": "Element",
            "required": True,
        },
    )
    message_uuid: str = field(
        metadata={
            "name": "messageUUID",
            "type": "Element",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[aAbB89][a-fA-F0-9]{3}-[a-fA-F0-9]{12}",
        },
    )
    label: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        },
    )
    mandatory: bool = field(
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    legal_notification: bool = field(
        metadata={
            "name": "legalNotification",
            "type": "Element",
            "required": True,
        },
    )
    sender: Sender = field(
        metadata={
            "name": "Sender",
            "type": "Element",
            "required": True,
        },
    )
    recipient: Recipient = field(
        metadata={
            "name": "Recipient",
            "type": "Element",
            "required": True,
        },
    )
    message_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "messageID",
            "type": "Element",
            "max_length": 256,
        },
    )
    message_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "messageCode",
            "type": "Element",
            "max_length": 256,
        },
    )
    notification: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 150,
        },
    )
    additional_notification: Optional[str] = field(
        default=None,
        metadata={
            "name": "additionalNotification",
            "type": "Element",
            "max_length": 256,
        },
    )
    reply: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reply_by_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "replyByDateTime",
            "type": "Element",
            "pattern": r".+Z",
        },
    )
    do_not_deliver_until_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "doNotDeliverUntilDate",
            "type": "Element",
        },
    )
    post_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "postType",
            "type": "Element",
            "max_length": 256,
        },
    )
    content_data: Optional[ContentData] = field(
        default=None,
        metadata={
            "name": "ContentData",
            "type": "Element",
        },
    )
    forward_data: Optional[ForwardData] = field(
        default=None,
        metadata={
            "name": "ForwardData",
            "type": "Element",
        },
    )
    reply_data: List[ReplyData] = field(
        default_factory=list,
        metadata={
            "name": "ReplyData",
            "type": "Element",
        },
    )


@dataclass
class Message:
    class Meta:
        namespace = "https://DigitalPost.dk/MeMo-1"

    message_header: MessageHeader = field(
        metadata={
            "name": "MessageHeader",
            "type": "Element",
            "required": True,
        },
    )
    message_body: Optional[MessageBody] = field(
        default=None,
        metadata={
            "name": "MessageBody",
            "type": "Element",
        },
    )
    memo_version: Decimal = field(
        default=1.1,
        metadata={
            "name": "memoVersion",
            "type": "Attribute",
            "required": True,
        },
    )
    memo_sch_version: str = field(
        default="1.1.0",
        metadata={
            "name": "memoSchVersion",
            "type": "Attribute",
            "required": True,
            "max_length": 256,
        },
    )
