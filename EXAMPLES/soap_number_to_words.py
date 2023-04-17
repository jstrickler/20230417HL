from suds.client import Client

URL = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl"

client = Client(URL)

print(f"client: {client}")

response = client.service.NumberToWords(1234)
print(f"response: {response}")
