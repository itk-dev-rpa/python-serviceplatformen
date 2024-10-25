"""This module contains multiple dataclasses used to define a MeMo message.
More information and detailed descriptions can be found here:
https://digitaliser.dk/digital-post/vejledninger/memo
"""

from dataclasses import dataclass
from datetime import datetime, date
from typing import Literal, Optional
import uuid


# Typehints
Base64String = str
MimeTypeString = str

NAME_SPACES = {
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "memo": "https://DigitalPost.dk/MeMo-1",
        "gln": "https://www.gs1.dk/gs1-standarder/identifikation/gln-global-location-number/",
        "udd": "https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/elevregister-2/udd#",
        "rid": "https://www.nets.eu/dk-da/løsninger/nemid/nemid-tjenesteudbyder/supplerende-tjenester/pid-rid-cpr-tjenester",
        "pnum": "https://indberet.virk.dk/myndigheder/stat/ERST/P-enhedsloesningen",
        "form": "http://www.form-online.dk/",
        "kle": "http://kle-online.dk/",
        "dmv": "https://motorregister.skat.dk/",
        "grd": "https://data.gov.dk/model/core/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "sor": "https://services.nsi.dk/en/Services/SOR"
}


@dataclass(kw_only=True)
class File:
    __namespace__ = NAME_SPACES["memo"]
    encodingFormat: MimeTypeString
    filename: str
    language: str
    content: Base64String


@dataclass(kw_only=True)
class AttentionPerson:
    __namespace__ = NAME_SPACES["memo"]
    personID: str
    label: str


@dataclass(kw_only=True)
class EMail:
    __namespace__ = NAME_SPACES["memo"]
    emailAddress: str
    relatedAgent: str


@dataclass(kw_only=True)
class Telephone:
    __namespace__ = NAME_SPACES["memo"]
    telephoneNumber: str
    relatedAgent: str


@dataclass(kw_only=True)
class GlobalLocationNumber:
    __namespace__ = NAME_SPACES["gln"]
    globalLocationNumber: str
    location: str


@dataclass(kw_only=True)
class ContentResponsible:
    __namespace__ = NAME_SPACES["memo"]
    contentResponsibleID: str
    label: str


@dataclass(kw_only=True)
class ProductionUnit:
    __namespace__ = NAME_SPACES["grd"]
    productionUnitNumber: str
    productionUnitName: str


@dataclass(kw_only=True)
class SEnumber:
    __namespace__ = NAME_SPACES["grd"]
    seNumber: str
    companyName: str


@dataclass(kw_only=True)
class GeneratingSystem:
    __namespace__ = NAME_SPACES["memo"]
    generatingSystemID: str
    label: str


@dataclass(kw_only=True)
class EID:
    __namespace__ = NAME_SPACES["grd"]
    eID: str
    label: str


@dataclass(kw_only=True)
class SORdata:
    __namespace__ = NAME_SPACES["sor"]
    sorIdentifier: str
    entryName: str


@dataclass(kw_only=True)
class AddressPoint:
    __namespace__ = NAME_SPACES["grd"]
    geographicEastingMeasure: str
    geographicNorthingMeasure: str
    geographicHeightMeasure: str


@dataclass(kw_only=True)
class Address:
    __namespace__ = NAME_SPACES["grd"]
    id: str
    addressLabel: str
    houseNumber: str
    door: str
    floor: str
    co: str
    zipCode: str
    city: str
    country: str
    AddressPoint: AddressPoint


@dataclass(kw_only=True)
class UnstructuredAddress:
    __namespace__ = NAME_SPACES["grd"]
    unstructured: str


@dataclass(kw_only=True)
class ContactInfo:
    __namespace__ = NAME_SPACES["memo"]
    label: str
    value: str


@dataclass(kw_only=True)
class ContactPoint:
    __namespace__ = NAME_SPACES["memo"]
    contactGroup: Optional[str]
    contactPointID: str
    label: str
    ContactInfo_: Optional[tuple[ContactInfo, ...]] = None


@dataclass(kw_only=True)
class CPRdata:
    __namespace__ = NAME_SPACES["grd"]
    cprNumber: str
    name: str


@dataclass(kw_only=True)
class CVRdata:
    __namespace__ = NAME_SPACES["grd"]
    cvrNumber: str
    companyName: str


@dataclass(kw_only=True)
class MotorVehicle:
    __namespace__ = NAME_SPACES["dmv"]
    licenseNumber: str
    chassisNumber: str


@dataclass(kw_only=True)
class PropertyNumber:
    __namespace__ = NAME_SPACES["grd"]
    propertyNumber: str


@dataclass(kw_only=True)
class Education:
    __namespace__ = NAME_SPACES["udd"]
    educationCode: str
    educationName: str


@dataclass(kw_only=True)
class CaseID:
    __namespace__ = NAME_SPACES["memo"]
    caseID: str
    caseSystem: str


@dataclass(kw_only=True)
class KLEdata:
    __namespace__ = NAME_SPACES["kle"]
    subjectKey: str
    version: str
    activityFacet: str
    label: str


@dataclass(kw_only=True)
class FORMdata:
    __namespace__ = NAME_SPACES["form"]
    taskKey: str
    version: str
    activityFacet: str
    label: str


@dataclass(kw_only=True)
class AdditionalContentData:
    __namespace__ = NAME_SPACES["memo"]
    contentDataType: str
    contentDataName: str
    contentDataValue: str


@dataclass(kw_only=True)
class ForwardData:
    __namespace__ = NAME_SPACES["memo"]
    messageUUID: str
    originalMessageDateTime: datetime
    originalSender: str
    originalContentResponsible: Optional[str] = None
    contactPointID: Optional[str] = None
    comment: Optional[str] = None


@dataclass(kw_only=True)
class AdditionalReplyData:
    __namespace__ = NAME_SPACES["memo"]
    label: str
    value: str


@dataclass(kw_only=True)
class ReplyData:
    __namespace__ = NAME_SPACES["memo"]
    messageID: Optional[str] = None
    messageUUID: str
    replyUUID: Optional[str] = None
    senderID: Optional[str] = None
    recipientID: Optional[str] = None
    caseID: Optional[str] = None
    contactPointID: Optional[str] = None
    generatingSystemID: Optional[str] = None
    comment: Optional[str] = None
    AdditionalReplyData_: Optional[tuple[AdditionalReplyData, ...]] = None


@dataclass(kw_only=True)
class EntryPoint:
    __namespace__ = NAME_SPACES["memo"]
    url: str


@dataclass(kw_only=True)
class Reservation:
    __namespace__ = NAME_SPACES["memo"]
    description: str
    reservationUUID: str
    abstract: str
    location: str
    startDateTime: datetime
    endDateTime: datetime
    organizerMail: Optional[str] = None
    organizerName: Optional[str] = None


@dataclass(kw_only=True)
class Action:
    __namespace__ = NAME_SPACES["memo"]
    label: str
    actionCode: Literal["AFTALE", "BETALING", "SELVBETJENING", "INFORMATION", "UNDERSKRIV", "BEKRAEFT", "FORBEREDELSE", "TILMELDING"]
    startDateTime: Optional[datetime] = None
    endDateTime: Optional[datetime] = None
    Reservation_: Optional[Reservation] = None
    EntryPoint_: Optional[EntryPoint] = None


@dataclass(kw_only=True)
class MainDocument:
    __namespace__ = NAME_SPACES["memo"]
    mainDocumentID: Optional[str] = None
    label: Optional[str] = None
    Files: tuple[File, ...]
    Actions: Optional[tuple[Action, ...]] = None


@dataclass(kw_only=True)
class AdditionalDocument:
    __namespace__ = NAME_SPACES["memo"]
    additionalDocumentID: Optional[str] = None
    label: Optional[str] = None
    Files: tuple[File, ...]
    Actions: Optional[tuple[Action, ...]] = None


@dataclass(kw_only=True)
class TechnicalDocument:
    __namespace__ = NAME_SPACES["memo"]
    technicalDocumentID: Optional[str] = None
    label: Optional[str] = None
    Files: tuple[File, ...]


@dataclass(kw_only=True)
class MessageBody:
    __namespace__ = NAME_SPACES["memo"]
    createdDateTime: datetime
    MainDocument: MainDocument
    AdditionalDocuments: Optional[tuple[AdditionalDocument, ...]] = None
    TechnicalDocuments: Optional[tuple[TechnicalDocument, ...]] = None


@dataclass(kw_only=True)
class AttentionData:
    __namespace__ = NAME_SPACES["memo"]
    AttentionPerson_: Optional[AttentionPerson] = None
    ProductionUnit_: Optional[ProductionUnit] = None
    GlobalLocationNumber_: Optional[GlobalLocationNumber] = None
    EMail_: Optional[EMail] = None
    SEnumber_: Optional[SEnumber] = None
    Telephone_: Optional[Telephone] = None
    EID_: Optional[EID] = None
    ContentResponsible_: Optional[ContentResponsible] = None
    GeneratingSystem_: Optional[GeneratingSystem] = None
    SORdata_: Optional[SORdata] = None
    Address_: Optional[Address] = None
    UnstructuredAddress_: Optional[UnstructuredAddress] = None


@dataclass(kw_only=True)
class Sender:
    __namespace__ = NAME_SPACES["memo"]
    senderID: str
    idType: Literal["MyndighedsID", "CPR", "CVR", "Andet"]
    label: str
    idTypeLabel: Optional[str] = None
    AttentionData_: Optional[AttentionData] = None
    ContactPoint_: Optional[ContactPoint] = None


@dataclass(kw_only=True)
class Recipient:
    __namespace__ = NAME_SPACES["memo"]
    recipientID: str
    idType: Literal["MyndighedsID", "CPR", "CVR", "Andet"]
    idTypeLabel: Optional[str] = None
    label: Optional[str] = None
    AttentionData_: Optional[AttentionData] = None
    ContactPoint_: Optional[ContactPoint] = None


@dataclass(kw_only=True)
class ContentData:
    __namespace__ = NAME_SPACES["memo"]
    CPRdata_: Optional[CPRdata] = None
    CVRdata_: Optional[CVRdata] = None
    MotorVehicle_: Optional[MotorVehicle] = None
    PropertyNumber_: Optional[PropertyNumber] = None
    CaseID_: Optional[CaseID] = None
    KLEdata_: Optional[KLEdata] = None
    FORMdata_: Optional[FORMdata] = None
    ProductionUnit_: Optional[ProductionUnit] = None
    Education_: Optional[Education] = None
    Address_: Optional[Address] = None
    UnstructuredAddress_: Optional[UnstructuredAddress] = None
    AdditionalContentData_: Optional[tuple[AdditionalContentData, ...]] = None


@dataclass(kw_only=True)
class MessageHeader:
    __namespace__ = NAME_SPACES["memo"]
    messageType: Literal["DIGITALPOST", "NEMSMS"]
    messageUUID: str
    messageID: Optional[str] = None
    messageCode: Optional[str] = None
    label: str
    notification: Optional[str] = None
    additionalNotification: Optional[str] = None
    reply: Optional[bool] = None
    replyByDateTime: Optional[datetime] = None
    doNotDeliverUntilDate: Optional[date] = None
    mandatory: bool
    legalNotification: bool
    postType: Optional[str] = None
    Sender: Sender
    Recipient: Recipient
    ContentData_: Optional[ContentData] = None
    ForwardData_: Optional[ForwardData] = None
    ReplyData_: Optional[tuple[ReplyData, ...]] = None


@dataclass(kw_only=True)
class Message:
    __namespace__ = NAME_SPACES["memo"]
    __attributes__ = {
        "memoVersion": "1.1",
        "memoSchVersion": "1.1.0",

    }
    MessageHeader: MessageHeader
    MessageBody_: Optional[MessageBody] = None


def create_nemsms(message_label: str, message_text: str, sender: Sender, recipient: Recipient, message_uuid: str | None = None) -> Message:
    """Create a Message object that represents a NemSMS message.

    Args:
        message_label: The header text of the NemSMS.
        message_text: The text content of the NemSMS. Max 150 chars.
        sender: A Sender object representing the sender of the message.
        recipient: A Recipient object representing the recipient of the message.
        message_uuid: The uuid of the message. If None a random id will be generated.

    Returns:
        A Message object representing a NemSMS.
    """
    if not message_uuid:
        message_uuid = str(uuid.uuid4())

    return Message(
        MessageHeader=MessageHeader(
            messageType="NEMSMS",
            messageUUID=message_uuid,
            label=message_label,
            notification=message_text,
            mandatory=False,
            legalNotification=False,
            Sender=sender,
            Recipient=recipient
        )
    )


def create_digital_post_with_attached_files(label: str, sender: Sender, recipient: Recipient, files: tuple[File],
                                            message_uuid: str | None = None, created_datetime: datetime | None = None) -> Message:
    """Create a Message object representing Digital Post with one or
    more file attachments.

    Args:
        label: The header text of the message.
        sender: A Sender object representing the sender of the message.
        recipient: A Recipient object representing the recipient of the message.
        files: A tuple of File objects to be attached to the message's main document.
        message_uuid: The uuid of the message. If None a random id will be generated.
        created_datetime: The creation time of the message. If None the current time will be used.

    Returns:
        A Message object.
    """
    if not message_uuid:
        message_uuid = str(uuid.uuid4())

    if not created_datetime:
        created_datetime = datetime.now()

    return Message(
        MessageHeader=MessageHeader(
            messageType="DIGITALPOST",
            messageUUID=message_uuid,
            label=label,
            mandatory=False,
            legalNotification=False,
            Sender=sender,
            Recipient=recipient,
        ),
        MessageBody_=MessageBody(
            createdDateTime=created_datetime,
            MainDocument=MainDocument(
                Files=files
            )
        )
    )
