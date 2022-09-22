from lxml.html import parse
from lxml.etree import tostring
from lxml import etree as et

import urllib.request

#cambio de user agent
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

#descarga y parseo de la pagina.
response = urllib.request.urlopen('https://buenosaires.craigslist.org/')
doc = parse(response)

elems = doc.xpath("//h1/*")


for item in elems:
    print(tostring(item))


root = et.Element('html', version="5.0")
et.SubElement(root, 'head')
et.SubElement(root, 'title', bgcolor="red", fontsize='22')
et.SubElement(root, 'body', fontsize="15")

# Use pretty_print=True to indent the HTML output
print (et.tostring(root, pretty_print=True).decode("utf-8"))

print(root.tag)
for e in root:
    print(e.tag)

root.set('newAttribute', 'attributeValue') 

# Print root again to see if the new attribute has been added
print(et.tostring(root, pretty_print=True).decode("utf-8"))

print(root.get('newAttribute'))
print(root[1].get('alpha')) # root[1] accesses the `title` element
print(root[1].get('bgcolor'))

print(root[2].get("fontsize"))

# Copying the code from the very first example
root = et.Element('html', version="5.0")
et.SubElement(root, 'head')
et.SubElement(root, 'title', bgcolor="red", fontsize="22")
et.SubElement(root, 'body', fontsize="15")

# Add text to the Elements and SubElements
root.text = "This is an HTML file"
root[0].text = "This is the head of that file"
root[1].text = "This is the title of that file"
root[2].text = "This is the body of that file and would contain paragraphs etc"

print(et.tostring(root, pretty_print=True).decode("utf-8"))

# Check if an element has children
if len(root) > 0:
    print("True")
else:
    print("False")

# Check the same things for the root's child nodes.
for i in range(len(root)):
    if (len(root[i]) > 0):
        print("True")
    else:
        print("False")

for i in range(len(root)):
    print(et.iselement(root[i]))

# Check if an element has a parent
for i in range(len(root)):
    print(et.iselement(root[i]))

# Retrieving elements strings
# root[1] is the `title` tag
print(root[1].getnext()) # The tag after the `title` tag
print(root[1].getprevious()) # The tag before the `title` tag


root = et.XML('<html version="5.0">This is an HTML file<head>This is the head of that file</head><title bgcolor="red" fontsize="22">This is the title of that file</title><body fontsize="15">This is the body of that file and would contain paragraphs etc</body></html>')
root[1].text = "The title text has changed!"
print(et.tostring(root, xml_declaration=True).decode('utf-8'))

print(type(root))

print(root.find('a')) # No <a> tags exist, so this will be `None`
print(root.find('head').tag)
print(root.findtext('title')) # Directly retrieve the the title tag's text