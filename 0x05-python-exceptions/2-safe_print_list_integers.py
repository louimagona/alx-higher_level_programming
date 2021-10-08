#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            try:
                print("{:d}".format(my_list[i]), end='')
            except IndexError as err:
                print(err)
            else:
                count += 1
        else:
            pass
    print()
    return(count)
