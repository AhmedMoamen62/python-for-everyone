import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    place_id = js['results'][0]['place_id']
    print("Place id",place_id)

# import urllib.request
# import json


# url = 'http://py4e-data.dr-chuck.net/comments_604785.json'

# data = urllib.request.urlopen(url).read().decode()
# print('Retrieving',url)
# print('Retrieving',len(data),'characters')

# js = json.loads(data)

# print('Count:',len(js['comments']))

# sum = 0

# for count in js['comments']:
# 	sum = sum + int(count["count"])
# print("Sum:",sum)

# import urllib.request, urllib.parse, urllib.error
# import twurl
# import json
# import ssl

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# TWITTER_URL = 'http://api.twitter.com/1.1/friends/list.json'

# while True:
# 	acc = input('Enter Twitter Account: ')
# 	if len(acc) < 1 : break
# 	url = twurl.augment(TWITTER_URL,{'screen_name' : acc , 'count' : '5'})

# 	print('Retrieving',url)
# 	connection = urllib.request.urlopen(url,context=ctx)
# 	data = connection.read().decode()
# 	headers = dict(connection.getheaders())
# 	print('Remaining',headers['x-rate-limit-remaining'])
# 	js = json.loads(data)
# 		#the opposite of loads
# 	print(json.dumps(js,indent=4))


# 	for u in js['users']:
# 		print(u['screen_name'])
# 		s = u['status']['text']
# 		print(' ',s[:50])

# # {
# # 	"status" : "OK",
# # 		"results" : [ 
# # 		{
# # 			"geometry" : {
# # 				"location_type" : "APPROXIMATE",
# # 				"location" : {
# # 					"lat" : 42.2808256
# #					"lng" : -83.7430378
# # 				}
# # 			},
# # 			"address_components" : [
# # 				{
# # 					"long_name" : "Ann Arbor",
# # 					"types" : [
# # 						"locality"
# # 						"political"
# # 					],
# #					"short_name" : "Ann Arbor"
# # 				}
# # 			],
# # 			"formatted_address" : "Ann Arbor, MI, USA",
# # 			"types" : [
# # 				"locality"
# # 				"political"
# # 			]
# # 		}
# # 	]
# # }

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# while True:
# 	address = input('Enter location: ')
# 	if len(address) < 1 : break
# 	url = serviceurl + urllib.parse.urlencode({'address':address})

# 	print('Retrieving',url)
# 	uh = urllib.request.urlopen(url)
# 	data = uh.read().decode()
# 	print('Retrieving',len(data),'characters')
# 	try:
# 		js = json.loads(data)
# 	except:
# 		js = None

# 	if not js or 'status' not in js or js['status'] != 'OK':
# 		print('==== Failure To  Retrieve ====')
# 		print(data)
# 		continue

# 	#the opposite of loads
# 	print(json.dumps(js,indent=4))

# 	lat = js["results"][0]["geometry"]["location"]["lat"]
# 	lng = js["results"][0]["geometry"]["location"]["lng"]
# 	print('lat',lat,'lng',lng)
# 	location = js['results'][0]['formatted_address']
# 	print(location)

# data = '''[
#     {
#     "id" : "001",
# 	"x" : "2",
# 	"name" : "Chuck"
# 	},
# 	{
# 	"id" : "009",
# 	"x" : "7",
# 	"name" : "Chuck"
# 	} 
# ]'''

# ## return a list of dictionaries
# info = json.loads(data)
# print("User count:",len(info))
# for item in info:
# 	print("Name",item["name"])
# 	print("Id",item["id"])
# 	print("Attribute",item["x"])

# data = '''{
# 	"name" : "Chuck",
# 	"phone" : {
# 		"type" : "int1",
# 		"number" : "+1 734 303 4456"
# 	},
# 	"email" : {
# 		"hide" : "yes"
# 	}
# }'''

# ## return a dictionary
# info = json.loads(data)
# print("Name:",info["name"])
# print("Hide:",info["email"]["hide"])