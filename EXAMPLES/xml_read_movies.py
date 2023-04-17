
# import xml.etree.ElementTree as ET
import lxml.etree as ET

movies_doc = ET.parse('movies.xml')  # read and parse the XML file

movies = movies_doc.getroot()  # get the root element (<movies>)

for movie in movies:  # loop through children of root element
    print('{} by {}'.format(
        movie.get('name'),  # get 'name' attribute of movie element
        movie.findtext('director'),  # get 'director' attribute of movie element
    )
    )
