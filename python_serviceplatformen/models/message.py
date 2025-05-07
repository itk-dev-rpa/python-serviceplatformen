"""This module contains multiple dataclasses used to define a MeMo message.
More information and detailed descriptions can be found here:
https://digitaliser.dk/digital-post/vejledninger/memo
"""

from dataclasses import dataclass
from datetime import datetime, date
from typing import Literal, Optional
import uuid
from xml.etree import ElementTree


# Naming follows the names of the official MeMo format
# Class descriptions are in the official MeMo docs
# We can't change the number of class attributes
# pylint: disable=invalid-name, missing-class-docstring, too-many-instance-attributes


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

for k, v in NAME_SPACES.items():
    ElementTree.register_namespace(k, v)


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
    addressPoint: AddressPoint


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
    contactInfo: Optional[tuple[ContactInfo, ...]] = None


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
    originalRepresentative: Optional[str] = None
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
    additionalReplyData: Optional[tuple[AdditionalReplyData, ...]] = None


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
    reservation: Optional[Reservation] = None
    entryPoint: Optional[EntryPoint] = None


@dataclass(kw_only=True)
class MainDocument:
    __namespace__ = NAME_SPACES["memo"]
    mainDocumentID: Optional[str] = None
    label: Optional[str] = None
    files: tuple[File, ...]
    actions: Optional[tuple[Action, ...]] = None


@dataclass(kw_only=True)
class AdditionalDocument:
    __namespace__ = NAME_SPACES["memo"]
    additionalDocumentID: Optional[str] = None
    label: Optional[str] = None
    files: tuple[File, ...]
    actions: Optional[tuple[Action, ...]] = None


@dataclass(kw_only=True)
class TechnicalDocument:
    __namespace__ = NAME_SPACES["memo"]
    technicalDocumentID: Optional[str] = None
    label: Optional[str] = None
    files: tuple[File, ...]


@dataclass(kw_only=True)
class MessageBody:
    __namespace__ = NAME_SPACES["memo"]
    createdDateTime: datetime
    mainDocument: MainDocument
    additionalDocuments: Optional[tuple[AdditionalDocument, ...]] = None
    technicalDocuments: Optional[tuple[TechnicalDocument, ...]] = None


@dataclass(kw_only=True)
class AttentionData:
    __namespace__ = NAME_SPACES["memo"]
    attentionPerson: Optional[AttentionPerson] = None
    productionUnit: Optional[ProductionUnit] = None
    globalLocationNumber: Optional[GlobalLocationNumber] = None
    email: Optional[EMail] = None
    SE_number: Optional[SEnumber] = None
    telephone: Optional[Telephone] = None
    eID: Optional[EID] = None
    contentResponsible: Optional[ContentResponsible] = None
    generatingSystem: Optional[GeneratingSystem] = None
    SOR_data: Optional[SORdata] = None
    address: Optional[Address] = None
    unstructuredAddress: Optional[UnstructuredAddress] = None


@dataclass(kw_only=True)
class Representative:
    __namespace__ = NAME_SPACES["memo"]
    representativeID: str
    idType: Literal["CPR", "CVR"]
    label: str


@dataclass(kw_only=True)
class Sender:
    __namespace__ = NAME_SPACES["memo"]
    senderID: str
    idType: Literal["MyndighedsID", "CPR", "CVR"]
    label: str
    attentionData: Optional[AttentionData] = None
    contactPoint: Optional[ContactPoint] = None
    representative: Optional[Representative] = None


@dataclass(kw_only=True)
class Recipient:
    __namespace__ = NAME_SPACES["memo"]
    recipientID: str
    idType: Literal["MyndighedsID", "CPR", "CVR"]
    label: Optional[str] = None
    attentionData: Optional[AttentionData] = None
    contactPoint: Optional[ContactPoint] = None


@dataclass(kw_only=True)
class ContentData:
    __namespace__ = NAME_SPACES["memo"]
    CPR_data: Optional[CPRdata] = None
    CVR_data: Optional[CVRdata] = None
    motorVehicle: Optional[MotorVehicle] = None
    propertyNumber: Optional[PropertyNumber] = None
    caseID: Optional[CaseID] = None
    KLE_data: Optional[KLEdata] = None
    FORM_data: Optional[FORMdata] = None
    productionUnit: Optional[ProductionUnit] = None
    education: Optional[Education] = None
    address: Optional[Address] = None
    unstructuredAddress: Optional[UnstructuredAddress] = None
    additionalContentData: Optional[tuple[AdditionalContentData, ...]] = None


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
    mandatory: Optional[bool] = None
    legalNotification: Optional[bool] = None
    postType: Optional[str] = None
    sender: Sender
    recipient: Recipient
    contentData: Optional[ContentData] = None
    forwardData: Optional[ForwardData] = None
    replyData: Optional[tuple[ReplyData, ...]] = None


@dataclass(kw_only=True)
class Message:
    __namespace__ = NAME_SPACES["memo"]
    __attributes__ = {
        "memoVersion": "1.2",
    }
    messageHeader: MessageHeader
    messageBody: Optional[MessageBody] = None


def create_nemsms(message_label: str, message_text: str, sender: Sender, recipient: Recipient) -> Message:
    """Create a Message object that represents a NemSMS message.

    Args:
        message_label: The header text of the NemSMS.
        message_text: The text content of the NemSMS. Max 150 chars.
        sender: A Sender object representing the sender of the message.
        recipient: A Recipient object representing the recipient of the message.

    Returns:
        A Message object representing a NemSMS.
    """
    return Message(
        messageHeader=MessageHeader(
            messageType="NEMSMS",
            messageUUID=str(uuid.uuid4()),
            label=message_label,
            notification=message_text,
            sender=sender,
            recipient=recipient
        )
    )


def create_digital_post_with_main_document(label: str, sender: Sender, recipient: Recipient, files: tuple[File]) -> Message:
    """Create a Message object representing Digital Post with a main document attached.

    Args:
        label: The header text of the message.
        sender: A Sender object representing the sender of the message.
        recipient: A Recipient object representing the recipient of the message.
        files: A tuple of File objects to be attached to the message's main document.

    Returns:
        A Message object.
    """
    return Message(
        messageHeader=MessageHeader(
            messageType="DIGITALPOST",
            messageUUID=str(uuid.uuid4()),
            label=label,
            sender=sender,
            recipient=recipient,
        ),
        messageBody=MessageBody(
            createdDateTime=datetime.now(),
            mainDocument=MainDocument(
                files=files
            )
        )
    )
