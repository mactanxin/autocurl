import time
import os
i=0
while True:
    os.popen('curl -x 201.229.208.2:0080 "http://count28.51yes.com/sa.aspx?id=287573288&refe=&location=http%3A//www.sh678.com/&color=32x&resolution=1280x800&returning=0&language=zh-cn&ua=Mozilla/4.0%20%28compatible%3B%20MSIE%206.0%3B%20Windows%20NT%205.1%3B%20SV1%3B%20.NET%20CLR%202.0.50727%29"').read()
    i=i+1
    print i
    time.sleep(2)
