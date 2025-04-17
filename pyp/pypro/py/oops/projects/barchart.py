
# Write a python program that inputs a document and then outputs a barchart plot of the frequencies of each alphabet that appears in the document

import matplotlib.pyplot as plt
import string
from collections import Counter

class Bar:
    def __init__(self, file) -> None:
        self._file = file
        self.categories = list(string.ascii_letters)
        self.char_count = Counter()
    
    def file_reading(self):
       char_list = [] 
       with open(self._file, 'r') as file:
           for line in file:
               for char in line:
                   if char in self.categories:
                       char_list.append(char)
       return char_list
        
    def count_characters(self):
        char_list = self.file_reading()
        self.char_count = Counter(char_list)
        self.values = [self.char_count[char] for char in self.categories]
    
    def plot(self):
        self.count_characters()
        plt.figure(figsize=(12, 6))  
        plt.bar(self.categories, self.values, color='skyblue')
        plt.title("Plot of occurance of alphabets")
        plt.xlabel("alphabets")
        plt.ylabel("total occurances")
        plt.show()


bar_plot = Bar('text.txt')
bar_plot.plot()