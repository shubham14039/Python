# write a python program to remove the element right after the element entered by the user
# If the element entered by the user is the last element, then remove the first element

import array as arr

def remove_element(input_array, element):
    try:                                              # Try block attempts to find the index of the element
        index_element = input_array.index(element)    # If the element is found, it continues. Otherwise
    except ValueError:                                # .index() raises a ValueError
        print("element is not present in the list")   # The except block catches this exception, prints a message     
        return input_array                              # indicating the element isn't present, and returns the original array unchanged.
    if index_element != len(input_array)-1:
        input_array.pop(index_element+1)
    else:
        print("Element is the last one in the array")
    return input_array

aray = arr.array('i',[1,2,3,4,5,6,7,8,9])
print(remove_element(aray,10))
