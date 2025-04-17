# write a function to count  the frequency of each element in an array
def frequency(list):
    frequency = {}
    for i in list:
        if i not in frequency.keys():
            frequency[i] = 1
        else:
            frequency[i] += 1
    return frequency



# Given two arrays, write a function to find out the list of elements which occur in both the lists 
def intersection(list1, list2):
    def binary_search(list2, target, low=0, high=None):
        if high is None:
            high = len(list2) - 1
    
        if low > high:
            return False
    
        mid = (low + high) // 2
    
        if list2[mid] == target:
            return True
        elif target < list2[mid]:
            return binary_search(list2, target, low, mid - 1)
        else:
            return binary_search(list2, target, mid + 1, high)

            
    if len(list1) == 0 or len(list2) == 0:
        return "Either one or both of the lists are empty"
    
    common_elements = []
    for i in list1:
        if binary_search(list2, i):
            common_elements.append(i)
    return common_elements
# I HAVE NO IDEA WHaT I HAVE DONE
# l = [1,2,3,4,5,6,7,8,9]
# s = [1,87,34,2,4,56,23,6]
# print(intersection(s,l))


    
# Write a function to reverse an array
def reverse_array(list):
    pass
    
    
    
    
# Given an array of n integers, find two elements which sum upto the given target
def twoSum(list, target):
    new_list = []
    for i in list:
        for j in list:
            if i+j == target:
                new_list.append(i)
                new_list.append(j)
    return new_list
# It iterates through the list two times, so it returns the same thing two times


list = [1,2,3,4,5,6,7,8]
print(twoSum(list, 4))





