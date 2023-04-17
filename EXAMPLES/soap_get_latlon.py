import sys
import lxml.etree as ET
from zeep import Client # get suds SOAP client
import logging

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# https://graphical.weather.gov/xml/

NWS_URL = 'http://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl' # URL for SOAP service (AKA WSDL)

def main(args):
    client = Client(NWS_URL) # get a client for that site

    logger.debug("client: %s", client)
    logger.debug(dir(client))

    for zip_code in args:
        try:
            lat, lon = get_lat_lon(zip_code, client)
        except ValueError as err:
            logger.warning(err)
        else:
            print(f"{zip_code}: {lat}, {lon}")


def get_lat_lon(zip_list, client):

    response = client.service.LatLonListZipCode(zipCodeList=zip_list)  # call remote function with named parameter

    logger.debug("RESPONSE: %s", response)
    logger.debug(dir(response))
    doc = ET.fromstring(response)
    raw_data = doc.findtext('latLonList')
    raw_lat, raw_lon = raw_data.split(',')
    return float(raw_lat), float(raw_lon)

    return response

if __name__ == '__main__':
    main(sys.argv[1:])
