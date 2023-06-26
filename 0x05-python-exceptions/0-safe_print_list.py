#!/usr/bin/python3
def safe_print_list(new_list=[], num=0):
    elem_count = 0
    for i in range(num):
        try:
            print("{}".format(new_list[i]), end="")
            elem_count = elem_count + 1
        except IndexError:
            continue
    print("")
    return elem_count

