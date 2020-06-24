import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
# url = 'http://py4e-data.dr-chuck.net/known_by_Danniel.html'
# count = 7
# position = 18

for i in range(count):
	html = urllib.request.urlopen(url,context=ctx).read()
	soup = BeautifulSoup(html,'html.parser')
	tag = soup('a')[position - 1]
	url = tag.get('href',None)
	name = re.findall('_(.+)\.html',url)[0][3:]
	print("Retrieving: ",url)

# return a list of anchor tags

# tags = soup('a') 
# for tag in tags:
# 	print(tag.get('href',None))
# 	sub_name = re.findall('_(.+)\.html',tag.get('href',None))
# 	name = sub_name[0][3:]
# 	print(name)

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# for line in file:
# 	print(line.decode().strip())


# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode(encoding="utf-8")
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     print(type(data.decode()))
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()

# import socket

# mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # pass the host and the port
# mysocket.connect(('data.pr4e.org',80)) 
# # request from the server
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysocket.send(cmd)
# # print(cmd.decode())

# while True:
# 	## 512 of characters
# 	data = mysocket.recv(512)
# 	if len(data) < 1:
# 		break
# 	print(data.decode())
# mysocket.close()