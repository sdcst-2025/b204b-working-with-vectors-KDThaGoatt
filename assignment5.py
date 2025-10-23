import numpy as np
np.set_printoptions(legacy='1.25')

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

e1 = np.array( [2,3,13] ) 
e2 = np.array( [3,-4,-6] )

def vectorSolve():
    e1y = e1 / e1[0]
    e2y = e2 / e2[0]
    ey = e1y - e2y
    y = ey / ey[1]

    e1x = e1 / e1[1]
    e2x = e2 / e2[1]
    ex = e1x - e2x
    x = ex / ex[0]

    return round(x[2], 3), round(y[2],3)

xy = vectorSolve()

try:
    xint = int(xy[0])
    yint = int(xy[1])
    print(f"x = {xint} and y = {yint}")
except:
    print(f"x = {xy[0]} and y = {xy[1]}")