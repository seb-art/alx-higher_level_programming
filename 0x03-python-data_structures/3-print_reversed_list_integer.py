#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for m in my_list.revese():
        print("{:d}".format(m))
