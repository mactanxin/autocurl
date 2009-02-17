#!/usr/local/bin/python
import re,urllib

'''
e.g
./autocurl.py > proxy-list.txt
'''

if __name__ == '__main__':
    for i in range(30):
        url = 'http://www.samair.ru/proxy/proxy-%s.htm' % str(i).zfill(2)
        html = urllib.urlopen(url).read()
        for p1,p2,p3,p4,port in re.findall(r'(\d+).(\d+).(\d+).(\d+):(\d+)',html,re.M):
            print ":".join( [".".join([p1,p2,p3,p4]),port] )
