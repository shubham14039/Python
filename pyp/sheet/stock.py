# We have to find the maximum difference between the two elements in a list, and only proceeding forward is allowed.

ls = [2,1,9,5,3,6,4,20]
n = len(ls)
all_max = 0
for i in range(n):
    total = 0
    for j in range(i, n):
        if ls[j] - ls[i] > total:
            total = ls[j] - ls[i]
    if total > all_max:
        all_max = total
print(all_max)


# I dont know what the fuck is going on here
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very large number
        min_price = float('inf')
        max_profit = 0
        
        # Loop through the prices once
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the potential profit with the current price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

