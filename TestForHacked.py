#!/usr/bin/env python
#
# This program takes a IP subnet, tests for :80, 
# if found, checks for the string "hacked"
# and prints the IP address if found. 
#
# Author: Dillon Petschke
#
# Date: 3-31-2020
#
# Run as python3 ./TestForHacked.py
# 

import sys
import requests
import ipaddress
from bs4 import BeautifulSoup

CompanyName = list(ipaddress.ip_network('x.x.x.x/16').hosts()) 
# Change x.x.x.x/16 to your IP space ie. 192.168.1.0/24

try:
 
	for addr in CompanyName:
		try :
			new = str(addr)
			url = str('http://' + new + ':80')
			#url = str('https://' + new + ':443')  Uncomment this line to check 443 instead. 
			#				      Note: cannot check 80 and 443 at the same time.
			request = requests.get(url, timeout=.1)
			if request.status_code == 200:
				result = (request.text.find('hacked'))
				if result == -1:		
					print(url)
		except Exception as e:
			pass
				
except Exception as e:
        print ('Error: %s' % e)
        sys.exit(1)		

print ("Done!")

