#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    newlist = my_list[:]
    if idx < 0:
        return(newlist)
    elif idx >= list_len:
        return(newlist)
    else:
        newlist[idx] = element
        return(newlist)
