# python_serviceplatformen

This project is made to hopefully make it easier to use Kombit's Serviceplatformen API.

## Certificates and authentication

To use Kombit's Serviceplatformen you need a valid OCES3 certificate registered for your project.
Ask your local Kombit systems architect for help with this.

You need specific access to each service on Serviceplatformen you want to use.
One certificate can have access to multiple services.

This project needs your certificate to be in a unified PEM format. That is
with the public and private key in a single file.

If your certificate is in P12-format you can convert it using openssl:

```bash
openssl pkcs12 -in Certificate.p12 -out Certificate.pem -nodes
```

Due to limitations in Python's implementation of SSL your certificate needs to exist as
a file on the system while using this library.

When your certificate is registered and in PEM-format, you simply hand it to the KombitAccess
class and it will handle the rest for you.

```python
from python_serviceplatformen.authentication import KombitAccess
ka = KombitAccess(cvr=cvr, cert_path=cert_path)
```

## Tests

This project contains automated tests in the "tests" folder.
To run these test you need to install the developer dependecies:

```bash
pip install python_serviceplatformen[dev]
```

### Environment variables

Create a .env file in the project folder and fill out these variables:

```yaml
KOMBIT_TEST_CVR = "XXXXXXXX"  # The cvr of the organization who owns the certificate
KOMBIT_TEST_CERT_PATH = "C:\something\Certificate.pem"  # The path to the certificate file
```
