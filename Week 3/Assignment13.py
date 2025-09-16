import numpy as np

execution_times  = np.random.randint(5,51, size = (5,50))
print("Execution times : ",execution_times)

"""
1. Statistical Analysis
o Calculate the average execution time per cycle.
o Identify the test case with the maximum execution time in the entire dataset.
o Find the standard deviation of execution times for each cycle to measure consistency.
"""
print(f"1. Statistical Analysis\nAverage execution time per cycle : {np.mean(execution_times, axis = 1)} seconds")
max_execution_time = np.max(execution_times)

max_execution_time_test_cases = []
standard_deviation_across_each_cycle = []
for (rowindex, row) in enumerate(execution_times):
    standard_deviation_across_each_cycle.append("Cycle " + str(rowindex+1) + " : " + str(float(np.std(row))))
    for (colindex, col) in enumerate(row):
        if (col == max_execution_time):
            max_execution_time_test_cases.append((rowindex,colindex))
print(f"Test cases with the maximum execution time : {max_execution_time_test_cases}")
print(f"Standard deviation of execution times for each cycle : {standard_deviation_across_each_cycle}")

"""
2. Slicing Operations
o Extract the first 10 test execution times from Cycle 1.
o Extract the last 5 test execution times from Cycle 5.
o Extract every alternate test from Cycle 3.
"""
print(f"\n2. Slicing Operations\nFirst 10 test execution times from Cycle 1 : {execution_times[0,:10]}")
print(f"Last 5 test execution times from Cycle 5 : {execution_times[4, -5:]}")
print(f"Every alternate test from Cycle 3 : {execution_times[2, : : 2]}")


"""
3. Arithmetic Operations
o Perform element-wise addition and subtraction between Cycle 1 and Cycle 2.
o Perform element-wise multiplication and division between Cycle 4 and Cycle 5.
"""
print(f"\n3. Arithmetic Operations\nFirst 10 test execution times from Cycle 1 : {execution_times[0,:10]}")
print(f"Element-wise addition between Cycle 1 and Cycle 2 : {np.add(execution_times[0],execution_times[1])}")
print(f"Element-wise subtraction between Cycle 1 and Cycle 2 : {np.subtract(execution_times[0],execution_times[1])}")
print(f"Element-wise multiplication between Cycle 4 and Cycle 5 : {np.multiply(execution_times[3],execution_times[4])}")
print(f"Element-wise division between Cycle 4 and Cycle 5 : {np.divide(execution_times[3],execution_times[4])}")


"""4. Power Functions
o Square and cube all execution times.
o Apply a square root transformation on the dataset.
o Apply logarithmic transformation (np.log(array+1)) to normalize skewed data.
"""
print(f"\n4. Power Functions\nSquare of all execution times : {np.power(execution_times,2)}")
print(f"Cube of all execution times : {np.power(execution_times,3)}")
print(f"Square root transformation on the dataset : {np.sqrt(execution_times)}")
print(f"Logarithmic transformation to normalize skewed data : {np.log(execution_times+1)}")


"""
5. Copy Operations
o Create a shallow copy of the dataset and modify one cycle. Observe if the original
changes.
o Create a deep copy using .copy() and modify it. Confirm the original remains
unchanged.
"""
shallow_copy = execution_times.view()
print(f"\n5. Copy Operations\nShallow copy of the dataset: {shallow_copy}")
shallow_copy[0,0] = 0
print("Shallow_copy[0,0]  : ",shallow_copy[0,0])
print("execution_times[0,0]  : ",execution_times[0,0])
print(f"After modifiying an element in shallow copy, are both the elements in shallow and original are same? : {shallow_copy[0,0]==execution_times[0,0]}")

deep_copy = execution_times.copy()
print(f"\nDeep copy of the dataset: {deep_copy}")
deep_copy[0,0] = 100
print("Deep_copy[0,0]  : ",deep_copy[0,0])
print("execution_times[0,0]  : ",execution_times[0,0])
print(f"After modifiying an element in deep copy, are both the elements in deep and original are same? : {deep_copy[0,0]==execution_times[0,0]}")


"""6. Filtering with Conditions
o Extract all test cases in Cycle 2 that take more than 30 seconds.
o Identify tests that consistently (in every cycle) take more than 25 seconds.
o Replace all execution times below 10 seconds with 10 (minimum thresholding).
"""
print(f"\n6. Filtering with Conditions\nAll test cases in Cycle 2 that take more than 30 seconds : {execution_times[1][execution_times[1] > 30]}")
for (rowindex, row) in enumerate(execution_times,start=1):
    print (f"Tests in cycle {rowindex} which takes more than 25 seconds : {row[row > 25]}")
execution_times[execution_times < 10] = 10
print(f"Execution times after threshold update: {execution_times}")
