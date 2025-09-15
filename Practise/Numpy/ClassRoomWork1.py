"""
1. create 1d array 10,20,30,40,50,60 -> 1D array
2. Slice - [2:]
3. [3:5]
4. [-4]
5. reverse the array

"""
import numpy as np

oneD_array = np.array([10,20,30,40,50,60])


print("One_D_Array : ", oneD_array)
print("Dimension of One_D_Array : ", oneD_array.ndim)

print("oneD_array[2:] -> ", oneD_array[2:])
print("oneD_array[3:5] -> ",oneD_array[3:5])
print("oneD_array[-4] -> ", oneD_array[-4])
print("oneD_array[::-1] -> ", oneD_array[::-1])

print(oneD_array[1:4])
