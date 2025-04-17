def binary_search(l:list, n:int):
    if len(l) < 1:
        return False
    mid = len(l)//2
    if l[mid] == n:
        return True
    if n > l[mid]:
        return binary_search(l[mid+1:], n)
    else:
        return binary_search(l[:mid], n)

ls = [1,2,3,4,5,6,7,8]
print(binary_search(ls, 9))
