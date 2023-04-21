"""
Read data from knights.txt into a dictionary of tuples
"""

from pprint import pprint

knight_info = {}  # create empty dict

with open("../DATA/knights.txt", encoding="utf8") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        # create new dict element with name as key and a tuple of the
        # other fields as the value
        knight_info[name] = title, color, quest, comment

pprint(knight_info, sort_dicts=False)
print()

#   str   tuple
for name, info in knight_info.items():
    print(info[0], name)

print()
print(knight_info['Bedevere'][2])
