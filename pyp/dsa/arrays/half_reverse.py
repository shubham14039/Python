# Given an array of even length, reverse the first and second halves of the array

# first we have to reverse a full array

import array as arr

aray = arr.array('i', [1,2,3,4,5,6,7,8,9])

# First method is to cycle through the whole list once (or len(list) times each element)
def cycle_reverse():
    pass

# Second method is through copying the trailing elements to a new list
# def reverse(a):
#     new_list = []
#     for i in range(len(a)):
#         new_list.append(a[-1])
#         a.pop()
#     return new_list
#
# print(reverse(aray))

# Reverse without copying (or making) a new list:
def reverse_without_copy(list):
    n = len(list)
    for i in range(n//2):
        list[i], list[n -i-1] = list[n-i-1], list[i]
    return list
print(reverse_without_copy(aray))
#Now we have to reverse half of the list
