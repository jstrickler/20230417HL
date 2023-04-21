
import requests

URL = 'http://www.python.org'

response = requests.get(
    URL, 
    headers={'content-type': 'text/html'},
)  # HTTP response

if response.status_code == requests.codes.OK:  # 200

    for header, value in sorted(response.headers.items()): # response.headers is a dictionary of the headers
        print("{:20.20s} {}".format(header, value))
    print()

    print(response.text[:200])   # The content is returned as a bytes object, so it needs to be decoded to a string; print the first 200 bytes
    print('...')
    print(response.text[-200:])   # print the last 200 bytes
