# Write a python program to remove the element with maximum frequency of occurance

import array as arr

def remove_freq_element(list):
    # Initialize a dictionary and add number of times an element is occuring 
    frequency = {}
    for num in list:
        if num not in frequency.keys():
            frequency[num] = 1
        else:
            frequency[num] += 1


    # get the maxmum number of times a value has occured
    target_value = 0
    for value in frequency.values():
        if target_value < value:
            target_value = value
    
    # Remove the key corresponding to maximum value from the original list
    for key, value in frequency.items():
        if value == target_value:
            for _ in range(target_value):
                list.remove(key)
    return list

#  execution: 

list = arr.array('i',[1,2,3,2,4,2,5,2,6,4,3,2,6,7,5,6,8,3]) # total elements = 18, 2=5 remaining elemnts should be 13
print(remove_freq_element(list))
