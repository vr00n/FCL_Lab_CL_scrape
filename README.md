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
