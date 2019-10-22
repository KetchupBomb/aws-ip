#! /usr/bin/env python3

from ipaddress import ip_interface, ip_address
import json
import requests
import sys


URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"


def is_aws_ip(ip):
    aws = requests.get(URL).json()
    awsv4 = {ip_interface(a["ip_prefix"]): a for a in aws["prefixes"]}
    awsv6 = {ip_interface(a["ipv6_prefix"]): a for a in aws["ipv6_prefixes"]}
    aws = {**awsv4, **awsv6}

    if "/" in ip:
        ip = ip_interface(ip)
    else:
        ip = ip_address(ip)

    return [v for k, v in aws.items() if ip in k.network]


if __name__ == "__main__":
    ret = is_aws_ip(sys.argv[1])
    print(json.dumps(ret, indent=2))
    exit(0 if ret else 1)
