import numpy as np

a = np.array([[[1,2,3],
            [4,5,6]],
            [[7,8,9],
            [10,11,12]]])

print("Original array:-")
print(a)
print("Array has ",a.shape,"rows and columns befor transpose")

print("Array after tranpose:-")
a = a.T
print(a)
print("Array has ",a.shape,"rows and columns after transpose")