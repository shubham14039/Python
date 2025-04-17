# Let B be an array of size n >= 6 containing integers from 1 to n-5, inclusive, with exactly five repeated. Describe a good algorithm for finding the five integers in B that are repeated.


ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,9, 25, 26, 27, 28, 29, 30, 31, 32, 94, 33, 34, 35, 36, 37, 38, 39, 40, 40, 41,42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 46, 52, 53, 54, 55, 56, 57, 58, 59, 93, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94] 

#
# This method does the part work, but it has some problems:
#     1. If the list is very long then it will take infinite time
#     2. It only scans the sliced list upto the element (from the beginning), which does not work in this case :- if the elements are not put in sorted order, then it will break

# list_of_el = []
# for j in range(len(ls)-1):
#     if ls[j] in ls[:j]:
#         list_of_el.append(ls[j])
# print(list_of_el)
#

# The more efficient program is as:
def five_repeated(nums: list[int]) -> list[int]:
    pass 

 
