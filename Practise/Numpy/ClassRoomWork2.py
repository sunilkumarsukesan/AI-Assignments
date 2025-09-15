"""
1. Sample 2D Array
2. reverse the array
3. samplearray [0][1]
4. samplearray [1][1]
5. samplearray [0][3]
6. sum of all the two dimensional elements
"""
import numpy as np
two_dim_array = np.array([[1, 2 , 3, 4, 5 ],[6, 7 , 8,9,10]])

print("two_D_Array : ", two_dim_array)
print("Dimension of two_D_Array : ", two_dim_array.ndim)

print("Reversing the 2D array -> ", two_dim_array[::-1, ::-1])
print("two_dim_array[0][1] -> ",two_dim_array[0][1])
print("two_dim_array[1][1] -> " , two_dim_array[1][1])
print("two_dim_array[0][3] -> ",two_dim_array[0][3])

sum = 0
for (index,row) in enumerate(two_dim_array):
    print("row -> ", row , "index - > ", index)
    for (index,col) in enumerate(row):
        print("col -> ", col ,  "index - > ", index)
        sum = sum + col

print("Sum of all the elements : ", sum)

