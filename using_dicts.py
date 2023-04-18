from collections import defaultdict

d1 = dict()   # empty dict
d2 = {'foo': 35, 'bar': 18, 'blah': -3}  # literal dict
d3 = {}  # empty dict
d4 = dict(foo=35, bar=18, blah=-3)  # initialize with arguments

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'DXB': 'Dubai',
    'LTN': 'London',  # (Luton)
    'LGW': 'London',  # (Gatwick)
    'LHR': 'London',  # (Heathrow)
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(f"airports['DXB']: {airports['DXB']}")
airports['LGB'] = "Long Beach"
# print(f"airports['BUR']: {airports['BUR']}")
print(f"airports.get('BUR'): {airports.get('BUR')}")
print(f"airports.get('BUR', 'NOT FOUND'): {airports.get('BUR', 'NOT FOUND')}")

airport = airports.setdefault('ONT', 'Ontario')
print(f"airports: {airports}")

data = {'ALB': 'Albany', 'PIT': 'Pittsburgh', 'LGB': "Longer Beach"}
# airports.update(data)  
airports |= data  # same as .update()
print(f"airports: {airports}")

def get_zero():
    # some_function()...
    return 0

dzero = defaultdict(get_zero)

dzero['a'] = 5
dzero['r'] = 22
print(f"dzero['a']: {dzero['a']}")
print(f"dzero['m']: {dzero['m']}")
print(f"dzero: {dzero}")
print('-' * 60)

for code, city in airports.items():
    print(code, city)
print()

for code, city in sorted(airports.items()):
    print(code, city)
print()

def by_value(element):
    return element[1], element[0]  # return value, key

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print()





