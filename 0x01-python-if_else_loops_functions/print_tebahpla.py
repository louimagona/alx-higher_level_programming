#!/usr/bin/python3
for i in reversed(range(65, 91)):
    print("{:c}".format(i if (i % 2 != 0) else (i + 32)), end='')
