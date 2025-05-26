import os
import subprocess

import proton
from proton import SSLDomain
from proton.handlers import MessagingHandler
from proton.reactor import Container
from proton.utils import BlockingConnection

from python_serviceplatformen.authentication import KombitAccess


URL = "amqp://beskedfordeler.eksterntest-stoettesystemerne.dk:5671"
URL = "beskedfordeler.eksterntest-stoettesystemerne.dk:5671"
QUEUE = "your-queue-name"

CERT_PATH = "/mnt/c/Users/az68933/Desktop/SF1601/Certificate.crt.pem"
KEY_PATH = "/mnt/c/Users/az68933/Desktop/SF1601/Certificate.key.pem"
CERT_BUNDLE_PATH = "/mnt/c/Users/az68933/Desktop/SF1601/Certificate.pem"
CA_CERT = "/mnt/c/Users/az68933/Desktop/SF1601/BFO_EXTTEST_Beskedfordeler_1.cer"

class TLSExternalReceiver(MessagingHandler):
    def __init__(self, url, queue_name, ssl_domain):
        super().__init__()
        self.url = url
        self.queue_name = queue_name
        self.ssl_domain = ssl_domain

    def on_start(self, event):
        print("Start")
        conn = event.container.connect(
            self.url,
            ssl_domain=self.ssl_domain,
            sasl_enabled=True,
            allowed_mechs='EXTERNAL'
        )
        event.container.create_receiver(conn, self.queue_name)
        print("Started")

    def on_message(self, event):
        print("Received message:", event.message.body)

def create_ssl_domain():
    ssl_domain = SSLDomain(SSLDomain.MODE_CLIENT)
    ssl_domain.set_credentials(CERT_PATH, KEY_PATH, None)
    ssl_domain.set_trusted_ca_db(CA_CERT)
    ssl_domain.set_peer_authentication(SSLDomain.VERIFY_PEER)
    return ssl_domain

if __name__ == "__main__":
    kombit_access = KombitAccess("55133018", r"C:\Users\az68933\Desktop\SF1601\Certificate.pem", test=True)
    kombit_access.get_access_token("http://entityid.kombit.dk/service/bfo_modtag/2")

    # BlockingConnection(url=URL, ssl_domain=CERT_BUNDLE_PATH)

    ssl = create_ssl_domain()
    handler = TLSExternalReceiver(URL, QUEUE, ssl)
    Container(handler).run()
