#!/bin/sh

#e.g post.sh -F username=qingfeng http://xxx.com

curl -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" \
   -x 127.0.0.1:8118 -L \
   $1 $2
