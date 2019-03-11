# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:24:26 2018

@author: Karthi UK
"""
import random

a = list(random.sample(range(50),10))
print(a)
print([x for x in a if a.index(x) == 0 or a.index(x) == len(a) - 1])
