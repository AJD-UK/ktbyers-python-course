import pexpect

for i in range(1,255):
    ping = pexpect.spawn('ping -c 1 192.168.0.%s' %i)
    result = ping.expect([pexpect.EOF,pexpect.TIMEOUT])
    print(ping.before)
