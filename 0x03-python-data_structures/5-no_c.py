#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    my_list = list(my_string)
    list_len = len(my_list)
    for i in range(0, list_len):
        if my_list[i] != 'c' and  my_list[i] != 'C':
            new_list.append(my_list[i])
    new_string = ''.join(new_list)
    return(new_string)
