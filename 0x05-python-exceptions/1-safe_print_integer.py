#!/usr/bin/python3
def safe_print_integer(val):
    try:
        print("{:d}".format(val))
        return True
    except BaseException:
        return False

