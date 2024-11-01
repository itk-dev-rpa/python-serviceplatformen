# python_serviceplatformen

This project is made to make it easier to use Kombit's Serviceplatformen API.

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
kombit_access = KombitAccess(cvr="12345678", cert_path="C:\something\Certificate.pem", test=False)
```

If you want to use the test system instead pass `test=True` to KombitAccess.

## Digital Post

This library supports the full functionality of Digital Post including NemSMS.

### Check registration

You can easily check if someone is registered for Digital Post or NemSMS:

```python
digital_post.is_registered(cpr="1234567890", service="digitalpost", kombit_access=kombit_access)
digital_post.is_registered(cpr="1234567890", service="nemsms", kombit_access=kombit_access)
```

### MeMo model

A detailed data class model has been defined to help define MeMo objects which are used
in the api.

The entire model is located in the message module:

```python
from python_serviceplatformen.models.message import Message
```

A detailed description of the model and all attributes can be found in the official documentation:
[MeMo - Digitaliser.dk](https://digitaliser.dk/digital-post/vejledninger/memo)

**Note:** The model doesn't follow the normal python naming conventions to follow the source names as close as possible.

### Send Digital Post

To send a message construct a message object and then send it off to the send_message function:

```python
import uuid
from datetime import datetime
import base64

from python_serviceplatformen.authentication import KombitAccess
from python_serviceplatformen import digital_post
from python_serviceplatformen.models.message import (
    Message, MessageHeader, Sender, Recipient, MessageBody, MainDocument, File
)

kombit_access = KombitAccess(cvr="55133018", cert_path=r"C:\Users\az68933\Desktop\SF1601\Certificate.pem")

m = Message(
    messageHeader=MessageHeader(
        messageType="DIGITALPOST",
        messageUUID=str(uuid.uuid4()),
        label="Digital Post test message",
        mandatory=False,
        legalNotification=False,
        sender=Sender(
            senderID="12345678",
            idType="CVR",
            label="Python Serviceplatformen"
        ),
        recipient=Recipient(
            recipientID="1234567890",
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

digital_post.send_message("Digital Post", m, kombit_access)
```

### Recipes

The message module also contains a few static helper functions to construct simple messages. These are not meant to
be all encompassing but to help as a starting point.

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
DIGITAL_POST_TEST_CPR = "xxxxxxxxxx"  # The receiver of the test messages
```

### Running the tests

To run all tests open a command line in the project folder and run:

```bash
python -m unittest
```
