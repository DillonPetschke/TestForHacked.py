# TestForHacked.py
This program takes an IP subnet, tests for :80 or 443,  if found, checks for the string "hacked" and prints the IP address if found. 

To use, Input your IP space in line 19 in format '192.168.1.0/24'
  
To switch to 443 instead of 80, comment out line 27 using "#" and uncomment line 28 by removing the "#"

NOTE: An error will occur if both line 27 and 28 are uncommented. 
