import feedparser
import wget
import pdb
import sys
import time
import os

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
						wget.download(entry['link'])

