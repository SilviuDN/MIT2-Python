# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:25:04 2022

@author: MIT
"""

import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 
    
for i in range(10):
    print(dist1())
    
print('##################################################################')

for i in range(10):
    print(dist2())
    