#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    for i in range(len(my_list) - 1, -1, -1):
        print(i, my_list[i])
        if new_list.count(new_list[i]) > 1:
            del new_list[i]
    sum = 0
    for i in range(len(new_list)):
        sum += new_list[i]
    return sum
