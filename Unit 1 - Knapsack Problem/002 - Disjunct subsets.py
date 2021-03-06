# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:15:35 2022

@author: User
"""


# yield all subsets
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
items = [0,1,2]


generator = powerSet(items)


# =============================================================================
# for k in range(16):
#     generator.__next__()
# =============================================================================


#yield all pairs of disjunctive subsets
def yieldAllCombos(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        #print( '************************************' )
        #print(combo)
        for m in range( len(combo) + 1 ):
            tempTuple = (combo[:m], combo[m:] )
            yield tempTuple 
            #print(tempTuple )
                
generator2 = yieldAllCombos(items)

