# Use standard control structures to compute the sum of all numbers in an nxn data set, represented as a list of lists.
#
def summation(nums):
    total = 0
    for i in nums:
        sums = 0
        for j in i:
            sums += j
        total += sums
    return total

ls = [[1,2,3],[4,5,6],[7,8,9]]
print(summation(ls))
#
# In the above example, the time complexity of the function is nXm (where n is the number of nested lists, and m is the number of elements in each list). Also this function is for only one nested list of lists. If we increase the number of nested lists, the time complexity becomes very large. 
#
# A better implementation would be the use of sum() function:


def summ(nums):
    total = 0
    for i in nums:
        total += sum(i)
    return total

print(summ(ls))


# Or in list comprehension syntax, we can summarize the whole code block, and at the same time also reducing the time complesity


total = [sum(i) for i in ls]
print(sum(total))
