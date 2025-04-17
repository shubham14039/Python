# write a python program to copy the elements of an ARRAY to another array

# How to copy an array to another array:
# First we will have to create an array data type
 
import array as arr

def copy(input_array):
    copied_array = [None]*len(input_array)
    for i in range(len(input_array)):
        copied_array[i] = input_array[i]
    return copied_array

input_arr = arr.array('i', [34,23,53,2,67,36,78])
print(copy(input_arr))
