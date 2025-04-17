# Selection sort:
#     find the minimum and append it to a new list. And eventually youll end up with a sorted list.
#     But that creates a new list which takes up space, which is not efficient for handling large lists. so we will replace the minimum element with the first element snd continue from the 2nd (index 1) element till the list is sorted.

def selection_sort(nums):
    if not nums:
        return nums
    # Find the minimum element in the list 
    for k in range(len(nums)):
        min = nums[0]
        index = 0
        for i, num in enumerate(nums[:k+1]): # The enumerate() function returns the index first and then value 
            if num < min:
                min = num
                index = i

        nums[0], nums[index] = nums[index], nums[0]
        return nums

# # This function only replaces the minimum element only one times. 
# ls = [9,3,4,5,8,1]
# print(selection_sort(ls))
#
ls = [90,45,3,12,56,78,5,24,46,85]
print(ls)
print(selection_sort(ls))

# def selection_sort(nums):
#     pass
#

