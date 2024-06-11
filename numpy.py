import numpy as np

# Define a list of lists representing a 2D array
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l)  # Print the original list of lists

# Convert the list of lists to a NumPy array
arr = np.array(l)
print(arr)  # Print the NumPy array

# This array provided representions of 3x3 matrix with elements 1 to 9 arranged in rows and columns.


# Create a 5x5 NumPy array filled with zeros
arr1 = np.zeros((5, 5))
print(arr1)  # Print the array

# Create a 3x3 NumPy array filled with ones
arr2 = np.ones((3, 3))
print(arr2)  # Print the array

# Create a NumPy array containing numbers from 1 to 9
arr4 = np.arange(1, 10)
print(arr4)  # Print the array

import numpy as np

# Single Dimensional
# Create arrays 'a' and 'b' with numbers from 0 to 3 and 4 to 7 respectively
a = np.arange(4)
b = np.arange(4, 8)
print(a)  # Print array 'a'
print(b)  # Print array 'b'
print(a * b)  # Print the element-wise product of arrays 'a' and 'b'

# Multi Dimensional
# Create arrays 'c' and 'd' representing a 3x3 array with numbers from 0 to 8 and a 3x3 array filled with ones respectively
c = np.arange(0, 9).reshape(3, 3)
d = np.ones((3, 3))
print(c)  # Print array 'c'
print(d)  # Print array 'd'
res= c * d # element-wise product of arrays 'a' and 'b'
print(res)

 #[[0*1 1*1 2*1]  Each element of 'c' is multiplied by the corresponding element of 'd'
 #[3*1 4*1 5*1]
 #[6*1 7*1 8*1]]
 
# Memory management: NumPy handles memory automatically, so you don't need to worry about it when working with arrays.
# Looping over elements: NumPy let as apply operations to entire arrays at once, saving  as from writing loops to process individual elements.
# Data type conversions: NumPy converts data types as needed
# Index manipulation: NumPy provides easy ways to access and modify array elements without needing to manually calculate indices.
