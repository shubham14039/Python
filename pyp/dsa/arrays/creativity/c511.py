# In experiment of code fragment 5.1, we begin with an empty list. If data were initially constructed with non empty length, does this affect the sequence of values at which the underlying array is expanded? Perform your own experiments, and comment on any relationship you see between the initial length and the expansion sewuence.



import sys

# data = []
data = [1,2,3,4,5]
for k in range(80):
    a = len(data)
    b = sys.getsizeof(data)
    print(f"length: {a}; size in bytes: {b}")
    data.append(None)
