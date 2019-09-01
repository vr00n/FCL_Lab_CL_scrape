## Run in a Jupyter Notebook with all the CL HTML files
from bs4 import BeautifulSoup
import requests
fileList = !ls *.html
cl_place = []
cl_coords = []
cl_title = []

for filename in fileList:
    soup = BeautifulSoup(open(filename), 'html.parser')
    html = list(soup.children)[2]
    head = list(html.children)[1]
    for i in soup.find_all('meta'):
        try:
            column = i['name']
        except KeyError:
            column = i['property']
        if column == "geo.placename":
            cl_place = i['content']
        if column == "geo.position":
            cl_coords = i['content']
        if column == "og:title":
            cl_title = i['content'].strip()
    cl_content = soup.find("section", {"id":"postingbody"}).text
    print "!~!",cl_place,"|",cl_title,"|",cl_coords,"|",cl_content
