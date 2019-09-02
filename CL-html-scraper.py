from bs4 import BeautifulSoup
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
import requests
import csv
import os
import sys
## REPLACE DIRECTORY with PATH
fileList = os.listdir('DIRECTORY')
cl_place = []
cl_coords = []
cl_title = []
cl_url = []
for filename in fileList:
    #print filename
## REPLACE DIRECTORY with PATH
    filename = 'DIRECTORY'+filename
    soup = BeautifulSoup(open(filename), 'html.parser')
    html = list(soup.children)[2]
    head = list(html.children)[1]
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

    print '!~!',cl_oid,'!~~!',cl_place,'!~~!',cl_title,'!~~!',cl_coords,'!~~!',cl_content,'!~~!',cl_community
