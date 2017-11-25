#!/usr/local/bin/python3

import socket, re, requests


def get_roku_ids():
    ssdpRequest = "M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMan: \"ssdp:discover\"\r\nMX: 5\r\nST: roku:ecp\r\n\r\n"
    socket.setdefaulttimeout(5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.sendto(bytearray(ssdpRequest, 'utf-8'), ("239.255.255.250", 1900))
    roku_list = {}
    while True:
        try:
            resp = str(sock.recv(1024), 'utf-8')
            matches = re.match(r'.*USN: uuid:roku:ecp:([\w\d]{12}).*LOCATION: (http://.*)/.*', resp, re.S)
            roku_list[matches.group(1)] = matches.group(2)
        except socket.timeout:
            break
    return roku_list


def roku_key(roku_id, key):
    return requests.post('http://{}/keypress/{}'.format(roku_id, key), data={})


# roku_key('192.168.1.103:8060', 'Home')
# print("{}".format(get_roku_ids()))
