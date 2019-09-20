
# Problem Statement

# Peak Finder : One-dimensional Version
# Position 1 is a peak if and only if b ≥ a and b ≥ c. Position 8 is a peak if i > h. Position 1 is a peak if a > b.
# list =  [ a, b, c, d, e, f, g, h, i]
# index ->  0  1  2  3  4  5  6  7  8


# 1. Naive approach
# if leftmost element is > next element, first element is peak
# similarly if rightmost element is > previous element, last element is peak
# otherwise compare element with its neighbours, if its greater than or = neighbours, its peak
def find_peak_naive_method(in_list):
    for index in range(0, len(in_list)):
        if index not in [0, len(in_list)-1]:
            if in_list[index] >= in_list[index-1] and in_list[index] >= in_list[index+1]:
                return index, in_list[index]
        elif index == 0:
            if in_list[index] > in_list[index+1]:
                return index, in_list[index]
        elif index == len(in_list)-1:
            if in_list[index] > in_list[index-1]:
                return index, in_list[index]
        else:
            continue
    return -1,-1


# 2. Sort in ascending/descending order
def find_peak_sorting_method(in_list):
    lst = in_list
    lst.sort()
    return len(lst)-1, lst[(len(lst)-1)]


# 3. Divide and Prune
# rather than comparing each element with its neighbour from left to right, do this
# Step1. Divide - divide the list in half
# Step2. Prune  - if list[mid-1] <= list[mid] => list[mid+1]
#                    return mid
#                 else
#                     if list[mid-1] > list[mid]
#                        prune left half of the list
#                     if list[mid+1] > list[mid]
#                        prune right half of the list
def find_peak_divide_n_prune(in_list):
    if len(in_list) == 0:
        return -1,-1
    elif len(in_list) == 1:
        return in_list[0], 0
    else:
        low  = mid = 0
        hi   = len(in_list)-1
        while (hi - low > 1): # stop when there are 2 elements left
            # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html # prevent overflow
            # https://www.python.org/dev/peps/pep-0238/
            mid = low + (hi - low)//2
            if in_list[mid-1] <= in_list[mid] >= in_list[mid+1]:
                return in_list[mid], mid # mid is peak
            elif in_list[mid-1] > in_list[mid]:
                hi = mid-1   # prune left, move hi to (mid-1)
            elif in_list[mid+1] > in_list[mid]:
                low = mid+1  # prune right, move low to (mid+1)
        # when 2 elements are left, compare them
        if in_list[low] >= in_list[hi]:
            return in_list[low], low
        else:
            return in_list[hi], hi

# 4.
# have a look at solution here:
# https://codereview.stackexchange.com/questions/145224/1d-peak-finder-algorithm

import time
# start from here
if __name__ == "__main__":

    # lists of lists to create less variables
    problemList = [
        [ 2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2], # all peaks , a=b=c
        [ 2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  8], # 2 peaks, a=b=c
        [ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12], # last element is peak, sorted increasing order, i > h
        [12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2], # first element is peak, sorted decreasing order a >b
        [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2], # a < b > c
        [ 4,  5,  6,  8,  8,  8,  6,  5,  4,  3,  2], # a < b = c
        [10, 10,  6,  5,  3,  2,  6,  5,  4,  3,  2], #
        [10,  8], #
        [10, 12], #
        [10], #
        [], #

    ]

    for index in range(len(problemList)):
        print("List : {}".format(problemList[index]))
        peak, ind = find_peak_divide_n_prune(problemList[index])
        print("Peak:{} found at index: {}\n".format(peak,ind))
