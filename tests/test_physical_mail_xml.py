"""This module contains tests for physical mail XML functionality."""

import unittest
from xml.etree import ElementTree

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from python_serviceplatformen.models.physical_mail import (
    AfsendelseIdentifikator,
    AfsendelseModtager,
    CPRnummerIdentifikator,
    CountryIdentificationCode,
    CountryIdentificationSchemeType,
    DokumentParametre,
    FilformatNavn,
    ForsendelseI,
    ForsendelseModtager,
    ForsendelseTypeIdentifikator,
    MeddelelseIndholdData,
    ModtagerAdresse,
    PersonName,
    PostCodeIdentifier,
    StreetBuildingIdentifier,
    StreetName,
    TransaktionsParametreI,
)
from tests.xml_compare import xml_compare

# We don't care about duplicate code in tests
# pylint: disable=R0801


class PhysicalMailXMLTest(unittest.TestCase):
    """Test converting physical mail dataclasses to XML."""

    def test_minimal_forsendelse(self):
        """Build a minimal ForsendelseI dataclass and compare its
        serialized XML to tests/physical_mail_xml/ForsendelseI_Minimal.xml.
        """
        with open("tests/physical_mail_xml/ForsendelseI_Minimal.xml", encoding="utf-8") as f:
            expected_xml = ElementTree.fromstring(f.read())

        forsendelse = ForsendelseI(
            afsendelse_identifikator=AfsendelseIdentifikator(value="dc3303Soa44e-9c1c-46aaf36974de"),
            forsendelse_type_identifikator=ForsendelseTypeIdentifikator(value=265),
            forsendelse_modtager=ForsendelseModtager(
                afsendelse_modtager=AfsendelseModtager(
                    cpr_nummer_identifikator=CPRnummerIdentifikator(value="0000000000")
                ),
                modtager_adresse=ModtagerAdresse(
                    person_name=PersonName(value="Test Testesen"),
                    street_name=StreetName(value="Testvej"),
                    street_building_identifier=StreetBuildingIdentifier(value="3"),
                    post_code_identifier=[PostCodeIdentifier(value="2300")],
                    country_identification_code=CountryIdentificationCode(
                        value="DK",
                        scheme=CountryIdentificationSchemeType.ISO3166_ALPHA2,
                    ),
                ),
            ),
            filformat_navn=FilformatNavn(value="pdf"),
            meddelelse_indhold_data=MeddelelseIndholdData(value="VGhpcyBpcyBhIHRlc3Q="),
            transaktions_parametre_i=TransaktionsParametreI(),
            dokument_parametre=DokumentParametre(),
        )

        serializer = XmlSerializer(
            context=XmlContext(),
            config=SerializerConfig(xml_declaration=False),
        )
        actual_xml = ElementTree.fromstring(serializer.render(forsendelse))

        xml_compare(actual_xml, expected_xml)


if __name__ == "__main__":
    unittest.main()
