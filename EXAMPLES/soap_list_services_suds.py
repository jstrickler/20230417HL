import logging
from suds.client import Client

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

NWS_URL = 'http://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl' # URL for SOAP service (AKA WSDL)

client = Client(NWS_URL) # get a client for that site

for method in client.wsdl.services[0].ports[0].methods: # iterate over courses
    print(method)

logger.debug(client.wsdl)
