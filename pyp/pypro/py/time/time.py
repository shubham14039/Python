import time 
"""
This script contains functions to calculate the sum of numbers from 1 to n and measure the execution time of the calculation.

Functions:
    sum_n(n): Calculates the sum of numbers from 1 to n.
    time_clac(q, function): Measures execution time using time.time() for a given function and range of inputs.
    time_calculation(j, func): Measures execution time using time.perf_counter() for a given function and range of inputs.

The script demonstrates the usage of these functions by calling time_clac() with sum_n() as an argument.
"""

def sum_n(n):
    add = 0
    for i in range(n+1):
        add += i
    return add

def time_clac(q, function): # Using time.time().  
    l = [i for i in range(1, q+1)] 
    for y in l:
        start = time.time() 
        function(y) 
        end = time.time() - start
        print(f"For n = {y}, Result = {function(y)}, Execution time: {end} seconds")
        



def time_calculation(j, func):  # Using time.perf_counter(). Used for measuring high performance operations. 
    lc = [i for i in range(1, j+1)]
    for k in lc:
        start = time.perf_counter()
        func(k)
        end = time.perf_counter() - start 
        print(f"For n = {k}, Result = {func(k)}, Execution time: {end:.2e} seconds")



def no_of_processes():
    pass
    
    
    
# time_calculation(10, sum_n)
time_clac(10, sum_n)