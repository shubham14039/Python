# def insertion_sort(list):
#     for i in range(1,len(list)):
#         current = list[i]
#         j = i
#         while j > 0 and list[j-1] > current:
#             list[j] = list[j-1]
#             j -= 1
#         list[j] = current
#     return list
# # Insertion sort for arrays conataining integers
# list = [9,8,5,7,6,1,2,4,3]
# print(insertion_sort(list))
# Sort a list of jumbled letters in proper alphabetical order


# Below is an example from CT week -6, insertion sort

# def insertion(nums: list[int]) -> list[int]:
#     for i in nums:
#         for j in nums:
#             if j > i:
#                 nums.insert((nums.index(j)-1), i)
#                 nums.remove(i)
#     return nums
#
# ls = [5,78,23,34,90,65,45,1,12,13,11,34,86,43]
# print(insertion(ls))


# Doesnot works as intended
# (Was meant to sort by insertion through the naive way)

# def insertion(nums: list[int]) -> list[int]:
#     sorted_nums = [0]*len(nums)
#     for i in nums:
#         # check and find the correct poosition of the current element 
#         for j in range(len(sorted_nums)-1):
#             if sorted_nums[j] > i:
#                 sorted_nums[j-1] = i
#         nums.remove(i)
#     return sorted_nums
#
# ls = [5,78,23,34,90,65,45,1,12,13,11,34,86,43]
# print(insertion(ls))
