
# Implement selection sort 
# This function caclculates the sorted list in O(n^2) time complexity (which is horrible)
# clearly this implementation of selection_sort scans through the list a total of n times (where n is the length of the list) and each time the length decreases by 1. 
def selection(nums: list[int]) -> list[int]:
    nums_sorted = []
    while nums:
        minimum = min(nums)
        nums_sorted.append(minimum)
        nums.remove(minimum)
    return nums_sorted

ls = [2,7,9,4,78,34,56,78,89,68,45,3,1,23,34]
print(selection(ls))


# Now this implementation also takes O(n^2) time complexity. Genereally selection sort requires this time complexity because of its deseign nature. And selection sort is useful for cases when there are small number of elements to be sorted. For more efficient time, we would use merge, quick and/or heap sort.
def selection_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        for j in range(i + 1, n):
            # Find the index of the minimum element in the unsorted part
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
