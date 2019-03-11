# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:28:45 2018

@author: 18096
"""

import requests
from bs4 import BeautifulSoup

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")
title = soup.findAll(class_="lh-condensed")
print(title)