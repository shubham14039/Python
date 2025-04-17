# Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.


import array as arr

aray = arr.array('i',[2,3,4,5,12,32,45,53,67,9,8,89,91,78,56,99])
min = aray[0]
max = aray[0]
total = 0
for i in range(len(aray)):
    if aray[i]>max:
        max = aray[i]
    if aray[i]<min:
        min=aray[i]
    total += 1


print(f"The minimum element is {min}")
print(f"The maximum element is {max}")
print(f"The total number of comaprisons is {total}")
