import unittest
from datetime import date, datetime
import base64
from xml.etree import ElementTree

from python_serviceplatformen.models import message, xml_util
from python_serviceplatformen.models.message import EID, Action, AdditionalContentData, AdditionalDocument, AdditionalReplyData, Address, AddressPoint, AttentionData, AttentionPerson, CPRdata, CVRdata, CaseID, ContactInfo, ContactPoint, ContentData, ContentResponsible, EMail, Education, EntryPoint, FORMdata, ForwardData, GeneratingSystem, GlobalLocationNumber, KLEdata, MainDocument, MessageBody, MessageHeader, MotorVehicle, ProductionUnit, PropertyNumber, ReplyData, Reservation, SEnumber, SORdata, Sender, Recipient, File, Message, TechnicalDocument, Telephone, UnstructuredAddress

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
            ),
            message_uuid="Message UUID"
        )

        s = xml_util.dataclass_to_xml_string(m)

        self.assertIsInstance(s, str)
        # TODO: Read this from external files

    def test_digital_post_with_attached_files(self):
        """Test creating a Digital Post message
        with file attachments and convert it to XML.
        """
        m = message.create_digital_post_with_attached_files(
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
            message_uuid="Message UUID",
            created_datetime=datetime(2000, 1, 1),
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

        s = xml_util.dataclass_to_xml_string(m)

        self.assertIsInstance(s, str)
        # TODO: Read this from external files

    def test_minimum_example(self):
        """Test converting to xml against the example file at
        https://digitaliser.dk/Media/638142936404764960/MeMo_Minimum_Example.xml
        Stored locally at "tests/message_xml/MeMo_Minimum_Example.xml".
        """
        m = Message(
            MessageHeader=MessageHeader(
                messageType="DIGITALPOST",
                messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                label="Pladsanvisning",
                mandatory=False,
                legalNotification=False,
                Sender=Sender(
                    senderID="12345678",
                    idType="CVR",
                    label="Kommunen"
                ),
                Recipient=Recipient(
                    recipientID="2211771212",
                    idType="CPR"
                )
            ),
            MessageBody_=MessageBody(
                createdDateTime=datetime(2018, 5, 3, 12, 0, 0),
                MainDocument=MainDocument(
                    Files=[
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

        # Check against schema
        xml_util.validate_memo(message_xml)

        # Compare to example xml
        example_xml = ElementTree.parse("tests/message_xml/MeMo_Minimum_Example.xml").getroot()
        _xml_compare(message_xml, example_xml)

    def test_full_example(self):
        """Test converting to xml against the example file at
        https://digitaliser.dk/Media/638142936375938205/MeMo_Full_Example.xml
        Stored locally at "tests/message_xml/MeMo_Full_Example.xml".
        """
        m = Message(
            MessageHeader=MessageHeader(
                messageType="DIGITALPOST",
                messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                messageID="MSG-12345",
                messageCode="Pladsanvisning",
                label="Besked fra Børneforvaltningen",
                notification="Du har fået digitalpost fra Kommunen vedr. din ansøgning om børnehaveplads.",
                additionalNotification="Du har fået digitalpost fra Kommunen vedr. din ansøgning om børnehaveplads til Emilie Hansen",
                reply=True,
                replyByDateTime=datetime(2018, 9, 30, 12, 0, 0),
                doNotDeliverUntilDate=date(2018, 9, 15),
                mandatory=False,
                legalNotification=False,
                postType="MYNDIGHEDSPOST",
                Sender=Sender(
                    senderID="12345678",
                    idType="CVR",
                    label="Kommunen",
                    AttentionData_=AttentionData(
                        AttentionPerson_=AttentionPerson(
                            personID="9000001234",
                            label="Hans Hansen"
                        ),
                        ProductionUnit_=ProductionUnit(
                            productionUnitNumber="1234567890",
                            productionUnitName="Produktionsenhed A"
                        ),
                        GlobalLocationNumber_=GlobalLocationNumber(
                            globalLocationNumber="5798000012345",
                            location="Kommune A"
                        ),
                        EMail_=EMail(
                            emailAddress="info@tusindfryd.dk",
                            relatedAgent="Hans Hansen"
                        ),
                        SEnumber_=SEnumber(
                            seNumber="12345678",
                            companyName="Kommune A"
                        ),
                        Telephone_=Telephone(
                            telephoneNumber="12345678",
                            relatedAgent="Hans Hansen"
                        ),
                        EID_=EID(
                            eID="CVR:12345678-RID:1234567890123",
                            label="Kommune A"
                        ),
                        ContentResponsible_=ContentResponsible(
                            contentResponsibleID="22334455",
                            label="Børnehaven, Tusindfryd"
                        ),
                        GeneratingSystem_=GeneratingSystem(
                            generatingSystemID="Sys-1234",
                            label="KommunaltPostSystem"
                        ),
                        SORdata_=SORdata(
                            sorIdentifier="468031000016004",
                            entryName="tekst"
                        ),
                        Address_=Address(
                            id="8c2ea15d-61fb-4ba9-9366-42f8b194c852",
                            addressLabel="Gaden",
                            houseNumber="7A",
                            door="th",
                            floor="3",
                            co="C/O",
                            zipCode="9000",
                            city="Aalborg",
                            country="DK",
                            AddressPoint=AddressPoint(
                                geographicEastingMeasure="557501.23",
                                geographicNorthingMeasure="6336248.89",
                                geographicHeightMeasure="0.0"
                            )
                        )
                    ),
                    ContactPoint_=ContactPoint(
                        contactGroup="22.33.44.55",
                        contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                        label="Kommunen, Pladsanvisningen",
                        ContactInfo_=(
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
                ),
                Recipient=Recipient(
                    recipientID="2211771212",
                    idType="CPR",
                    label="Mette Hansen",
                    AttentionData_=AttentionData(
                        AttentionPerson_=AttentionPerson(
                            personID="2211771212",
                            label="Mette Hansen"
                        ),
                        ProductionUnit_=ProductionUnit(
                            productionUnitNumber="1234567890",
                            productionUnitName="[Produktionsenhed]"
                        ),
                        GlobalLocationNumber_=GlobalLocationNumber(
                            globalLocationNumber="5798000012345",
                            location="[Navn på lokation]"
                        ),
                        EMail_=EMail(
                            emailAddress="m.hansen@gmail.com",
                            relatedAgent="Mette Hansen"
                        ),
                        SEnumber_=SEnumber(
                            seNumber="12345678",
                            companyName="[Virksomhed]"
                        ),
                        Telephone_=Telephone(
                            telephoneNumber="12345678",
                            relatedAgent="Mette Hansen"
                        ),
                        EID_=EID(
                            eID="12345678_1234567890",
                            label="[Virksomhed]"
                        ),
                        ContentResponsible_=ContentResponsible(
                            contentResponsibleID="22334455",
                            label="[Ansvarlig]"
                        ),
                        SORdata_=SORdata(
                            sorIdentifier="468031000016004",
                            entryName="[SOR tekst]"
                        ),
                        UnstructuredAddress_=UnstructuredAddress(
                            unstructured="Bakketoppen 6, 9000 Aalborg"
                        )
                    ),
                    ContactPoint_=ContactPoint(
                        contactGroup="22.33.44.55",
                        contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                        label="Kommunen, Pladsanvisningen",
                        ContactInfo_=(
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
                ContentData_=ContentData(
                    CPRdata_=CPRdata(
                        cprNumber="2512169996",
                        name="Emilie Hansen"
                    ),
                    CVRdata_=CVRdata(
                        cvrNumber="12345678",
                        companyName="[Virksomhed]"
                    ),
                    MotorVehicle_=MotorVehicle(
                        licenseNumber="AB12345",
                        chassisNumber="WFR18ZZ67W094959"
                    ),
                    PropertyNumber_=PropertyNumber(
                        propertyNumber="ABC1234"
                    ),
                    CaseID_=CaseID(
                        caseID="SAG-12345",
                        caseSystem="Sagssystem 1234"
                    ),
                    KLEdata_=KLEdata(
                        subjectKey="00.00.00",
                        version="Maj 2018",
                        activityFacet="[Tekst]",
                        label="[KLE tekst]"
                    ),
                    FORMdata_=FORMdata(
                        taskKey="00.00.00.00",
                        version="Opgavenøglen v2.12",
                        activityFacet="Tekst]",
                        label="[FORM tekst]"
                    ),
                    ProductionUnit_=ProductionUnit(
                        productionUnitNumber="1234567890",
                        productionUnitName="[Produktionsenhed]"
                    ),
                    Education_=Education(
                        educationCode="123ABC",
                        educationName="[Uddannelse navn]"
                    ),
                    AdditionalContentData_=(
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
                ForwardData_=ForwardData(
                    messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                    originalMessageDateTime=datetime(2021, 3, 15, 12, 0, 0),
                    originalSender="Kommunen",
                    originalContentResponsible="Børnehaven, Tusindfryd",
                    contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                    comment="kommentar til modtageren"
                ),
                ReplyData_=(
                    ReplyData(
                        messageID="MSG-12344",
                        messageUUID="8C2EA15D-61FB-4BA9-9366-42F8B194C114",
                        senderID="12345678",
                        recipientID="1234567890",
                        caseID="SAG-456",
                        contactPointID="241d39f6-998e-4929-b198-ccacbbf4b330",
                        generatingSystemID="ABC-123",
                        comment="Tilbud om børnehaveplads til Emilie Hansen",
                        AdditionalReplyData_=(
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
                        AdditionalReplyData_=(
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
            MessageBody_=MessageBody(
                createdDateTime=datetime(2018, 5, 3, 12, 0, 0),
                MainDocument=MainDocument(
                    mainDocumentID="456",
                    label="Tilbud om børnehaveplads",
                    Files=(
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
                    Actions=(
                        Action(
                            label="Spørgeskema",
                            actionCode="SELVBETJENING",
                            startDateTime=datetime(2018, 11, 9, 12, 0, 0),
                            endDateTime=datetime(2018, 12, 9, 12, 0, 0),
                            EntryPoint_=EntryPoint(
                                url="http://www.tusindfryd.dk/spørgeskema.html"
                            )
                        ),
                        Action(
                            label="Opret aftale i kalender",
                            actionCode="AFTALE",
                            startDateTime=datetime(2018, 11, 10, 9, 0, 0),
                            endDateTime=datetime(2018, 11, 9, 12, 0, 0),
                            Reservation_=Reservation(
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
                AdditionalDocuments=(
                    AdditionalDocument(
                        additionalDocumentID="789",
                        label="Tilbud om børnehaveplads",
                        Files=(
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
                        Actions=(
                            Action(
                                label="Tusindfryd hjemmeside",
                                actionCode="INFORMATION",
                                startDateTime=datetime(2018, 11, 10, 9, 0, 0),
                                endDateTime=datetime(2018, 11, 9, 12, 0, 0),
                                EntryPoint_=EntryPoint(
                                    url="http://www.tusindfryd.dk"
                                )
                            ),
                            Action(
                                label="Opret aftale i kalender",
                                actionCode="AFTALE",
                                Reservation_=Reservation(
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
                        Files=(
                            File(
                                encodingFormat="application/pdf",
                                filename="vejledning.pdf",
                                language="da",
                                content="VGhpcyBpcyBhIHRlc3Q="
                            )
                        ),
                        Actions=(
                            Action(
                                label="Register opslag",
                                actionCode="SELVBETJENING",
                                startDateTime=datetime(2018, 11, 10, 9, 0, 0),
                                endDateTime=datetime(2018, 11, 9, 12, 0, 0),
                                EntryPoint_=EntryPoint(
                                    url="http://registration.nemhandel.dk/NemHandelRegisterWeb/public/participant/info?key=5798009811578&keytype=GLN"
                                )
                            )
                        )
                    )
                ),
                TechnicalDocuments=(
                    TechnicalDocument(
                        technicalDocumentID="222555",
                        label="Teknisk dokument",
                        Files=(
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

        message_xml = xml_util.dataclass_to_xml(m, message.NAME_SPACES)

        # Check against schema
        xml_util.validate_memo(message_xml)

        # Compare to example xml
        example_xml = ElementTree.parse("tests/message_xml/MeMo_Full_Example.xml").getroot()
        _xml_compare(message_xml, example_xml)


def _xml_compare(x1: ElementTree.Element, x2: ElementTree.Element, path = "") -> None:
    """Compare two xml elements recursively.

    Args:
        x1: The first element to compare.
        x2: The second element to compare
        path: The path to the elements. Defaults to "".

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
        raise ValueError(f"Children length differs {len(x1)} != {len(x2)}")

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
