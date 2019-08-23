#!/bin/bash
for i in $(cat sites.txt)
do
num=`curl -s "$i" | grep "totalcount" | awk -F\> '{print $2}' | awk -F\< '{print $1}' | head -1`
echo $i,$num
done
