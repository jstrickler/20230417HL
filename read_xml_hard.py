import lxml.etree as et

doc = et.parse('DATA/solar.xml')
print(f"doc: {doc}")

root = doc.getroot()
print(f"root: {root}")
for child in root:
    # print(child.tag)
    if "planets" in child.tag:
        for planet in child:
            print(planet.get('planetname'))
            for moon in planet:
                print(f"    {moon.text}")
print('-' * 60)
doc = et.parse('DATA/solar.xml')
for planet in doc.findall(".//planet"):
    print(planet.get("planetname"))
    for moon in planet.findall("moon"):
        print(f"    {moon.text}")
print('-' * 60)

it = root.getiterator()
for node in it:
    print(node.tag)

