"""This module contains tests for xml functionality."""

import unittest
from datetime import date, datetime
import base64
from xml.etree import ElementTree

from python_serviceplatformen.models import message, xml_util
from python_serviceplatformen.models.message import (
    EID, Action, AdditionalContentData, AdditionalDocument, AdditionalReplyData, Address, AddressPoint,
    AttentionData, AttentionPerson, CPRdata, CVRdata, CaseID, ContactInfo, ContactPoint, ContentData,
    ContentResponsible, EMail, Education, EntryPoint, FORMdata, ForwardData, GeneratingSystem, GlobalLocationNumber,
    KLEdata, MainDocument, MessageBody, MessageHeader, MotorVehicle, ProductionUnit, PropertyNumber, ReplyData,
    Reservation, SEnumber, SORdata, Sender, Recipient, File, Message, TechnicalDocument, Telephone, UnstructuredAddress,
    Representative
)

# We don't care about duplicate code in tests
# pylint: disable=R0801


class MessageXMLTest(unittest.TestCase):
    """Test converting Message objects to XML."""

    def test_nemsms(self):
        """Test creating a NemSMS Message object and convert it to XML."""
        m = message.create_nemsms(
            message_label="Label Text",
            message_text="Message Text",
            sender=Sender(
                label="Sender Label",
                senderID="Sender ID",
                idType="CVR"
            ),
            recipient=Recipient(
                label="Recipient Label",
                recipientID="Recipient ID",
                idType="CPR"
            )
        )

        # Set custom uuid for test purposes
        m.messageHeader.messageUUID = "fcdcf318-59b6-427c-9879-4f0af833d593"

        message_xml = xml_util.dataclass_to_xml(m)

        # Compare to example xml
        example_xml = ElementTree.parse("tests/message_xml/MeMo_NemSMS.xml").getroot()
        _xml_compare(message_xml, example_xml)

    def test_digital_post_with_attached_files(self):
        """Test creating a Digital Post message
        with file attachments and convert it to XML.
        """
        m = message.create_digital_post_with_main_document(
            label="Label Text",
            sender=Sender(
                label="Sender Label",
                senderID="Sender ID",
                idType="CVR"
            ),
            recipient=Recipient(
                recipientID="Recipient ID",
                idType="CPR"
            ),
            files=(
                File(
                    encodingFormat="text/plain",
                    filename="File1.txt",
                    language="da",
                    content=base64.b64encode(b"File content 1").decode()
                ),
                File(
                    encodingFormat="text/plain",
                    filename="File2.txt",
                    language="da",
                    content=base64.b64encode(b"File content 2").decode()
                )
            )
        )

        # Set custom properties for test purposes
        m.messageHeader.messageUUID = "78212f5c-6d79-4012-8ed1-e2420243bd17"
        m.messageBody.createdDateTime = datetime(2000, 1, 1, 0, 0, 0)

        message_xml = xml_util.dataclass_to_xml(m)

        # Compare to example xml
        example_xml = ElementTree.parse("tests/message_xml/MeMo_with_attachment.xml").getroot()
        _xml_compare(message_xml, example_xml)

    def test_minimum_example(self):
        """Test converting to xml against the example file at
        https://digitaliser.dk/Media/638683092370780959/MeMo_v1.2_Minimum_Example.xml
        Stored locally at "tests/message_xml/MeMo_Minimum_Example.xml".
        """
        m = Message(
            messageHeader=MessageHeader(
                messageType="DIGITALPOST",
                messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                label="Pladsanvisning",
                sender=Sender(
                    senderID="12345678",
                    idType="CVR",
                    label="Kommunen"
                ),
                recipient=Recipient(
                    recipientID="2211771212",
                    idType="CPR"
                )
            ),
            messageBody=MessageBody(
                createdDateTime=datetime(2024, 5, 3, 12, 0, 0),
                mainDocument=MainDocument(
                    files=[
                        File(
                            encodingFormat="application/pdf",
                            filename="Pladsanvisning.pdf",
                            language="da",
                            content="VGhpcyBpcyBhIHRlc3Q="
                        )
                    ]
                )
            )
        )

        message_xml = xml_util.dataclass_to_xml(m)

        # Compare to example xml
        example_xml = ElementTree.parse("tests/message_xml/MeMo_Minimum_Example.xml").getroot()
        _xml_compare(message_xml, example_xml)

    def test_full_example(self):
        """Test converting to xml against the example file at
        https://digitaliser.dk/Media/638683092408629381/MeMo_v1.2_Full_Example.xml
        Stored locally at "tests/message_xml/MeMo_Full_Example.xml".
        """
        m = Message(
            messageHeader=MessageHeader(
                messageType="DIGITALPOST",
                messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                messageID="MSG-12345",
                messageCode="Pladsanvisning",
                label="Besked fra Børneforvaltningen",
                notification="Du har fået digitalpost fra Kommunen vedr. din ansøgning om børnehaveplads.",
                additionalNotification="Du har fået digitalpost fra Kommunen vedr. din ansøgning om børnehaveplads til Emilie Hansen",
                reply=True,
                replyByDateTime=datetime(2025, 9, 30, 12, 0, 0),
                doNotDeliverUntilDate=date(2025, 9, 15),
                mandatory=True,
                legalNotification=False,
                postType="MYNDIGHEDSPOST",
                sender=Sender(
                    senderID="12345678",
                    idType="CVR",
                    label="Kommunen",
                    attentionData=AttentionData(
                        attentionPerson=AttentionPerson(
                            personID="9000001234",
                            label="Hans Hansen"
                        ),
                        productionUnit=ProductionUnit(
                            productionUnitNumber="1234567890",
                            productionUnitName="Produktionsenhed A"
                        ),
                        globalLocationNumber=GlobalLocationNumber(
                            globalLocationNumber="5798000012345",
                            location="Kommune A"
                        ),
                        email=EMail(
                            emailAddress="info@tusindfryd.dk",
                            relatedAgent="Hans Hansen"
                        ),
                        SE_number=SEnumber(
                            seNumber="12345678",
                            companyName="Kommune A"
                        ),
                        telephone=Telephone(
                            telephoneNumber="12345678",
                            relatedAgent="Hans Hansen"
                        ),
                        eID=EID(
                            eID="CVR:12345678-RID:1234567890123",
                            label="Kommune A"
                        ),
                        contentResponsible=ContentResponsible(
                            contentResponsibleID="22334455",
                            label="Børnehaven, Tusindfryd"
                        ),
                        generatingSystem=GeneratingSystem(
                            generatingSystemID="Sys-1234",
                            label="KommunaltPostSystem"
                        ),
                        SOR_data=SORdata(
                            sorIdentifier="468031000016004",
                            entryName="tekst"
                        ),
                        address=Address(
                            id="8c2ea15d-61fb-4ba9-9366-42f8b194c852",
                            addressLabel="Gaden",
                            houseNumber="7A",
                            door="th",
                            floor="3",
                            co="C/O",
                            zipCode="9000",
                            city="Aalborg",
                            country="DK",
                            addressPoint=AddressPoint(
                                geographicEastingMeasure="557501.23",
                                geographicNorthingMeasure="6336248.89",
                                geographicHeightMeasure="0.0"
                            )
                        ),
                        unstructuredAddress=UnstructuredAddress(
                            unstructured="Bakketoppen 6, 9000 Aalborg"
                        )
                    ),
                    contactPoint=ContactPoint(
                        contactGroup="22.33.44.55",
                        contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                        label="Kommunen, Pladsanvisningen",
                        contactInfo=(
                            ContactInfo(
                                label="Barnets CPR nummer",
                                value="2512169996"
                            ),
                            ContactInfo(
                                label="Barnets navn",
                                value="Emilie Hansen"
                            )
                        )
                    ),
                    representative=Representative(
                        representativeID="87654321",
                        idType="CVR",
                        label="Repræsentant Kommune"
                    )
                ),
                recipient=Recipient(
                    recipientID="2211771212",
                    idType="CPR",
                    label="Mette Hansen",
                    attentionData=AttentionData(
                        attentionPerson=AttentionPerson(
                            personID="2211771212",
                            label="Mette Hansen"
                        ),
                        productionUnit=ProductionUnit(
                            productionUnitNumber="1234567890",
                            productionUnitName="[Produktionsenhed]"
                        ),
                        globalLocationNumber=GlobalLocationNumber(
                            globalLocationNumber="5798000012345",
                            location="[Navn på lokation]"
                        ),
                        email=EMail(
                            emailAddress="m.hansen@gmail.com",
                            relatedAgent="Mette Hansen"
                        ),
                        SE_number=SEnumber(
                            seNumber="12345678",
                            companyName="[Virksomhed]"
                        ),
                        telephone=Telephone(
                            telephoneNumber="12345678",
                            relatedAgent="Mette Hansen"
                        ),
                        eID=EID(
                            eID="12345678_1234567890",
                            label="[Virksomhed]"
                        ),
                        contentResponsible=ContentResponsible(
                            contentResponsibleID="22334455",
                            label="[Ansvarlig]"
                        ),
                        SOR_data=SORdata(
                            sorIdentifier="468031000016004",
                            entryName="[SOR tekst]"
                        ),
                        unstructuredAddress=UnstructuredAddress(
                            unstructured="Bakketoppen 6, 9000 Aalborg"
                        ),
                        address=Address(
                            id="8c2ea15d-61fb-4ba9-9366-42f8b194c852",
                            addressLabel="Gaden",
                            houseNumber="7A",
                            door="th",
                            floor="3",
                            co="C/O",
                            zipCode="9000",
                            city="Aalborg",
                            country="DK",
                            addressPoint=AddressPoint(
                                geographicEastingMeasure="557501.23",
                                geographicNorthingMeasure="6336248.89",
                                geographicHeightMeasure="0.0"
                            )
                        )
                    ),
                    contactPoint=ContactPoint(
                        contactGroup="22.33.44.55",
                        contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                        label="Kommunen, Pladsanvisningen",
                        contactInfo=(
                            ContactInfo(
                                label="Barnets CPR nummer",
                                value="2512169996"
                            ),
                            ContactInfo(
                                label="Barnets navn",
                                value="Emilie Hansen"
                            )
                        )
                    )
                ),
                contentData=ContentData(
                    CPR_data=CPRdata(
                        cprNumber="2512169996",
                        name="Emilie Hansen"
                    ),
                    CVR_data=CVRdata(
                        cvrNumber="12345678",
                        companyName="[Virksomhed]"
                    ),
                    motorVehicle=MotorVehicle(
                        licenseNumber="AB12345",
                        chassisNumber="WFR18ZZ67W094959"
                    ),
                    propertyNumber=PropertyNumber(
                        propertyNumber="ABC1234"
                    ),
                    caseID=CaseID(
                        caseID="SAG-12345",
                        caseSystem="Sagssystem 1234"
                    ),
                    KLE_data=KLEdata(
                        subjectKey="00.00.00",
                        version="Maj 2018",
                        activityFacet="[Tekst]",
                        label="[KLE tekst]"
                    ),
                    FORM_data=FORMdata(
                        taskKey="00.00.00.00",
                        version="Opgavenøglen v2.12",
                        activityFacet="Tekst]",
                        label="[FORM tekst]"
                    ),
                    productionUnit=ProductionUnit(
                        productionUnitNumber="1234567890",
                        productionUnitName="[Produktionsenhed]"
                    ),
                    education=Education(
                        educationCode="123ABC",
                        educationName="[Uddannelse navn]"
                    ),
                    additionalContentData=(
                        AdditionalContentData(
                            contentDataType="Liste A",
                            contentDataName="Navn 1",
                            contentDataValue="Værdi 1"
                        ),
                        AdditionalContentData(
                            contentDataType="Liste A",
                            contentDataName="Navn 2",
                            contentDataValue="Værdi 2"
                        )
                    )
                ),
                forwardData=ForwardData(
                    messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                    originalMessageDateTime=datetime(2021, 3, 15, 12, 0, 0),
                    originalSender="Kommunen",
                    originalContentResponsible="Børnehaven, Tusindfryd",
                    originalRepresentative="Repræsentant Kommune",
                    contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                    comment="kommentar til modtageren"
                ),
                replyData=(
                    ReplyData(
                        messageID="MSG-12344",
                        messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                        senderID="12345678",
                        recipientID="1234567890",
                        caseID="SAG-456",
                        contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                        generatingSystemID="ABC-123",
                        comment="Tilbud om børnehaveplads til Emilie Hansen",
                        additionalReplyData=(
                            AdditionalReplyData(
                                label="Intern note",
                                value="tekst"
                            ),
                            AdditionalReplyData(
                                label="Intern reference",
                                value="tekst"
                            )
                        )
                    ),
                    ReplyData(
                        messageID="MSG-12345",
                        messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C657",
                        replyUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                        senderID="1234567890",
                        recipientID="12345678",
                        caseID="SAG-4567",
                        contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                        generatingSystemID="ABC-1234",
                        comment="tekst",
                        additionalReplyData=(
                            AdditionalReplyData(
                                label="Intern note",
                                value="tekst"
                            ),
                            AdditionalReplyData(
                                label="Intern reference",
                                value="tekst"
                            ),
                            AdditionalReplyData(
                                label="Vedr",
                                value="tekst"
                            ),
                            AdditionalReplyData(
                                label="Att",
                                value="tekst"
                            )
                        )
                    )
                )
            ),
            messageBody=MessageBody(
                createdDateTime=datetime(2018, 5, 3, 12, 0, 0),
                mainDocument=MainDocument(
                    mainDocumentID="456",
                    label="Tilbud om børnehaveplads",
                    files=(
                        File(
                            encodingFormat="application/pdf",
                            filename="Pladsanvisning.pdf",
                            language="da",
                            content="VGhpcyBpcyBhIHRlc3Q="
                        ),
                        File(
                            encodingFormat="text/plain",
                            filename="Pladsanvisning.txt",
                            language="da",
                            content="VGhpcyBpcyBhIHRlc3Q="
                        )
                    ),
                    actions=(
                        Action(
                            label="Spørgeskema",
                            actionCode="SELVBETJENING",
                            startDateTime=datetime(2018, 11, 9, 12, 0, 0),
                            endDateTime=datetime(2018, 12, 9, 12, 0, 0),
                            entryPoint=EntryPoint(
                                url="https://www.tusindfryd.dk/spørgeskema.html"
                            )
                        ),
                        Action(
                            label="Opret aftale i kalender",
                            actionCode="AFTALE",
                            startDateTime=datetime(2018, 11, 10, 9, 0, 0),
                            endDateTime=datetime(2018, 11, 9, 12, 0, 0),
                            reservation=Reservation(
                                description="Opstart Tusindfryd",
                                reservationUUID="8C2EA15D-61FB-4BA9-9366-42F8B194D241",
                                abstract="Opstart",
                                location="Gl. Landevej 61, 9000 aalborg, Rød stue",
                                startDateTime=datetime(2018, 11, 10, 9, 0, 0),
                                endDateTime=datetime(2018, 11, 10, 12, 0, 0),
                                organizerMail="info@tusindfryd.dk",
                                organizerName="Jette Hansen"
                            )
                        )
                    )
                ),
                additionalDocuments=(
                    AdditionalDocument(
                        additionalDocumentID="789",
                        label="Tilbud om børnehaveplads",
                        files=(
                            File(
                                encodingFormat="application/pdf",
                                filename="Pladsanvisning.pdf",
                                language="da",
                                content="VGhpcyBpcyBhIHRlc3Q="
                            ),
                            File(
                                encodingFormat="application/msword",
                                filename="Praktiske oplysninger.doc",
                                language="da",
                                content="VGhpcyBpcyBhIHRlc3Q="
                            )
                        ),
                        actions=(
                            Action(
                                label="Tusindfryd hjemmeside",
                                actionCode="INFORMATION",
                                startDateTime=datetime(2018, 11, 10, 9, 0, 0),
                                endDateTime=datetime(2018, 11, 9, 12, 0, 0),
                                entryPoint=EntryPoint(
                                    url="https://www.tusindfryd.dk"
                                )
                            ),
                            Action(
                                label="Opret aftale i kalender",
                                actionCode="AFTALE",
                                reservation=Reservation(
                                    description="Introduktion til nye forældre",
                                    reservationUUID="8C2EA15D-61FB-4BA9-9366-42F8B194E845",
                                    abstract="Invitation",
                                    location="Gl. Landevej 61, 9000 Aalborg",
                                    startDateTime=datetime(2018, 11, 10, 19, 0, 0),
                                    endDateTime=datetime(2018, 11, 10, 20, 30, 0),
                                    organizerMail="info@tusindfryd.dk",
                                    organizerName="Jette Hansen"
                                )
                            )
                        )
                    ),
                    AdditionalDocument(
                        additionalDocumentID="678",
                        label="Tilbud om børnehaveplads, vejledning",
                        files=(
                            File(
                                encodingFormat="application/pdf",
                                filename="vejledning.pdf",
                                language="da",
                                content="VGhpcyBpcyBhIHRlc3Q="
                            )
                        ),
                        actions=(
                            Action(
                                label="Register opslag",
                                actionCode="SELVBETJENING",
                                startDateTime=datetime(2018, 11, 10, 9, 0, 0),
                                endDateTime=datetime(2018, 11, 9, 12, 0, 0),
                                entryPoint=EntryPoint(
                                    url="https://registration.nemhandel.dk/NemHandelRegisterWeb/public/participant/info?key=5798009811578&keytype=GLN"
                                )
                            )
                        )
                    )
                ),
                technicalDocuments=(
                    TechnicalDocument(
                        technicalDocumentID="222555",
                        label="Teknisk dokument",
                        files=(
                            File(
                                encodingFormat="text/xml",
                                filename="TekniskDokument.xml",
                                language="da",
                                content="VGhpcyBpcyBhIHRlc3Q="
                            )
                        )
                    )
                )
            )
        )

        message_xml = xml_util.dataclass_to_xml(m)

        # Compare to example xml
        example_xml = ElementTree.parse("tests/message_xml/MeMo_Full_Example.xml").getroot()
        _xml_compare(message_xml, example_xml)


def _xml_compare(x1: ElementTree.Element, x2: ElementTree.Element, path = "") -> None:
    """Compare two xml elements recursively.

    Args:
        x1: The first element to compare.
        x2: The second element to compare
        path: The path to the elements used in error messages. Defaults to "".

    Raises:
        ValueError: If the elements or their children don't match.
    """
    main_error = ValueError(f"Elements {x1.tag} and {x2.tag} doesn't match. Path: {path}")
    if x1.tag != x2.tag:
        raise ValueError(f'Tags do not match: {x1.tag} != {x2.tag}') from main_error

    for name, value in x1.attrib.items():
        value_2 = x2.attrib.get(name)
        if value_2 != value:
            raise ValueError(f'Attribute {name} do not match: {value} != {value_2}') from main_error

    for name in x2.attrib.keys():
        if name not in x1.attrib:
            raise ValueError(f'x2 has an attribute x1 is missing: {name}') from main_error

    if not _text_compare(x1.text, x2.text):
        raise ValueError(f"Text value doesn't match: {x1.text} != {x2.text}") from main_error

    if not _text_compare(x1.tail, x2.tail):
        raise ValueError(f"Tail doesn't match: {x1.tail} != {x2.tail}") from main_error

    if len(x1) != len(x2):
        l1 = (t.tag for t in x1)
        l2 = (t.tag for t in x2)
        diff = set(l1) ^ set(l2)
        raise ValueError(f"Children length differs {len(x1)} != {len(x2)} - Diff: {'; '.join(diff)}") from main_error

    for c1, c2 in zip(x1, x2):
        _xml_compare(c1, c2, f"{path} -> {x1.tag}")


def _text_compare(s1: str | None, s2: str | None) -> bool:
    """Compare two strings that might be None.
    Ignores leading and trailing whitespace.

    Args:
        s1: The first string to compare.
        s2: The second string to compare.

    Returns:
        True if the strings match.
    """
    return (s1 or '').strip() == (s2 or '').strip()


if __name__ == "__main__":
    unittest.main()
