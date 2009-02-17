import re,urllib

if __name__ == '__main__':
    f = open("/Users/uc0079/Desktop/proxy.txt","w")
    for i in range(30):
        url = 'http://www.samair.ru/proxy/proxy-%s.htm' % str(i).zfill(2)
        html = urllib.urlopen(url).read()
        for p1,p2,p3,p4,port in re.findall(r'(\d+).(\d+).(\d+).(\d+):(\d+)',html,re.M):
            print p1,p2,p3,p4,port
            ip=":".join( [".".join([p1,p2,p3,p4]),port] )
            f.write(ip)
            f.write("\n")
    f.close()