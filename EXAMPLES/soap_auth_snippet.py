from zeep import Client

# create client
client = Client(...)

# make auth object
auth_ele = client.get_element('ns0:AuthenticationInfo')
auth = auth_ele(userName='me', password='mypwd')

# Pass auth to operation:

client.service.MyOperation(param1, param2, _soapheaders=[auth])
