a = (21,32,23)
try:
    for i in range(10):
        print(a[i])
        try:
            b = 13/0
        finally:
            print("Program finished")
except Exception as e:
    print(e)
else:
    print(a)
finally:
    print("Program finished")