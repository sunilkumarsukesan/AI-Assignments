"""
3 dimensional array name - sample3dim
[0][0][0]
 [0][1][2]
[1][1][2]
"""
import numpy as np
sample3dim = np.array([[[1, 2 , 3, 4, 5 ],[6, 7 , 8, 9, 10]],
                       [[11, 12 , 13, 14, 15 ],[16, 17 , 18, 19, 20]],
                       [[21, 22 , 23, 24, 25 ],[26, 27 , 28, 29, 30]],
                       [[31, 32 , 33, 34, 35 ],[36, 37 , 38, 39, 40]]])

"""
print(sample3dim.shape)
print("three_D_Array : ", sample3dim)
print("Dimension of three_D_Array : ", sample3dim.ndim)

print(sample3dim[0][0][0])
print(sample3dim [0][1][2])
print(sample3dim[1][1][2])
print(sample3dim[::-1,::-1,::-1])
"""
#print(np.concatenate((sample3dim [2] [1] [1:3],sample3dim [3] [1] [1:3])))

print(sample3dim [2:4, 1 , 1:3])

