#!/bin/bash
for file in `find /home/ubuntu/FCL_Lab_CL_scrape/aws/ -name *.html | grep -v "("`
#for file in `ls -lA /home/ubuntu/FCL_Lab_CL_scrape/aws/*.html | awk '{print $9}' | awk -F/ '{print $6'}`
do
        filename=$file
        echo $filename
        python FCL_Lab_CL_scrape/CL-html-scraper.py $filename
        mv $filename /home/ubuntu/processed/
done
