#!/usr/bin/env python3
#1
fqdnIP = {"server1.testlab.com":"192.168.1.10","server2.testlab.com":"192.168.1.11",
	  "server3.testlab.com":"192.168.1.12","server4.testlab.com":"192.168.1.13",
	  "server5.testlab.com":"192.168.1.14","server6.testlab.com":"192.168.1.15"}
#2
print("FQDN's: ", fqdnIP.keys())
#3
print("IP's: ", fqdnIP.values())
#4
print("Full: ", fqdnIP)
#5
fqdnIP["server7.testlab.com"] = "192.168.1.16"
fqdnIP["server8.testlab.com"] = "192.168.1.17"
#6
key_to_lookup = "server2.testlab.com"
if key_to_lookup in fqdnIP:
	print("Key exists!")
else:
	print("Key does not exist!")
#7
lookup = "server10.testlab.com"
if lookup in fqdnIP:
	print("Key exists!")
else:
	print("Key does not exist!")
