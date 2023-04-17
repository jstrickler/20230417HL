from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
import lxml.etree as et

COUNTRY_WSDL_URL = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)

history = HistoryPlugin()

client = Client(
    wsdl=COUNTRY_WSDL_URL,
    service_name="CountryInfoService",
    port_name="CountryInfoServiceSoap12",
    plugins=[history],
)
response = client.service.ListOfContinentsByName()

raw_xml_sent = history.last_sent["envelope"]
pretty_xml_sent = et.tostring(raw_xml_sent, pretty_print=True).decode()
print(pretty_xml_sent)
print('-' * 60)
raw_xml_received = history.last_received["envelope"]
pretty_xml_received = et.tostring(raw_xml_received, pretty_print=True).decode()
print(pretty_xml_received)
