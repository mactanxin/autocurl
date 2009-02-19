import time
import os
i=0
f = open("/Users/uc0079/Desktop/avlproxy.txt","a")
for r in open("/Users/uc0079/Desktop/proxy.txt"):
    r = r.strip()
    curl = 'curl -x %s -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" -L "http://count28.51yes.com/sa.aspx?id=287573288&refe=&location=http%%3A//www.sh678.com/&color=32x&resolution=1280x800&returning=0&language=zh-cn&ua=Mozilla/4.0%%20%%28compatible%%3B%%20MSIE%%206.0%%3B%%20Windows%%20NT%%205.1%%3B%%20SV1%%3B%%20.NET%%20CLR%%202.0.50727%%29"' % r
    stdin,stdout,stderr=os.popen3(curl)
    err = stderr.read()
    if err.find("curl:")==-1:
        print r
    i+=1
    time.sleep(2)