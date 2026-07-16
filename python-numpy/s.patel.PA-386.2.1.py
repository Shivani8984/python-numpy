import numpy as np

# Create a NumPy array using np.array() function and specify the data type as 'int32.' 
# Print the array and its data type.

arr_int32 = np.array([1,2,3], dtype=np.int32)
print(arr_int32)

# Create another NumPy array using np.array() with the data type as 'float64.' Print the array and its data type.

arr_float64 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print(arr_float64)

# Create a one-dimensional NumPy array containing the integers from 1 to 5. Print the array.
oneD_array = np.array([1, 2, 3, 4, 5])
print(oneD_array)

# Create two NumPy arrays, arr1 and arr2, with any value of your choice. 
# Perform element-wise addition, subtraction, multiplication, and division between these arrays and print the results.


arr1 = np.array([12, 22, 25, 45])
arr2 = np.array([3, 6, 9, 12])

# 1. Element-wise Addition
addition = arr1 + arr2

# 2. Element-wise Subtraction
subtraction = arr1 - arr2

# 3. Element-wise Multiplication
multiplication = arr1 * arr2

# 4. Element-wise Division
division = arr1 / arr2

print("Array 1:", arr1)
print("Array 2:", arr2)
print("======================")
print("Addition Result:      ", addition)      
print("Subtraction Result:   ", subtraction)    
print("Multiplication Result:", multiplication) 
print("Division Result:      ", division)       

#  Calculate the dot product between arr1 and arr2. Print the result.
dot_array = np.dot(arr1, arr2)
print("Dot Array: " ,dot_array)


# Use NumPy to calculate the mean, median, and standard deviation of arr1.
mean_val = np.mean(arr1)

median_val = np.median(arr1)

std_dev = np.std(arr1)

print(f"Mean Value: {mean_val:.2f}")
print(f"Median Value: {median_val}")
print(f"Standard Deviation Value: {std_dev:.2f}")
