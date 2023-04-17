import sys
import logging
from zeep import Client
import yaml

logger = logging.getLogger()
logger.propagate = False
logger.setLevel(logging.WARNING)

# URL for SOAP service (AKA WSDL)
WSDL_URL = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)

def main(args):
    client = Client(WSDL_URL) # get a client for that site

    logging.debug(f"client: {client}")

    response = client.service.ListOfContinentsByName()  # call remote function with named parameter

    for continent_data in response:
        print(continent_data['sCode'], continent_data['sName'])

    

if __name__ == '__main__':
    main(sys.argv[1:])
