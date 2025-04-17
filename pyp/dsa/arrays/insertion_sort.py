
list = [9,8,4,3,6,7,2,5,1]
def insertion_sort(list):
    for i in range(1,len(list)):
        current = list[i]
        j = i
        while j > 0 and list[j-1] > current:
            list[j] = list[j-1]
            j -= 1
        list[j] = current
        
    return list

print(insertion_sort(list))
