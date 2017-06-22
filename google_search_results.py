import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re


def get_url_google(keyword,pages):

	query = keyword.strip().split()
	query="+".join(query)
	url =  "https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl&start="
	to_crawl = []
	curr = 0
	while curr < pages:
		crawl_url = url + str(curr*10)
		curr = curr + 1
		get_urls(crawl_url,to_crawl)
	
	#printing links scrapped as a list
	print (to_crawl)
	
def get_urls(page,to_crawl):

	req = urllib.request.Request(page, headers={'User-Agent': 'Mozilla/5.0'})
	soup = BeautifulSoup(urlopen(req).read(),"html.parser")
	reg=re.compile(".*&sa=")
	
	#Parsing web urls
	for item in soup.find_all('h3', attrs={'class' : 'r'}): 
    		line = (reg.match(item.a['href'][7:]).group())
    		to_crawl.append(line[:-4])


query=input("Enter the keyword\n")
pages=int(input("Enter the number of pages for which you want the search results\n"))
get_url_google(query,pages)	
	
	
	
	
	
