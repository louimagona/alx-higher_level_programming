#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = str[:]
    new = str_copy[:n] + str_copy[n+1:]
    return(new)
