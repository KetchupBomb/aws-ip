# AWS IP

A simple tool to determine if an IP Address or Domain belongs to Amazon.

I built this as part of a blog post and is just a toy project.

## tl;dr

Use it as a library:

```python
>>> import aws
>>> aws.is_aws_ip("1.2.3.4")
[]
```

Or use it as a CLI:

```shell
$ python3 aws.py 2406:da1c::0
[{"ipv6_prefix": "2406:da1c::/36", "region": "ap-southeast-2", "service": "EC2", "network_border_group": "ap-southeast-2"}]
```

> Note IPv6 support.

Or from the Docker image:

```shell
$ docker run --rm ketchupbomb/aws-ip amazon.com | jq
[
  {
    "ip_prefix": "205.251.240.0/22",
    "region": "us-east-1",
    "service": "AMAZON",
    "network_border_group": "us-east-1"
  },
  {
    "ip_prefix": "54.239.16.0/20",
    "region": "us-east-1",
    "service": "AMAZON",
    "network_border_group": "us-east-1"
  },
  {
    "ip_prefix": "176.32.96.0/21",
    "region": "us-east-1",
    "service": "AMAZON",
    "network_border_group": "us-east-1"
  }
]
```
