# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:04:26 2022

@author: Silviu
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    
    return 2*random.randint(0,49)

print( genEven() )
print(  random.choice(['apple', 'banana', 'cat']) )

# There are many good answers to this problem, some easier than others :)
def genEven2():
    return random.randrange(0, 100, 2)

def genEven3():
    return random.choice(range(0, 100, 2))

def genEven4():
    return int(random.random() * 50)*2

def genEven5():
    return random.choice(range(0, 50))*2

def genEven6():
    x = random.randint(0, 98)
    while x % 2 != 0:
        x = random.randint(0, 98)
    return x