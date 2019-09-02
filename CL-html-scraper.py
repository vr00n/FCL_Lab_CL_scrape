from bs4 import BeautifulSoup
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
import requests
import csv
import os
import sys
fileList = os.listdir('REPLACE WITH DIRECTORY')
cl_place = []
cl_coords = []
cl_title = []
cl_url = []
for filename in fileList:
    #print filename
    filename = 'REPLACE WITH DIRECTORY'+filename
    soup = BeautifulSoup(open(filename), 'html.parser')
    html = list(soup.children)[2]
    head = list(html.children)[1]
    cl_category = soup.find('li', {"class":'crumb category'}).text.strip("\n")
    cl_time = soup.find('time', {"class":'date timeago'}).text.strip("\n").strip(" ").strip("\n")
    for i in soup.find_all('meta'):
        try:
            column = i['name']
        except KeyError:
            column = i['property']
        if column == 'geo.placename':
            cl_place = i['content']
        if column == 'geo.position':
            cl_coords = i['content']
        if column == 'og:title':
            cl_title = i['content'].strip()
        if column == 'og:url':
            cl_url = i['content'] 
            cl_community = cl_url.split("/")[2]
            cl_oid = cl_url.split("/")[-1]
    cl_content = soup.find('section', {"id":'postingbody'}).text
    cl_content = cl_content.replace("\n"," ")

    print '!~!',cl_oid,'!~~!',cl_time,'!~~!',cl_category,'!~~!',cl_place,'!~~!',cl_title,'!~~!',cl_coords,'!~~!',cl_content,'!~~!',cl_community
