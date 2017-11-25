#!/usr/local/bin/python3

import sys, socket, re, subprocess
from openhab import openHAB


def get_roku():
    ssdpRequest = "M-SEARCH * HTTP/1.1\r\n" + \
                  "HOST: 239.255.255.250:1900\r\n" + \
                  "Man: \"ssdp:discover\"\r\n" + \
                  "MX: 5\r\n" + \
                  "ST: roku:ecp\r\n\r\n";
    socket.setdefaulttimeout(10)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.sendto(bytearray(ssdpRequest, 'utf-8'), ("239.255.255.250", 1900))
    while True:
        try:
            resp = str(sock.recv(1024), 'utf-8')
            # print(resp)
            # print("Matches")
            matchObj = re.match(r'.*USN: uuid:roku:ecp:([\w\d]{12}).*LOCATION: (http://.*)/.*', resp, re.S)
            return [matchObj.group(1), matchObj.group(2)]
        except socket.timeout:
            break


def talk_roku(key):
    base_url = get_roku()[1]
    openhab = openHAB(base_url)

    # fetch all items
    items = openhab.fetch_all_items()
    print(items)


talk_roku('Home')
