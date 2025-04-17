# Let A be an array of size n>=2 and containing integers from 1 to n-1, inclusive, with exactly two repeate. Suggest an algorithm for finding the repeated integers in A

# This implementation is slow as it creates another data type (dixtionary in this case). So if a very large dataset is given,
#     it will consume a lot of space.
import array as arr

# def repeated(list):
#     frequency = {}
#     for i in list:
#         if i not in frequency.keys():
#             frequency[i] = 1
#         else:
#             frequency[i] += 1
#     return frequency
#
# Heres a faster and optimized implementation:

def repeated(ls):
    pass

    # Our approach:
    #     implement a sorting algorithm (merge sort or wuick sort)
    #     search for two conseqcutive integers which are same 

aray = arr.array('i', [1,2,3,4,2,5,6,2,7,8,2,9])
print(repeated(aray))


# What am i doing here 
