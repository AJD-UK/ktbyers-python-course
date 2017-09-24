#!/usr/bin/python3

router_name = "Fortigate"
ip_addr = '1.2.3.4'
print('My default gateway is the %s with IP address %s' % (router_name, ip_addr))
print('My default gateway is the {0} with IP address {1}'.format(router_name, ip_addr))
hyphen = '-'*85
print('\nOperator\tOperation\tExample\tEvaluates\tExplanation\n%s' % hyphen)
exponent_value = 2 ** 3
print('**\t\tExponent\t2 ** 3\t%d\t\tTo the power of' % exponent_value)
modulus = 22 % 3
print('%%\t\tModulus\t\t22 %% 3\t%d\t\tRemainder (3 * 7 = 21)' % modulus)
