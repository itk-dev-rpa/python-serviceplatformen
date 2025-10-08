"""Tests of Kombit API authentication."""
import unittest
import os

from dotenv import load_dotenv

from python_serviceplatformen.authentication import KombitAccess

load_dotenv()

# We don't care about duplicate code in tests
# pylint: disable=R0801


class KombitAuthTest(unittest.TestCase):
    """Test authentication against the Kombit API."""

    def test_kombit_access(self):
        """Test authentication."""
        cvr = os.environ["KOMBIT_TEST_CVR"]
        cert_path = os.environ["KOMBIT_TEST_CERT_PATH"]
        ka = KombitAccess(cvr=cvr, cert_path=cert_path, test=True)

        # Test getting a SAML token
        saml_token = ka.get_saml_token("http://entityid.kombit.dk/service/postforespoerg/1")
        self.assertIsInstance(saml_token, str)
        self.assertGreater(len(saml_token), 0)

        # Test reuse of SAML token
        saml_token2 = ka.get_saml_token("http://entityid.kombit.dk/service/postforespoerg/1")
        self.assertEqual(saml_token, saml_token2)

        # Test getting an access token
        access_token = ka.get_access_token("http://entityid.kombit.dk/service/postforespoerg/1")
        self.assertIsInstance(access_token, str)
        self.assertGreater(len(access_token), 0)

        # Test reuse of access token
        access_token2 = ka.get_access_token("http://entityid.kombit.dk/service/postforespoerg/1")
        self.assertEqual(access_token, access_token2)

        # Test getting a nonsense token
        with self.assertRaises(ValueError):
            ka.get_saml_token("FooBar")

        # Test getting a nonsense token
        with self.assertRaises(ValueError):
            ka.get_access_token("FooBar")


if __name__ == '__main__':
    unittest.main()
