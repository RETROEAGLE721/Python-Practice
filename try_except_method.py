def RBI():
    SBI()
    print("Program is in RBI")

def SBI():
    a=(32,42)
    try:
        for i in range(10):
            print(a[i])
    except Exception as e:
        print(e)
        
try:
    RBI()
except Exception as e:
    print(e)
else:
    print("Program is in else")
finally:
    print("Program finished")
