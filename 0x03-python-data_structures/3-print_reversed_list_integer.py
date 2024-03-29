#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints a list in reverse order

    Args:
        my_list: List to print in reverse

    Returns:
        None
    """

    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
