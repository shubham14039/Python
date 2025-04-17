# The follwing code returns the sum of all the elements inside a nested list. 
def recurring_sum(list):
    ls = []
    for i in list:
        ls.append(sum(i))
        
    return sum(ls)

# This will work great
# But if we happen to encounter a huge number of nesting, then:
    # 1: We have to loop through a huge number of loops, which will take a lot of time
    # 2: We will write a lot of code 

# So, below is another function which handles the problem efficiently:



lis = [[2,3],[4,5],[8,1],[1,1]]
print(recurring_sum(lis))
