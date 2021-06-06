# Scam the scammer by feeding fake user data to their server
# Based on code by Engineer Man https://github.com/engineer-man/youtube https://www.youtube.com/channel/UCrUL8K81R4VBzm-KOYwrcxQ
# List of popular domains by https://github.com/mailcheck/mailcheck/wiki
# Modification: random domains from list are chosen for users

import requests
import os
import random
import string
import json
counter = 0
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

names = json.loads(open('names.json').read())
domains = json.loads(open('domains.json').read())

# Replace with ur url
url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

for name in names:
	name_extra = ''.join(random.choice(string.digits))
	username = name.lower() + name_extra + '@' + random.choice(domains)
	password = ''.join(random.choice(chars) for i in range(10))
	counter += 1
#	Replace request parameters with those out of ur url
#	U can use chrome built-in network tab to record ur request
#	requests.post(url, allow_redirects=False, data={
#		'auid2yjauysd2uasdasdasd': username,
#		'kjauysd6sAJSDhyui2yasd': password
#	})
	
	print ('sending username ' +username+ ' and password: ' +password)

print("Fake users sent: ", counter)