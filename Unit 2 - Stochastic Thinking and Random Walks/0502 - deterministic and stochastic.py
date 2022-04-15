# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:13:58 2022

@author: Silviu
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    evens = [10, 12, 14, 16, 18, 20]
    return evens[2]

print( deterministicNumber())


def stochasticNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    evens = [10, 12, 14, 16, 18, 20]
    n = len(evens)
    pos = random.randint(0, n-1)
    return evens[pos]

print( stochasticNumber())