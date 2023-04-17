import sys
import lxml.etree as ET
from suds.client import Client # get suds SOAP client
from datetime import datetime, timedelta
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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

    xml_doc = ET.fromstring(response) # parse XML response into ElementTree object
    logger.debug("xml_doc: %s", xml_doc)
    lat_lon_list = xml_doc.findtext('latLonList') # find latLonList tag in XML
    if len(lat_lon_list) > 1:
        lat_str, lon_str = lat_lon_list.split(',')
        return float(lat_str), float(lon_str)
    else:
        raise ValueError(f"Unable to get latitude and longitude for zip code {zip_list}")

if __name__ == '__main__':
    main(sys.argv[1:])
