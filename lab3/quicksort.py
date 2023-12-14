# Author  : Grace Amer Bech
# Date    : 26 th February
# Purpose : Lab 3


def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p

    pivot = the_list[r]  # set pivot to be the element at index r

    while j < r: # if j is less than r, compare, then increment r and swap the positions of i and j
        if compare_func(the_list[j], pivot):
            i = i + 1

            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp
            j = j + 1

        else:
            j = j + 1

    temp = the_list[r]
    the_list[r] = the_list[i + 1]
    the_list[i + 1] = temp

    return i + 1

def quick_sort(the_list, compare_func, p = None, r = None):
    if p == None and r== None:
        p = 0
        r = len(the_list) - 1
    if p < r: # while p is less than r, call partition on it, and sort the lists
        q = partition(the_list, p, r, compare_func)
        quick_sort(the_list, compare_func, p, q - 1)
        quick_sort(the_list, compare_func, q + 1, r)









