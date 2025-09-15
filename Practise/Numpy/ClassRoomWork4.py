
"""
Assignment Detals:

Create a Python script named numpy_array_basics.py that demonstrates the following:

1. Creating
Create a 1D NumPy array with execution times of 8 test cases:
o [10, 15, 20, 25, 30, 35, 40, 45]
2. Indexing & Shaping
Access the first, last, and 3rd element of the array.
Print the shape of the array.
3. Slicing
Print execution times of the first 3 tests.
o Print every alternate test time.
4. Iteration
o Iterate through the array and print each execution time with a message:
"Test X execution time: Y seconds".
5. Reshaping
o Reshape the 1D array (8 elements) into a 2D array of shape (2,4).
Print the reshaped array.
6. Joining
Create another NumPy array with 4 more execution times:
[50, 55, 60, 65]
Join (concatenate) this with the first array to form a longer array.
7. Splitting
Split the final array into 3 smaller arrays (equal parts if possible).
o Print each split.
"""
import numpy as np

oneDArray = np.array([10, 15, 20, 25, 30, 35, 40, 45])

#Access the first, last, and 3rd element of the array. Print the shape of the array.
print(oneDArray[0])
print(oneDArray[-1])
print(oneDArray[2])
print(oneDArray.shape)

#Print execution times of the first 3 tests. Print every alternate test time.
print(oneDArray[0:3])
print(oneDArray[::2])


# Iterate through the array and print each execution time with a message: "Test X execution time: Y seconds".
for (index, seconds) in enumerate(oneDArray):
    print(f"Test {index} execution time: {seconds} seconds")

# Reshape the 1D array (8 elements) into a 2D array of shape (2,4)
print(oneDArray.reshape(2,4))

#6. Joining Create another NumPy array with 4 more execution times: [50, 55, 60, 65]. Join (concatenate) this with the first array to form a longer array.
newArray =  np.array([50, 55, 60, 65])
concatenatedArray = np.concatenate((oneDArray, newArray))
print(concatenatedArray)

#7. Split the final array into 3 smaller arrays (equal parts if possible). Print each split.
print(np.split(concatenatedArray,3))