import numpy as np

# Indexing and Slicing

# arr = np.array([1,2,3,4,5])

# print(arr)
# print(arr[1])
# print(arr[1:4])

# # update an element in the array
# arr[0] = 10


# # update a slice of an array

# arr[1:4] = [6,7,8] 
# print(arr)

# Arithmetic Operations

# Create a 1D numpy array
# arr = np.array([1, 2, 3])

# # Perform arithmetic operations
# sum_arr = arr + 1  # Element-wise sum with scalar 1
# prod_arr = arr * 2 # Element-wise product with scalar 2
# div_arr = arr / 2  # Element-wise division with scalar 2
# # Print the results
# print(sum_arr)
# print(prod_arr)
# print(div_arr)


# print("=====================")
# arr = np.array([1,2,3,4,5,6])
# # Perform aggregate functions
# arr_sum = np.sum(arr)           # Sum of all elements
# mean_value = np.mean(arr)       # Arithmetic mean [cite: 957, 1258]
# median_value = np.median(arr)   # Middle value [cite: 958, 1275]
# std_deviation = np.std(arr)     # Standard deviation (spread) [cite: 960, 1297]
# arr_min = np.min(arr)           # Minimum value [cite: 1333]
# arr_max = np.max(arr)           # Maximum value [cite: 1333]
# # Print the results in a readable format
# print(f"Sum: {arr_sum}")
# print(f"Mean: {mean_value}")
# print(f"Median: {median_value}")
# print(f"Std Dev: {std_deviation:.2f}") # Formatted to 2 decimal places
# print(f"Min: {arr_min}, Max: {arr_max}")



# Reshaping and Transposing
# Create a 2D numpy array
# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# # Transpose the matrix using numpy's attribute
# transposed_matrix = matrix.T
# # Reshape the transposed matrix into a 3x2 matrix
# reshaped_matrix = transposed_matrix.reshape(2,3)
# # Print the original matrix, transposed matrix, and reshaped matrix
# print("Original Matrix:")
# print(matrix)

# print("transposed Matrix:")
# print(transposed_matrix)

# print("reshaped Matrix:")
# print(reshaped_matrix)



# NumPy—Boolean Operations

    # Logical AND
# a = np.array([True, True, False, False])
# b = np.array([True, False, True, False])
# c = np.logical_and(a, b)
# print(c)


#     # Logical OR
# a = np.array([True, True, False, False])
# b = np.array([True, False, True, False])
# c = np.logical_or(a, b)

# print(c) 


#     # Logical NOT
# a = np.array([True, False, True, False])
# b = np.logical_not(a)

# print(b) 

#     # Array-Wise Comparison
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([2, 2, 3, 3, 5])
# c = np.array_equal(a, b)

# print(c)


# # Sorting
# a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
# b = np.sort(a)

# print(b)

# Searching and Counting
# arr = np.array([33, 2, 3,56,58,96,4,6,9,])
# x = 3
# print("Is 3 in the array?")
# print(x in arr)
# print("The index of the minimum value:")
# print(np.argmin(arr))
# print("The index of the maximum value:")
# print(np.argmax(arr))

# Example 1: Count non-zero elements in a 1D array
arr_1d = np.array([0, 5, 0, 8, 0, 3, 7, 0])
nonzero_count_1d = np.count_nonzero(arr_1d)

print("1D Array:", arr_1d)
print("Number of Non-Zero Elements:", nonzero_count_1d)

# Example 2: Count non-zero elements in a 2D array
arr_2d = np.array([[0, 2, 0, 4],
          [5, 0, 0, 8],
          [0, 0, 3, 0]])
nonzero_count_2d = np.count_nonzero(arr_2d)
print("2D Array:")
print(arr_2d)
print("Number of Non-Zero Elements:", nonzero_count_2d)
