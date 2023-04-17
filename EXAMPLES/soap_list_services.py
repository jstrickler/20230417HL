import os
import lxml.etree as et
from zeep import Client, Settings

# URLs for SOAP services
COUNTRY_WSDL_URL = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)
NWS_WSDL_URL = 'http://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl'

def main():
    """Main
    """
    demos = (
        countries_list_services, nws_list_services
    )

    for demo in demos:
        demo()
        print("=" * 80)



def countries_list_services():
    client = Client(
        wsdl=COUNTRY_WSDL_URL,
        # service_name="CountryInfoService",
        # port_name="CountryInfoServiceSoap12",
    )
    service_names = _get_service_names(client)
    print(f"service_names: {service_names}")


def nws_list_services():
    client = Client(
        wsdl=NWS_WSDL_URL,
    )
    service_names = _get_service_names(client)
    print(f"service_names: {service_names}")

def _get_service_names(client):
    return [s[0] for s in client.service]

if __name__ == '__main__':
    main()
