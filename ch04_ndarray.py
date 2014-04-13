# Chapter 4 snippets

import numpy as np

data = np.array([[.9526, -0.246, -0.8856],[0.5639, 0.2379, 0.9104]])
data
data*10
data+data

# every nd array has a shape & data type
data.shape
data.dtype

data1 = [6,7.5,8,0,1]
arr1 =np.array(data1)
arr1

# Use nested sequences for higer dimensions
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
arr2
arr2.ndim
arr2.shape

# dtypes are defined for all the nd arrays, and best guess is made on input
arr1.dtype
arr2.dtype

# there are a couple ways to inialize an ndarray
np.zeros(10)
np.zeros((3,6))
np.empty((2,3,4))

np.arange(15)

# Data Types
arr1 = np.array([1,2,3], dtype=np.float)
arr2 = np.array([1,2,3], dtype=np.int32)
arr  = np.array([1,2,3,4,5])
arr.dtype
float_arr = arr.astype(np.float64)

# Cast example
arr = np.array([3.7,-1.2,-2.6,0.5, 12.9, 10.1])
arr
arr.astype(np.int32)

# Arithmic operations are element wise
arr * arr
arr - arr
# with scalar operations, it is executed across entire array as expected
1 / arr
arr ** 0.5

# One dim np arrays act similar to python arrays
arr = np.arange(10)
arr[5]
arr[5:8] = 12
arr

# Be aware that assignments are not copies, they are views of original array
arr_slice = arr[5:8]
arr_slice[1] = 12345
arr
arr_slice[:]=64
arr

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[2]
arr2d[0][2]
arr2d[0,2]

# boolean indexing
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
names == 'Bob'
data = randn(7,4)
data[names=='Bob']
data[names=='Bob',2:]
data[names=='Bob',3]

# Check out book for fancy indexing & transpose and swap
# Check out book for listing of fast unifuncs in numpy

# data processing example:
points = np.arange(-5,5,0.01)
xs, ys = np.meshgrid(points, points)

import matplotlib.pyplot as plt
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

# Theres a pretty slick way to express conditional logic:
xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True, False, True, True, False])

#Inefficient Method:
result = [(x if c else y)
          for x,y,c in zip(xarr,yarr,cond)]
# Efficient Method
result = np.where(cond,xarr,yarr)

# aggregate functions cans be called via either the array method or top level numpy
arr = np.random.randn(5,4)
arr.mean()
np.mean(arr)
arr.sum()
arr.mean(axis=1)
arr.sum(0)

# There are also array functions which return arrays:
arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
arr.cumsum(0)
arr.cumprod(1)

# Very common, be aware that True is coersed to 1 in sum
arr = randn(100)
(arr>0).sum()

bools = np.array([False, False, True, False])
bools.any()
bools.all()

#Sorting
arr = rand(8)
arr.sort()
arr
arr = rand(5,3)
arr.sort()
arr
#Top level sorting produces a sorted copy
large_arr = randn(1000)
large_arr.sort()
#... heres a good methof for percentile
large_arr[int(0.05 * len(large_arr))]

# unique() and set logic
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will','Joe', 'Joe'])
np.unique(names)
values = np.array([6,0,0,3,2,5,6])
np.in1d(values,[2,3,6])

# read/write to disk
arr = np.arange(10)
np.save('some_array',arr)
np.load('some_array.npy')
np.savez('array_archive.npz',a=arr,b=arr)
arch = np.load('array_archive.npz')
arch['b']

# save Load text files
# You can do this with np.loadtxt and np.genfromtxt

# Linear Algebra
x = np.array([[1.,2.,3.],[4.,5.,6.]])
y = np.array([[6.,23.],[-1.,7.],[8,9]])
x.doy(y)
np.dot(x,y)

from numpy.linalg import inv, qr
X = randn(5,5,)
mat = X.T.dot(X)
inv(mat)
np.round(mat.dot(inv(mat)),0)
q,r = qr(mat)
q
r

# random number generators
samples = np.random.normal(size=(4,4))
samples






















