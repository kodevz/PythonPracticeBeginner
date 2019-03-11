# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:12:32 2018

@author: Karthi UK
"""

import requests
from bs4 import BeautifulSoup

def getContent(soup):
	heading = soup.find("div", {"class":"dek"})
	if heading:
		yield heading.text
	
	for p in soup.find_all("p", {"class":""}):
		yield p.text

def readWebPageContent(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    for s in getContent(soup):
        print("\n%s" % s.encode("utf-8"))
        input("\nPress enter to continue  ")
        print("End of article")
    
    

if __name__ == "__main__":
    readWebPageContent("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
    