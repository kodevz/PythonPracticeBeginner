# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:52:34 2018

@author: 18096
"""
import random
print([x / y for x in list(random.sample(range(2,20),6)) for y in list(random.sample(range(2,20),8)) if x/y > 5])
