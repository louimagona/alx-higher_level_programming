#!/usr/bin/python3
def multiple_returns(sentence):
    new_list = []
    if not sentence:
        return(None)
    my_list = list(sentence)
    list_len = len(my_list)
    first_letter = my_list[0]
    new_list.append(list_len)
    new_list.append(first_letter)
    tuple1 = tuple(new_list)
    return(tuple1)
