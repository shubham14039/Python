# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

ls = [1,3,7,8,4,9,3,2,9,7,8,2,5,6,1,5,4]


# While this is a good approach:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_nums = []
        for i in nums:
            if i not in new_nums:
                new_nums.append(i)
            else:
                new_nums.remove(i)
        return new_nums[0]


# We can use bit manipulation technique (XOR):

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
