#! /usr/bin/env python3

from ipaddress import ip_interface, ip_address
import requests
import json
import socket
import sys


URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"


def is_aws_ip(*ips):
    ips = [ip_interface(ip) if "/" in ip else ip_address(ip) for ip in ips]

    aws = requests.get(URL).json()
    awsv4 = {ip_interface(a["ip_prefix"]): a for a in aws["prefixes"]}
    awsv6 = {ip_interface(a["ipv6_prefix"]): a for a in aws["ipv6_prefixes"]}
    aws = {**awsv4, **awsv6}

    result = []
    for ip in ips:
        for k, v in aws.items():
            if ip in k.network:
                result.append(v)

    return result


if __name__ == "__main__":
    ips = [s[4][0] for s in socket.getaddrinfo(sys.argv[1], 0)]
    ret = is_aws_ip(*ips)
    print(json.dumps(ret))
    exit(0 if ret else 1)
