#
# Given a list of intervals, return the longest contiguous interval
#
# Example:
# [(1, 3), (6, 9), (8, 11), (2, 4)] → (6, 11)
#


def longest_chain(arr):
    # sort array by 0th pos tuple value
    s_arr = sorted(arr)

    # assume negative numbers are VALID, set start/end vals to first tuple pair
    start = s_arr[0][0]
    end = s_arr[0][1]

    # loop through sorted list 
    for t in s_arr[1:]:
        if t[0] < end:  # if curr left val < current end val, take curr right val as new end
            end = t[1]
        else:           # else reset start/end vals to current tuple pair
            start = t[0]
            end = t[1]
    return (start, end)


l = [(1, 3), (6, 9), (8, 11), (2, 4)]
# l = [(1, 3), (2, 4)]
resp = longest_chain(l)
print(resp)

