================================================================DO NOT RUN THE CODE BELOW===============================================================


# Based on the discussion of section 5.4.1, develop an experiment to compare the efficiency of python's list comprehension syntax versus the construction of a list by repeated calls to append.
#

import time
from memory_profiler import profile

@profile
def function_to_test():

    # Run one method at a time
    start_time = time.time()

    # Standard list comprehension:
    le = [i for i in range(100000)]

    # Generator comprehension:
    le = (i for i in range(100000))

    # Repeated calls to append:
    list = []
    for _ in range(100000):
        list.append(None)

    end_time = time.time()
    return ("Execution time:", end_time - start_time, "seconds")

print(function_to_test())




The results are given below, both in terms of time as well as space complexity:

For Generator comprehension:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15     51.2 MiB     51.2 MiB           1   @profile
    16                                         def function_to_test():
    17
    18     51.2 MiB      0.0 MiB           1       start_time = time.time()
    19                                             # le = [i for i in range(100000)]
    20     51.2 MiB      0.0 MiB           1       le = (i for i in range(100000))
    21                                             # list = []
    22                                             # for _ in range(100000):
    23                                             #     list.append(None)
    24     51.2 MiB      0.0 MiB           1       end_time = time.time()
    25     51.2 MiB      0.0 MiB           1       return ("Execution time:", end_time - start_time, "seconds")

('Execution time:', 3.910064697265625e-05, 'seconds')


For repeated calls to append:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15     50.8 MiB     50.8 MiB           1   @profile
    16                                         def function_to_test():
    17
    18     50.8 MiB      0.0 MiB           1       start_time = time.time()
    19                                             # le = [i for i in range(100000)]
    20     50.8 MiB      0.0 MiB           1       list = []
    21     51.5 MiB      0.0 MiB      100001       for _ in range(100000):
    22     51.5 MiB      0.7 MiB      100000           list.append(None)
    23     51.5 MiB      0.0 MiB           1       end_time = time.time()
    24     51.5 MiB      0.0 MiB           1       return ("Execution time:", end_time - start_time, "seconds")

('Execution time:', 2.147024154663086, 'seconds')


For list comprehension:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15     51.3 MiB     51.3 MiB           1   @profile
    16                                         def function_to_test():
    17
    18     51.3 MiB      0.0 MiB           1       start_time = time.time()
    19     55.1 MiB      3.8 MiB      100001       le = [i for i in range(100000)]
    20     55.1 MiB      0.0 MiB           1       end_time = time.time()
    21     55.1 MiB      0.0 MiB           1       return ("Execution time:", end_time - start_time, "seconds")

('Execution time:', 1.107391119003296, 'seconds')

