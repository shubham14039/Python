# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
#
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

def repeat(ls: list[list[int]]) -> list[int]:
    new_list = [j for j in range(1,(len(ls)**2)+1)]
    for l in ls:
        for k in l:
            if k in new_list:
                new_list.remove(k)
            else:
                new_list.insert(0, k)
    return new_list

original = [[9,4,3],[1,6,5],[2,7,9]]
print(repeat(original))

# There are two loops in this function, which makes its time complexity O(n^2). Repeat the question for linear time complexity
