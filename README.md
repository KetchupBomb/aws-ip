# AWS IP

A simple tool to determine if an IP Address belongs to Amazon.

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
$ ./aws.py 2406:da1c::0
[
	{
		"ipv6_prefix":"2406:da1c::/36",
		"region":"ap-southeast-2",
		"service":"EC2"
	}
]
```

> Note IPv6 support.

Or from the Docker image:

```shell
$ IP=$(dig +short www.amazon.com A | tail -n1)
$ docker run --rm ketchupbomb/aws_ip $IP
[
	{
		"ip_prefix":"13.32.0.0/15",
		"region":"GLOBAL",
		"service":"CLOUDFRONT"
	}
]
```
