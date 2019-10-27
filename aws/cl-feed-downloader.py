import feedparser
import wget
import sys
import time
import os
count=0
while True:
    count=count+1
    print "Feeds Iteration #",count
    with open('cl-feeds.txt','r') as feed_file:
        for feed in feed_file.readlines():
            d = feedparser.parse(feed)
            for entry in d.entries:
                post_cat=feed.split("/")[-1].split("?")[0]
                post_community=entry['link'].split("/")[2].split(".")[0].encode('ascii','ignore')
                post_id=entry['link'].split("/")[-1].encode('ascii','ignore')
                with open('cl-posts.txt','r') as f_r:
                    if post_id in f_r.read():
                        continue
                    else: 
                        print post_community+"-"+post_cat+"-"+post_id+" is new"
                        with open('cl-posts.txt','a+',os.O_NONBLOCK) as f_w:
                            f_w.write(post_community+"-"+post_cat+"-"+post_id+'\n')
                            f_w.close()
                            try:
                                wget.download(entry['link'],bar=None)
                            except IOError as e:
                                print "Got IO error, sleeping for 5 seconds"
                                time.sleep(5)
                                wget.download(entry['link'],bar=None)
        time.sleep(60)
