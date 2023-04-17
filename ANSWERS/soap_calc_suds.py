from suds.client import Client

CALC_URL = "http://www.dneonline.com/calculator.asmx?wsdl"

client = Client(CALC_URL)

# to see methods
for method in client.wsdl.services[0].ports[0].methods: # <3>
    print(method)

result1 = client.service.Add(13, 5)
print("13 + 5 =", result1)

result2 = client.service.Subtract(13, 5)
print("13 - 5 =", result2)

result3 = client.service.Multiply(13, 5)
print("13 * 5 =", result3)

result4 = client.service.Divide(13, 5)
print("13 / 5 =", result4)
