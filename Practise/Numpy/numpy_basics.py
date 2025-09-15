import numpy as np

one_dim_array = np.array([1, 2 , 3, 4, 5 ])
two_dim_array = np.array([[1, 2 , 3, 4, 5 ],[1, 2 , 3, 4, 5]])
three_dim_array = np.array([[[1, 2 , 3, 4, 5 ],[6, 7 , 8, 9, 10]],[[11, 12 , 13, 14, 15 ],[16, 17 , 18, 19, 20]]])


print(one_dim_array)
print(type(one_dim_array))
print(one_dim_array.ndim)

print(two_dim_array[1][4])

print(three_dim_array[1][1][3])



print(three_dim_array[0:1,1:,::-1])

