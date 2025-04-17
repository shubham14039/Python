# Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

import array as arr

aray = arr.array('i',[0,1,2,3,4,5,6,7,8,9])


def reverse_items(list):
    new_list = []
    for _ in range(len(list)):
        new_list.append(list[-1])
        list.pop() #popping is necessarry because only after popping we can append the trailing elements to the new list
    return new_list
    
print(reverse_items(aray))

# However we can use the built in reverse() function of python, which actually reverse the aray
