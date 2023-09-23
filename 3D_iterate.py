import numpy as np
a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in a:
    for y in x:
        for z in y:
            print(z)
print()

for x in np.nditer(a):
    print(x)
    