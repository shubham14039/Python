# A sorted array is given, and its likely that it may be rotated by some order. Given a target number, find the index of the target in the array. If the target number does not exist, then return -1. The program should run on O(logn) time
    
# The problem is to be solved through binary search.

# Steps:
#     1. Sort the array
#     2. Use binary search to find the target index 

def binary_search(nums: list[int], target) -> int:
    if len(nums) == 0:
        return -1   
    mid = len(nums)//2
    if target == nums[mid]:
        return mid
    if target > nums[mid]:
        return binary_search(nums[mid+1:], target)
    else:
        return binary_search(nums[:mid], target)

array = [1,2,3,4,5,6,7,8,9]
print(binary_search(array, 0))

