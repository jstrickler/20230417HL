import sys
import lxml.etree as ET
import logging
from suds.sudsobject import asdict
from suds.client import Client # get suds SOAP client
import yaml
from io import StringIO

logging.basicConfig(level=logging.WARNING)

WSDL_URL = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)

# URL for SOAP service (AKA WSDL)

def main(args):
    client = Client(WSDL_URL) # get a client for that site

#    logging.info(f"client: {client}")

    response = client.service.ListOfContinentsByName()  # call remote function with named parameter

    logging.info(f"type(response) {type(response)}")
    response_dict = asdict(response)
    logging.info(f"type(response_dict): {type(response_dict)}")
    logging.info(f"response_dict: {response_dict}")
    logging.info(f"repr(response_dict): {repr(response_dict)}")

    logging.info(f"RESPONSE: {response}")

    for continent in response.tContinent:
        print(continent.sCode, continent.sName)


if __name__ == '__main__':
    main(sys.argv[1:])
