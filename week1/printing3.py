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
intdiv = 22 // 8
print('//\t\tInt division\t22 // 8\t%d\t\tDivide into whole numbers' % intdiv)
div =  22 / 8
print('/\t\tDivision\t22 / 8\t%.2f\t\tDivide (Py2 = // behaviour)' % div)
multi = 3 * 5
print('*\t\tMultiplication\t3 * 5\t%d\t\tTimes' % multi)
subt = 5 - 2
print('-\t\tSubtraction\t5 - 2\t%d\t\tTake away' % subt)
add = 2 + 2
print('+\t\tAddition\t2 + 2\t%d\t\tAdd' % add)
print('\nThe order of operations (also called precedence) of Python math operators is similar to that of mathematics. The ** operator is evaluated first; the *, /, //, and % operators are evaluated next, from left to right; and the + and - operators are evaluated last (also from left to right). You can use parentheses to override the usual precedence if you need to.\n')
print('%s\n%s' %(hyphen, hyphen))
print('Mornin\' boss')
print('Who\'s making t\' brews this mornin\'?')
name = input()
print('Ask %s to make it a strong un please' % name)
print('He\'s a good lad is ' + name)
name_length = len(name)
print('His name length is ' + str(name_length))
