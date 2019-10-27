import feedparser
import wget
import pdb
with open('cl-posts-test.txt','a+') as f:
    d = feedparser.parse('https://denver.craigslist.org/d/community/search/ccc?format=rss')
    for entry in d.entries:
        post_id=entry['link'].split("/")[6].encode('ascii','ignore')
        print type(post_id)
        if post_id in f.read():
            print post_id+" is duplicate"
        else: 
            f.write(post_id+'\n')
            #wget.download(entry['link'])
f.close()

