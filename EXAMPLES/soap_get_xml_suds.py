from suds.client import Client # get suds SOAP client
import lxml.etree as et

CIS_WSDL_URL = (
        "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)

client = Client(CIS_WSDL_URL, retxml=True)  # tell the client to return XML, not sudsobjects

response = client.service.ListOfContinentsByName()

root = et.fromstring(response)

print(et.tostring(root, pretty_print=True).decode())
print()

for continent in root.findall('.//{*}tContinent'):
    name = continent.findtext('{*}sName')
    iso_code = continent.findtext('{*}sCode')
    print(f"{name} ({iso_code})")
