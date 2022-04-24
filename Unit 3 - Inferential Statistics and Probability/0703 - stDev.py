# -*- coding: utf-8 -*-
"""
Created on Sat May 14 09:38:02 2022

@author: User
"""

def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    total = 0
    mean = 0
    squareSum = 0
    if len(L) == 0:
        return float('NaN')
    else:
        newlist = []
        for i in L:
            newlist.append(len(i))
            total += len(i)
        mean = float(total/len(L))
        for j in newlist:
            squareSum += float((j-mean)**2)
    return float((squareSum/len(L)))**0.5

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print ( stdDevOfLengths(L) )