"""Tests of the Kombit Digital Post API."""
from datetime import datetime
import unittest
import os
import uuid
import base64

from dotenv import load_dotenv

from python_serviceplatformen.authentication import KombitAccess
from python_serviceplatformen import digital_post
from python_serviceplatformen.models.message import Message, MessageBody, MessageHeader, File, Sender, Recipient, MainDocument
from python_serviceplatformen.models import message

load_dotenv(override=True)

# We don't care about duplicate code in tests
# pylint: disable=R0801


class DigitalPostTest(unittest.TestCase):
    """Test Digital Post functionality in the Kombit API."""

    @classmethod
    def setUpClass(cls) -> None:
        cvr = os.environ["KOMBIT_TEST_CVR"]
        cert_path = os.environ["KOMBIT_TEST_CERT_PATH"]
        cls.kombit_access = KombitAccess(cvr=cvr, cert_path=cert_path, test=True)

    def test_is_registered(self):
        """Test getting registration status."""
        cpr = os.environ['DIGITAL_POST_TEST_CPR']

        result = digital_post.is_registered(id_=cpr, service="digitalpost", kombit_access=self.kombit_access)
        self.assertTrue(result)

        result = digital_post.is_registered(id_=cpr, service="nemsms", kombit_access=self.kombit_access)
        self.assertTrue(result)

        cvr = os.environ["KOMBIT_TEST_CVR"]

        result = digital_post.is_registered(id_=cvr, service="digitalpost", kombit_access=self.kombit_access)
        self.assertTrue(result)

        # Test with nonsense.
        # This should result in False
        result = digital_post.is_registered(id_="FooBar", service="digitalpost", kombit_access=self.kombit_access)
        self.assertFalse(result)

        result = digital_post.is_registered(id_="FooBar", service="nemsms", kombit_access=self.kombit_access)
        self.assertFalse(result)

    def test_send_message(self):
        """Test sending a simple message."""
        cpr = os.environ['DIGITAL_POST_TEST_CPR']

        m = Message(
            messageHeader=MessageHeader(
                messageType="DIGITALPOST",
                messageUUID=str(uuid.uuid4()),
                label="Python Serviceplatformen Test (Send Message)",
                sender=Sender(
                    senderID=os.environ["KOMBIT_TEST_CVR"],
                    idType="CVR",
                    label="Python Serviceplatformen"
                ),
                recipient=Recipient(
                    recipientID=cpr,
                    idType="CPR"
                )
            ),
            messageBody=MessageBody(
                createdDateTime=datetime.now(),
                mainDocument=MainDocument(
                    files=[
                        File(
                            encodingFormat="text/plain",
                            filename="Besked.txt",
                            language="da",
                            content=base64.b64encode(b"Hello World").decode()
                        )
                    ]
                )
            )
        )

        digital_post.send_message("Digital Post", m, self.kombit_access)

    def test_send_digital_post_with_main_document(self):
        """Test the helper function for creating a message with a main document."""
        cpr = os.environ['DIGITAL_POST_TEST_CPR']

        m = message.create_digital_post_with_main_document(
            label="Python Serviceplatformen Test (With main document)",
            sender=Sender(
                senderID=os.environ["KOMBIT_TEST_CVR"],
                idType="CVR",
                label="Python Serviceplatformen"
            ),
            recipient=Recipient(
                recipientID=cpr,
                idType="CPR"
            ),
            files=[
                File(
                    encodingFormat="text/plain",
                    filename="Besked.txt",
                    language="da",
                    content=base64.b64encode(b"Hello World").decode()
                )
            ]
        )

        digital_post.send_message("Digital Post", m, self.kombit_access)


if __name__ == '__main__':
    unittest.main()
