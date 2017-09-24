#!/usr/bin/python3

router_name = "Fortigate"
ip_addr = '1.2.3.4'
print('My default gateway is the %s with IP address %s' % (router_name, ip_addr))
print('My default gateway is the {0} with IP address {1}'.format(router_name, ip_addr))
hyphen = '-'*55
print('\nOperator\tOperation\tExample\tEvaluates to...\n%s' % hyphen)
exponent_value = 2 ** 3
print('**\t\tExponent\t2 ** 3\t%d' % exponent_value)
