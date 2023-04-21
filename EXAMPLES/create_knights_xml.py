import lxml.etree as et



root = et.Element("knights")
with open('../DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight = et.SubElement(root, "knight", title=title)
        knight_name = et.SubElement(knight, "name")
        knight_name.text = name
        et.SubElement(knight, 'color').text = color
        et.SubElement(knight, 'quest').text = quest
        et.SubElement(knight, 'comment').text = comment

xml_string = et.tostring(root,xml_declaration=True)
print(xml_string.decode())

doc = et.ElementTree(root)
print(f"doc: {doc}")
doc.write('knights.xml', pretty_print=True, xml_declaration=True)

with open('knights.xml') as knights_in:
    doc = et.parse(knights_in)
    print(doc)
