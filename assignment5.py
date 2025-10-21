import numpy as np

"""
2x + 3y = 13
3x - 4y = -6

hint: when solving, try the following approach to solve the system:
e1: 4x + 8y = 16
e2: 3x + 2y = 8

make a new equation by dividing e1 by the coefficient on the x:
1x + 2y = 4

make a new equation by dividing e2 by the coefficient on the x:
1x + 0.666666y = 1.33333333

make a new equation by subtracing the new e1 and the new e2
0x + 1.333333y = 2.666666666

solve for y by dividing this new equation by its coefficient

0x + 1y = 2

repeat the process, but with y to solve for x

"""

e1 = np.array( [] ) 
e2 = np.array( [] )

