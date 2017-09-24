#!/usr/bin/python

ipv6 = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'
ipv6_split = ipv6.split(':')
print ipv6_split
ipv6_join = ':'.join(ipv6_split)
print "This is an IPv6 address %s" % ipv6_join
