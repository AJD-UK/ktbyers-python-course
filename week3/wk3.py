#!/usr/bin/python

import sys

ip = sys.argv[1]

octets = ip.split('.')
print 'first_octet\tsecond_octet\tthird_octet\tfourth_octet'
print '-'*70
print bin(int(octets[0])),'\t', bin(int(octets[1])),'\t', bin(int(octets[2])),'\t', bin(int(octets[3]))

