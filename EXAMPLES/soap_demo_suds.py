import os
import lxml.etree as et
from suds import

# URLs for SOAP services
CALC_WSDL_URL = "http://www.dneonline.com/calculator.asmx?WSDL"
COUNTRY_WSDL_URL = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)
NWS_WSDL_URL = 'http://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl'
NUM_CONV_WSDL_URL = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"


def main():
    """Main
    """
    demos = (calc_demo, calc_list_services,
             countries_demo, countries_demo_raw, countries_list_services,
             nws_demo, nws_list_services,
             num_conv_demo, num_conv_list_services)

    for demo in demos:
        demo()
        print("=" * 80)

def calc_demo():

    client = Client(wsdl=CALC_WSDL_URL,
                       service_name="Calculator",
                       port_name="CalculatorSoap12")
    result = client.service.Add(5, 5)
    print(f"5 + 5: {result}")
    print(f"type(result): {type(result)}")

    result = client.service.Divide(25, 7)
    print(f"25 / 7: {result}")

    result = client.service.Multiply(1234, 1234)
    print(f"125 * 1234: {result}")

def calc_list_services():
    client = Client(
        wsdl=CALC_WSDL_URL,
        service_name="Calculator",
        port_name="CalculatorSoap12"
    )
    service_names = _get_service_names(client)
    print(f"service_names: {service_names}")

def countries_demo():
    client = Client(
        wsdl=COUNTRY_WSDL_URL,
        service_name="CountryInfoService",
        port_name="CountryInfoServiceSoap12",
    )
    response = client.service.ListOfContinentsByName()
    print(response)
    print(f"type(response): {type(response)}")

def countries_demo_raw():
    settings = Settings(raw_response=True)
    client = Client(
        wsdl=COUNTRY_WSDL_URL,
        service_name="CountryInfoService",
        port_name="CountryInfoServiceSoap12",
        settings=settings,
    )
    response = client.service.ListOfContinentsByName()
    print(response.text)
    print(f"type(response): {type(response)}")

def countries_list_services():
    client = Client(
        wsdl=COUNTRY_WSDL_URL,
        service_name="CountryInfoService",
        port_name="CountryInfoServiceSoap12",
    )
    service_names = _get_service_names(client)
    print(f"service_names: {service_names}")



def nws_demo():

    client = Client(
        wsdl=NWS_WSDL_URL,
        service_name="ndfdXML",
        port_name="ndfdXMLPort",
    )
    response = client.service.LatLonListZipCode(zipCodeList="27705 10001 90210")
    print(f"type(response): {type(response)}")
    xml_doc = et.fromstring(response)
    lats_lons = xml_doc.findtext('latLonList')
    print(f"data: {lats_lons}")

def nws_list_services():
    client = Client(
        wsdl=NWS_WSDL_URL,
        service_name="ndfdXML",
        port_name="ndfdXMLPort",
    )
    service_names = _get_service_names(client)
    print(f"service_names: {service_names}")

def num_conv_demo():
    client = Client(
        wsdl=NUM_CONV_WSDL_URL,
        service_name="NumberConversion",
        port_name="NumberConversionSoap12",
    )
    result = client.service.NumberToWords(1234)
    print(f"result: {result}")
    result = client.service.NumberToDollars(47.92)
    print(f"result: {result}")


def num_conv_list_services():
    client = Client(
        wsdl=NUM_CONV_WSDL_URL,
        service_name="NumberConversion",
        port_name="NumberConversionSoap12",
    )
    service_names = _get_service_names(client)
    print(f"service_names: {service_names}")



def _get_service_names(client):
    return [s[0] for s in client.service]

if __name__ == '__main__':
    main()
