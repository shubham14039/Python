# Write a python fucntion that takes two 3-Dimensional numeric data sets and adds them componentwise
# That means if A = [[a1,a2,a3],[a4,a5,a6],[a7,a8,a9]] and B = [[b1,b2,b3],[b4,b5,b6],[b7,b8,b9]], then A+B = [[a1+b1,a2+b2,a3+b3],[a4+b4,a5+b5,a6+b6],[a7+b7,a8+b8,a9+b9]]
#
# c = []
# for i in range(len(a)):
#     d = []
#     for j in range(len(a[i])):
#         e = []
#         for k in range(len(a[i][j])):
#             ck = a[i][j][k] + b[i][j][k]
#             e.append(ck)
#         d.append(e)
#     c.append(d)
# print(c)


# If we dont want to use nested for loops (which increases the time complexity), we can use special packages like numpy for creating and manipulating arrays of various sizes.

import numpy as np

a = np.array(
    [
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ],
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ],
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    ]
)

b = np.array(
    [
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ],
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ],
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    ]
)

print(a+b)
