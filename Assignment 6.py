"""
NumPy Fundamentals - Concise Version
"""

import numpy as np

# 1D, 2D, 3D arrays
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2],[3,4]])
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("1D:", arr1)
print("2D:\n", arr2)
print("3D:\n", arr3)

# Array attributes - shape, dimensions, size, data type
print("Shape:", arr1.shape, arr2.shape, arr3.shape)
print("Dim:", arr1.ndim, arr2.ndim, arr3.ndim)
print("Size:", arr1.size, arr2.size, arr3.size)
print("Dtype:", arr1.dtype, arr2.dtype, arr3.dtype)

# Indexing and slicing - accessing elements and subarrays
arr = np.array([10,20,30,40,50,60,70,80])
print("Original:", arr)
print("Index 2:", arr[2])
print("Slice 2:6:", arr[2:6])
print("First 3:", arr[:3])
print("Last 3:", arr[-3:])
print("Step 2:", arr[::2])

mat = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Matrix:\n", mat)
print("Row 0:", mat[0])
print("Col 0:", mat[:,0])
print("Rows 0-1, Cols 1-2:\n", mat[0:2, 1:3])

# Reshaping - changing array dimensions
arr = np.arange(12)
print("Original:", arr)
print("Reshape 3x4:\n", arr.reshape(3,4))
print("Reshape 2x3x2:\n", arr.reshape(2,3,2))
print("Flatten:", arr.reshape(3,4).flatten())

# Generating arrays using built-in functions
print("zeros(3):", np.zeros(3))
print("zeros(2,3):\n", np.zeros((2,3)))
print("ones(4):", np.ones(4))
print("arange(0,10,2):", np.arange(0,10,2))
print("linspace(0,10,5):", np.linspace(0,10,5))
print("eye(3):\n", np.eye(3))
print("random(2,3):\n", np.random.rand(2,3))

# Mathematical operations - element-wise arithmetic
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print("a:", a, "b:", b)
print("Add:", a+b)
print("Sub:", a-b)
print("Mul:", a*b)
print("Div:", a/b)
print("Power:", a**2)
print("Sqrt:", np.sqrt(a))
print("Exp:", np.exp(a))
print("Log:", np.log(a))

# Vectorized operations - applying operations to entire arrays at once
data = np.array([10,20,30,40,50])
print("Data:", data)
print("+5:", data+5)
print("*2:", data*2)
print(">25:", data>25)
print("==30:", data==30)

# Boolean masking - filtering arrays using conditions
scores = np.array([45,67,89,34,78,92,56,88,71,63])
print("Scores:", scores)
print(">70:", scores[scores>70])
print("70-90:", scores[(scores>70)&(scores<90)])
scores[scores<40] = 40
print("Min 40:", scores)

# Broadcasting - operations between different shaped arrays
mat = np.array([[1,2,3],[4,5,6]])
print("Matrix:\n", mat)
print("+10:\n", mat+10)
row = np.array([10,20,30])
print("+ Row:", mat+row)
col = np.array([[10],[20]])
print("+ Col:\n", mat+col)

# Aggregate functions - summary statistics
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Array:\n", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))
print("Std:", np.std(arr))
print("Column Sum:", np.sum(arr, axis=0))
print("Row Mean:", np.mean(arr, axis=1))

# Practical example - analyzing student grades
np.random.seed(42)
grades = np.random.randint(50,100,(5,4))
print("Grades (5x4):\n", grades)
print("Student Averages:", np.mean(grades, axis=1))
print("Subject Averages:", np.mean(grades, axis=0))
print("Top Student:", np.argmax(np.mean(grades, axis=1)))
print("Failing any subject:", np.any(grades<60, axis=1))

# Data types - checking and converting array data types
print("Int:", np.array([1,2,3]).dtype)
print("Float:", np.array([1.0,2.5]).dtype)
print("Bool:", np.array([True,False]).dtype)
print("Convert:", np.array([1,2,3]).astype(float).dtype)

# Advanced slicing - using steps and reverse
arr = np.arange(12)
print("Array:", arr)
print("Step 2:", arr[::2])
print("Reverse:", arr[::-1])
print("First 6 step 2:", arr[:6:2])
mat = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Matrix:\n", mat)
print("Every 2nd row/col:\n", mat[::2,::2])