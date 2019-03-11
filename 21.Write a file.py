# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:48:45 2018

@author: 18096
"""
import requests
from bs4 import BeautifulSoup

r_html = requests.get('http://www.nytimes.com/')
soup = BeautifulSoup(r_html.content, "lxml")
lines = soup.find_all("h2",{"class": "story-heading"})

name_file = input('Where do you want to store the output? Please specify the format as well:')

with open(name_file, 'w') as open_file:
    for line in lines:
        open_file.write(line.text)