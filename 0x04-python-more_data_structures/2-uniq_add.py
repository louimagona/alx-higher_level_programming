#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    uniq = set(my_list)
    for i in uniq:
        total += i
    return(total)
