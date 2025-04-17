# Write a python program that inputs a document and then outputs a barchart plot of the frequencies of each alphabet that appears in the document
# 
# 
# Use The concepts of object oriented programming


 
import matplotlib.pyplot as plt
import string
from collections import Counter


categories = list(string.ascii_letters) # List all the alphabet letters


lsit = [] # initialize an empty list for storing all the characters in the document
with open('text.txt', 'r') as file:
    for line in file:
        for char in line:
            if char in categories:
                lsit.append(char) # Append all the letters in the empty list
                
                
                
# Logic for counting and appending all the counted values
    # values = []
    # for i in categories:
    #     count = lsit.count(i)
    #     values.append(count)
    
count = Counter(lsit) # Count the occurances of each element in the list
values = [count[char] for char in categories] # Append each value 


plt.figure(figsize=(12, 6))  # Set figure size for better visibility
plt.bar(categories, values, color='skyblue')
plt.title("Plot of occurance of alphabets")
plt.xlabel("alphabets")
plt.ylabel("total occurances")
plt.show()