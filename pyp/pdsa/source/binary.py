

def binary(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    low, high = 0, len(nums)-1
    while low<=high:
        mid = (low+high)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid +1
        else:
            high = mid -1
    return -1

ls = [1, 1, 1, 1, 1]
print(binary(ls, 1))
