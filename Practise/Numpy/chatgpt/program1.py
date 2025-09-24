import numpy as np

# ============================================
# Shape & Reshape
# ============================================

# Q1. Reshape into 3x4
# Array: [1,2,3,4,5,6,7,8,9,10,11,12]
# Your answer here
data = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(data.shape)
print(data.reshape(3,4))


# Q2. Flatten into 1D
# Array: [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# Your answer here
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data.reshape(9))

# Q3. Reshape into (2,6)
# Array: [[1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12]]
# Your answer here
data = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(data.reshape(2,6))

# ============================================
# Indexing & Slicing
# ============================================

# Q4. Get element at row=2, col=1
# Array: [[10,20,30],
#         [40,50,60],
#         [70,80,90]]
# Your answer here
data = np.array([[10,20,30],
         [40,50,60],
         [70,80,90]])
print(data[2][1])


# Q5. Slice middle 2x2
# Array: [[1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12],
#         [13,14,15,16]]
# Your answer here
data = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
print(data [1:3, 1:3])

# Q6. From 3D, get arr[1, :, 2]
# Array: [[[1,2,3],[4,5,6]],
#         [[7,8,9],[10,11,12]],
#         [[13,14,15],[16,17,18]]]
# Your answer here


# ============================================
# Concatenate & Split
# ============================================

# Q7. Concatenate horizontally
# Arrays: [[1,2],[3,4]]  and  [[5,6],[7,8]]
# Your answer here


# Q8. Concatenate vertically
# Arrays: [[1,2],[3,4]]  and  [[5,6],[7,8]]
# Your answer here


# Q9. Split into 3 equal parts
# Array: [10,20,30,40,50,60]
# Your answer here


# ============================================
# Arithmetic Operations
# ============================================

# Q10. Add two arrays
# Arrays: [1,2,3]  and  [4,5,6]
# Your answer here


# Q11. Subtract arrB from arrA
# Arrays: [10,20,30]  and  [1,2,3]
# Your answer here


# Q12. Multiply element-wise
# Arrays: [[1,2],[3,4]]  and  [[2,2],[2,2]]
# Your answer here


# Q13. Divide element-wise
# Arrays: [10,20,30]  and  [2,4,5]
# Your answer here


# Q14. Sum of all elements
# Array: [[1,2,3],[4,5,6]]
# Your answer here


# Q15. Product of all elements
# Array: [2,3,4]
# Your answer here


# Q16. Difference between consecutive elements
# Array: [10,15,20,25]
# Your answer here


# ============================================
# Regex Match (np.char)
# ============================================

# Q17. Extract digits
# Array: ["apple","banana123","cherry45","date"]
# Your answer here


# Q18. Find words starting with 'b'
# Array: ["apple","banana123","cherry45","date"]
# Your answer here


# Q19. Replace all digits with '#'
# Array: ["apple","banana123","cherry45","date"]
# Your answer here


# Q20. Check which contain "an"
# Array: ["apple","banana123","cherry45","date"]
# Your answer here


# ============================================
# Where
# ============================================

# Q21. Replace even numbers with 0
# Array: [1,2,3,4,5,6,7,8,9,10]
# Your answer here


# Q22. Label >25 as "High", else "Low"
# Array: [10,20,30,40,50]
# Your answer here


# Q23. Get indices of numbers >50
# Array: [15,60,25,80,30,100]
# Your answer here


# Q24. Replace negatives with abs
# Array: [-1,2,-3,4,-5]
# Your answer here


# ============================================
# Sort
# ============================================

# Q25. Sort ascending
# Array: [5,2,9,1,7]
# Your answer here


# Q26. Sort each row
# Array: [[3,1,2],[9,7,8]]
# Your answer here


# Q27. Sort each column
# Array: [[3,1,2],[9,7,8]]
# Your answer here


# Q28. Sort strings
# Array: ["dog","apple","banana"]
# Your answer here


# ============================================
# Filtering
# ============================================

# Q29. Filter values >20
# Array: [10,15,20,25,30]
# Your answer here


# Q30. Extract values greater than mean
# Array: [[1,2,3],[4,5,6],[7,8,9]]
# Your answer here


# Q31. Filter even numbers
# Array: [1,2,3,4,5,6]
# Your answer here


# Q32. Divisible by both 2 and 5
# Array: [5,10,15,20,25,30,35,40]
# Your answer here


# Q33. Names longer than 5
# Array: ["Ram","Krishna","Mohan","Amit"]
# Your answer here


# ============================================
# Power
# ============================================

# Q34. Square of numbers
# Array: [1,2,3,4,5,6,7,8,9,10]
# Your answer here


# Q35. Cube of numbers
# Array: [2,3,4,5]
# Your answer here


# Q36. Raise to 4
# Array: [[1,2,3],[4,5,6],[7,8,9]]
# Your answer here


# Q37. Power with array exponents
# Arrays: [10,100,1000]  and  [1,2,3]
# Your answer here


# Q38. Broadcasting power
# Arrays: [1,2,3]  and  [2,3,4]
# Your answer here
