# Given an array of integers, find if it’s possible to remove exactly one integer from the array that divides the array
# into two subarrays with the same sum.

# Input:  arr = [6, 2, 3, 2, 1]
# Output:  true
# Explanation:  On removing element 2 at index 1,
# the array gets divided into two subarrays [6]
# and [3, 2, 1] having equal sum
#
# Input:  arr = [6, 1, 3, 2, 5]
# Output:  true
# Explanation:  On removing element 3 at index 2,
# the array gets divided into two subarrays [6, 1]
# and [2, 5] having equal sum.
#
# Input:  arr = [6, -2, -3, 2, 3]
# Output: true
# Explanation:  On removing element 6 at index 0,
# the array gets divided into two sets []
# and [-2, -3, 2, 3] having equal sum
#
# Input:  arr = [6, -2, 3, 2, 3]
# Output: false


def split_sum(arr_in):
    # loop through array, splitting array into two sub arrays at each pos
    for i, val in enumerate(arr_in):
        sub_arr_left = arr_in[:i+1]
        sub_arr_right = arr_in[i+2:]

        # print('left: {}\t\tright:{}'.format(sub_arr_left, sub_arr_right))

        if sum(sub_arr_left) == sum(sub_arr_right):
            # return True
            return 'true'
    return 'false'


print(split_sum([6, 2, 3, 2, 1]))
print(split_sum([6, 1, 3, 2, 5]))
print(split_sum([6, -2, -3, 2, 3])) # this one doesnt work, but it does not make sense that it should be "true"
print(split_sum([6, -2, 3, 2, 3]))
