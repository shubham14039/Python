# Given an array nums of size n, return the majority element.


# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# Constraitns:
# if there is no element -> return false
# if there are conflicts in the number of words -> return the greater word
# The use of other object types  is strictly prohibited

# one way of solving this problem is by iteration
# class Solution():
#     def majority_element(self, nums: list[int]) -> int:
#         n = len(nums)
#         if n == 0:
#             return False
#
#         frequency = {}
#         for elements in nums: 
#             if elements not in frequency.keys():
#                 frequency[elements] = 1
#             else:
#                 frequency[elements] += 1
#
#         target = 0
#         for value in frequency.values():
#             if target < value:
#                 target = value
#         for key, val in frequency.items():
#             if val == target:
#                 return key
# what if the elemments in the list are of equal number



# Now optimise the code to perform in linear time and O(1) space.

#

# another way of solving this problem is by:
#     sort the list and find the element at index n/2
# what if there are more than two repeating integers? Then we will be getting the number that is at the n/2 th position and {maybe} not the actual number


# def majority_element(nums: list[int]) -> int:
#     nums.sort()
#     n = len(nums)//2
#     return nums[n]
#
# list_of_items = [3,3,3,4,4,4,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7]
# print(majority_element(list_of_items))

