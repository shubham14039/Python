import time 


list = [75, 28, 88, 67, 81, 16, 70, 86, 23, 38, 72, 77, 80, 51, 85, 15, 82, 10, 64, 53, 71, 44, 26, 21, 42, 25, 73, 22, 87, 94, 19, 33, 50, 96, 45, 40, 60, 55, 57, 83, 61, 66, 18, 89, 68, 79, 69, 74, 100, 31, 91, 52, 46, 13, 90, 34, 99]

# list.sort()
# print(list)



def search(l,t):
    for i in l:
        if i == t:
            print(f"{t} found at {l.index(i)}")

def binary_search(l,t):
    l.sort()
    low = 0
    high = len(l)
    while high-low>1:
        mid = (high+low)//2
        if l[mid]<=t:
            low = mid
        else:
            high = mid
    return l[low] == t



start = time.perf_counter()
search(list,99)
end = time.perf_counter() - start
print(f"In normal search. time: {end} ")

start = time.perf_counter()
print(binary_search(list, 99))
end = time.perf_counter() - start
print(f"In binary search. time: {end} ")



