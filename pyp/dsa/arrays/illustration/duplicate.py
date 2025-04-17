# # Write a python program to remove all the occurances of duplicate array elements (or simply: making a set from a list)
# import array as arr


# #  one method is to use the set() method, which changes an array into a set, removing duplicate elelemts. we are not goona do that way.

# # second method
# def duplicate(list):
#     for i in list:
#         if i not in list[0:list.index(i)]:
#             pass
#         else:
#             list.remove(i)
#     return list

# aray = arr.array('i',[3,4,6,7,4,2,8,4,3,9,0,1])
# print(duplicate(aray))



def remove_duplicate(arr):
    arr.sort()
    temp = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            temp.append(arr[i])
    temp.append(arr[-1])
    return temp 


if __name__ == '__main__':
    list = [1,2,3,2,4,4]
    print(remove_duplicate(list))