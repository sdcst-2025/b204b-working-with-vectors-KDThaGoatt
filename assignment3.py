"""
represent each system of linear equations as a set of numpy vector arrays
the first one has been done for you:

2x + 3y = 13
x - 2y = -4
"""

import numpy as np

l1 = np.array( [2,3,13])
l2 = np.array( [1,-2,-4])

"""
x + y = 10
2x + y = 13
"""
l1 = np.array( [1,1,10])
l2 = np.array( [2,1,13])


"""
3x - 4y = 22
2x + y = 9
"""
l1 = np.array( [3,-4,22])
l2 = np.array( [2,1,9])

"""
5x - 3y = 7
3x + 4y = 1
"""
l1 = np.array( [5,-3,7])
l2 = np.array( [3,4,1])