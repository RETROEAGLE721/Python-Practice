import numpy as np
a = np.array([[[1,2,3],
               [4,5,6]],
              [[7,8,9],
               [10,11,12]]])
b = np.array([[[1,2,3],
               [4,5,6]],
              [[7,8,9],
               [10,11,12]]])
print("Original matrix:-")
for x in a :
    print(x)

print("Matrix after adding 2:-")
print(a+b)
print("Matrix after Dividing 2:-")
# two times // to divide and to get outptu without decimal numbers  
#  one times // to divide and get outptu with decimal numbers 
print(a//2)
print((a/2).astype(int))

print("Matrix after square of every element:")
print(a**2)
