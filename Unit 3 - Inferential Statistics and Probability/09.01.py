# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:41:00 2022

@author: Silviu
"""

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if (len(fields) != 3) or (not fields[0].isnumeric()):
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

print( loadFile() )