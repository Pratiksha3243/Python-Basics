import numpy as np

# x =[1,2,3,4,5,6]
# myArray = np.array(x)
# myArray2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(myArray)
# print(myArray2)

# print(myArray.shape) # gives the rows & columns
# print(myArray2.shape)

# print(myArray.dtype)# gives the space stored in
# print(myArray2.dtype)

# print(myArray.nbytes)# gives the space of all ele
# print(myArray2.nbytes)

# print(myArray.size)# gives the no of ele in arr
# print(myArray2.size)

# print(myArray.ndim)# gives the  no of dimensions
# print(myArray2.ndim)

# print(myArray.flat)# iterate on the loop and then print them
# print(myArray2.flat)

# myArray = np.zeroes([2,3])
# print(myArray)

# myArray = np.arange(1,100)
# print(myArray)

# # myArray = np.linspace(0,10,5)
# # print(myArray)

# # myArray = np.empty([2,3])
# # print(myArray)

# # myArray = np.identity(3)
# # print(myArray)

# # myArray = np.reshape([3,4])
# # print(myArray)

# ar = myArray.reshape(3,33)
# arr = ar.ravel()
# print("Reshaping")
# print("ravel")
# print(ar)

myArr = np.array([3,2,50],
                 [10,0,3],
                 [0,2,30])

arr = np.sum(myArr)
print(arr)

ar = myArr.sum(axis = 0)
print(ar)






 