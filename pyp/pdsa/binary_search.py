# Implement binary search for a list

def binary(nums: list[int], target: int)-> int:
    if len(nums) == 0:
        return False
    low, high = 0, len(nums)-1
    
    while low <= high:
        mid = (low+high)//2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid-1
    return False

ls = [1,2,3,4,5,6,8,9,12,15,17,19,26,28,46,48,49,53,55,67,69]

print(binary(ls, 1))
print(binary(ls, 5))
print(binary(ls, 9))
print(binary(ls, 0))
print(binary(ls, 67))
print(binary(ls, 69))



