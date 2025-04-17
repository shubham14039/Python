# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

    for i in range(n):
        index = nums1.index(0)
        nums1[index] = nums2[i]
    nums1.sort()
    # # return nums1
    # It does not matters if we return anything or not. Because .sirt() function modifies list in place. So even if we return anything, it will return the reference of the result itself. Which is redundant.
    #     If we do not return anything, the changes made to nums1 will be reflected outside the method itself, because nums1 will be passed by refrence. (mutable objects in python are passed by reference)

    

ls1 = [9,5,7,0,0,0]
ls2 = [4,8,6]

print(merge(ls1, 3, ls2,3))
# for i in ls2:
#     index = ls1.index(0)
#     ls1[index] = i
#
# ls1.sort()
# print(ls1)
