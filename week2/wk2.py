#!/usr/bin/python

print 'Input an IP network ' 
ip = raw_input()
octets = ip.split('.')
print 'first_octet\tsecond_octet\tthird_octet\tfourth_octet'
print '-'*70
print bin(int(octets[0])),'\t', bin(int(octets[1])),'\t', bin(int(octets[2])),'\t', bin(int(octets[3]))

entry1 = "* 1.0.192.0/18 157.130.10.233 0 701 38040 9737 i"
entry2 = "* 1.1.1.0/24 157.130.10.233 0 701 1299 15169 i"
entry3 = "* 1.1.42.0/24 157.130.10.233 0 701 9505 17408 2.1465 i"
entry4 = "* 1.0.192.0/19 157.130.10.233 0 701 6762 6762 6762 6762 38040 9737 i"

bgp1 = entry1.split(' ')
bgp2 = entry2.split(' ')
bgp3 = entry3.split(' ')
bgp4 = entry4.split(' ')

ipp1 = bgp1[1]
ipp2 = bgp2[1]
ipp3 = bgp3[1]
ipp4 = bgp4[1]

as1 = bgp1[4:-1]
as2 = bgp2[4:-1]
as3 = bgp3[4:-1]
as4 = bgp4[4:-1]

print '\n\nip_prefix\tas_path'
print ipp1, '\t', as1
print ipp2, '\t', as2
print ipp3, '\t', as3
print ipp4, '\t', as4

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

ios_version = cisco_ios.split(', ')
print ios_version[2].strip('Version ')
