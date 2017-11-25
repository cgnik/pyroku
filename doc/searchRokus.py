#!/usr/bin/python

import sys
import socket
import re

ssdpRequest = b"M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMan: \"ssdp:discover\"\r\nMX: 5\r\nST: roku:ecp\r\n\r\n"; 
socket.setdefaulttimeout(10)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.sendto(ssdpRequest, (b"239.255.255.250", 1900))
while True:
    try:
        resp = sock.recv(1024).decode('utf-8')
        #print(resp)
        #print("Matches")
        matchObj = re.match(r'.*USN: uuid:roku:ecp:([\w\d]{12}).*LOCATION: (http://.*/).*', resp, re.S)
        print (matchObj.group(1) + " " + matchObj.group(2))
    except socket.timeout:
        break
