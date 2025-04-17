
import array as arr


# Function to find the frequency of 2 in the array
# def frequency(input_array):
#     count = 0
#     for i in input_array:
#         if i == 2:
#             count += 1
#     return count


def frequency(input_array):
    freq = {}
    for num in input_array:
        if num not in freq.keys():
            freq[num] = 1
        else:
            freq[num] += 1
    return freq
    
input_ar = arr.array('i',[1,2,3,4,5,2,7,8,9,2,5,6,2])
print(frequency(input_ar))
