# CL scraping for the FCL
- **Jargon**
	 - [IFFTT - If this then that](https://ifttt.com): An online service that lets you connect internet things with each other. 
	 - CL - Craigslist
	 - FCL - [Friendly Cities Lab](http://www.friendlycitieslab.com)
---

 - [CL-html-scraper.py](https://github.com/vr00n/FCL_Lab_CL_scrape/blob/master/CL-html-scraper.py "CL-html-scraper.py") reads individual HTML posts from a directory and converts it to a tabular format in the following format
	 - cl_oid : Unique ID based on the post's URL
	 - cl_time: The time it was published
	 - cl_category: The category of the post
	 - cl_place: The place name from `geo.placename` tag in the html
	 - cl_title: The title of the post
	 - cl_coords: Lat/Long coordinates from what appears to be the geocoded IP address of the post
	 - cl_content: The body of the post
	 - cl_community: The specific community site of this post

 - `drive-download-20190327T021408Z-001.zip` contains 3 years of missed connections in NYC. It is a limited dataset that contains post-time, post-title, and post-content and was created as a result of me testing an IFFTT integration on craigslist and i forgot to turn it off.

 - `cl-cities` is a directory containing a script that parses individual craigslist sites and outputs missed connection counts for each site.
	 - [cl_mis_count.sh](https://github.com/vr00n/FCL_Lab_CL_scrape/blob/master/cl_mis_count.sh "cl_mis_count.sh") is a bash script that takes `sites.txt` as an input and outputs the number of missed connection entries for each site.
	 - `sites.txt` is a list of craigslist sites.
---

# Cragislist scraping

## IFTTT settings

1. Login to IFFTT
	 - Username:clmissed@mailinator.com
	 - Password: *check slack*
2. View the existing scrapers here: https://ifttt.com/my_applets
3. https://ifttt.com/create to create a new "applet"
	- Click on "This"
	- Search for and choose "**RSS Feed**"
	- Select "**New Feed Item**"
		- Feed URL = https://atlanta.craigslist.org/search/ccc?format=rss
		*(You can replace "atlanta" with any other CL community page)*
		- https://atlanta.craigslist.org/d/for-sale/search/sss shows all "for sale" posts"
		- https://atlanta.craigslist.org/d/housing/search/hhh : housing posts
		- https://atlanta.craigslist.org/d/jobs/search/jjj : jobs posts
		- https://atlanta.craigslist.org/d/services/search/bbb : services posts
		- https://atlanta.craigslist.org/d/gigs/search/ggg : gigs posts
		- https://atlanta.craigslist.org/d/resumes/search/rrr : resumes posts
	- Click on "**That**"
	- Search for and choose "**Google Drive**" (It is currently connected to my personal gdrive". This will need to be changed.
	- Select "**Upload File from URL**"
		- Change the defaults for File URL from {{EntryImageUrl}} to {{EntryUrl}}
		- Change File name to ATL_{{EntryTitle}}. This will name every new feed from atlanta's community posts to ATL_`The Title of the Post`
		- The Drive folder path is currently set to `IFTTT/Feed/CL-MISSED/`
		- Click on Create to "activate the applet"
		- Make sure you disable "Receive notifications when this Applet runs"
	- You are now capturing every new feed from 

## Converting the posts into a CSV

 - Download the CL-MISSED folder from Google Drive to your local computer (using Cyberduck or something similar). This takes some time.
 -  https://github.com/vr00n/FCL_Lab_CL_scrape/blob/master/CL-html-scraper.py is a python script that uses BeautifulSoup to do this. 
 - `python CL-html-scraper.py >> cl-cleaned.csv`  should create a "delimited file"
	 - Before running this script, make sure you change REPLACE WITH DIRECTORY with the full path of the CL-MISSED folder that you just downloaded.
 - Now that you have a delimited file, open it in a text editor:
	 - Mac: Text Wranger ; Windows: Notepad ++
 - Open the delimited file in the text editor and do the following operations
 - Insert a header row  as follows:
	 - `URL|LOCAL TIME|CATEGORY|PLACE|TITLE|CONTENT|COMMUNITY|LATITUDE|LONGITUDE`
	 - Replace all occurences of !~~! with \t
	 - Remove all occurences of !~!

## Next Steps:

Downloading the CL-MISSED folder from Google Drive is proving to be a bottleneck. We need to figure out a way to either:

- Write a python script (using feedparse package) to directly capture the RSS feed automatically into some consolidated data store. (Question: What does GATech use as its cloud ?)
OR
- Get the existing python script to read directly from Google Drive without having to download the CL-MISSED folder
