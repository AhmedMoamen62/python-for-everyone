import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import xml.etree.ElementTree as ET

# url = input('Enter location: ')
url = 'http://py4e-data.dr-chuck.net/comments_604784.xml'
xml = urllib.request.urlopen(url)
xmltree = ET.fromstring(xml.read())
print('Retrieving ',url)
counts = xmltree.findall('.//count')
print('Count: ',len(counts))
sum = 0
for count in counts:
	sum = sum + int(count.text)
print(sum)

## library for conveting xml to tree

# import xml.etree.ElementTree as ET
# data = '''<stuff>
# 	<users>
# 		<user x="2">
# 			<id>001</id>
# 			<name>Chuck</name>
# 		</user>
# 		<user x="7">
# 			<id>009</id>
# 			<name>Brent</name>
# 		</user>
# 	</users>
# </stuff>'''

# stuff = ET.fromstring(data)
# lst = stuff.findall('users/user')
# print('User count:',len(lst))
# for item in lst:
# 	print('Name:',item.find('name').text)
# 	print('Id:',item.find('id').text)
# 	print('Attribute',item.get("x"))


# import xml.etree.ElementTree as ET
# data = '''<person>
#  <name>Chuck</name>
#  <phone type="int1">
#    +1 734 303 4456
#    </phone>
#    <email hide="yes"/>
#  </person>'''

# tree = ET.fromstring(data)
# print('Name:',tree.find('name').text)
# print('Attr:',tree.find('phone').get('type'))
