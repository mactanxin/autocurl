import time
import os
import datetime

for r in open("/Users/uc0079/Desktop/proxy.txt"):
    r = r.strip()
    curl = 'curl -x %s -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" -m 10 -r "www.weiphone.com" -L "http://www.weiphone.com/?fromuid=158892"' % r
    stdin,stdout,stderr=os.popen3(curl)
    if stdout.read().find("Weiphone")!=-1:
        print r
    time.sleep(2)