import time
import os
import telnetlib
i=0
while True:
	print os.popen("sh a.sh").read()
	print "telnet"
	tn = telnetlib.Telnet('127.0.0.1','9051')
	tn.write("AUTHENTICATE\r\n")
	print tn.read_until("250 OK\r\n")
	tn.write("signal NEWNYM\r\n")
	print tn.read_until("250 OK\r\n")
	tn.write("quit\r\n")
	i+=1
	print i
	time.sleep(2)