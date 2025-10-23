import numpy as np

def rrow(vector,index):
    vectEnd = vector / vector[index]
    return vectEnd
    # your code goes here
    # divide your vector by the vector element at the position given by the scalar to find the reduced row


l1 = np.array( [10,4,8])
assert rrow(l1,0)[0] == 1
assert rrow(l1,0)[1] == 0.4
assert rrow(l1,0)[2] == 0.8
assert rrow(l1,1)[0] == 2.5
assert rrow(l1,1)[1] == 1
assert rrow(l1,1)[2] == 2

l1 = np.array( [-3,8,5])
assert rrow(l1,1)[0] == -0.375
assert rrow(l1,1)[1] == 1
assert rrow(l1,1)[2] == 0.625
assert rrow(l1,2)[0] == -0.6
assert rrow(l1,2)[1] == 1.6
assert rrow(l1,2)[2] == 1

