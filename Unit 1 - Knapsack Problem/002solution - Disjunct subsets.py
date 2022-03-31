# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:45:24 2022

@author: User
"""


# in solutiile anterioare am luat toate numerele in baza 2 de n cifre
# 0/1 --> contine, nu contine elementul
# acum iau toate numerele in baza 3 de n cifre
# 0/1/2 --> elementul lipseste / e in subm 1 / e in subm 2
# cu baza 2 puteam lucra implicit, cu baza 3 nu ==> impart la puteri ale lui 3 in loc sa translatez la dreapta cu j "biti"
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        
items = [0,1,2]

generator3 = yieldAllCombos(items)