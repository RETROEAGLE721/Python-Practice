food=["apple","banana","orange","avacado","apple","grapes"]
print("ITEM ON INDEX 2 IS:-",food[2])
print("ITEMS BETWEEN INDEX 1 AND 4 ARE:-",food[1:4])
print("ITEMS FROM START TO INDEX 4 ARE:-",food[:4],"\nAND ITEMS FROM INDRX 2 UPTO END OF LIST ARE:-",food[2:])
print("THERE ARE TOTAL",food.count("apple"),"TIMES APPLE IN LIST")
food.remove("orange")
food.insert(2, "mango")
print("REPLACTING ORANGE WITH MANGO WE GET :-",food)
print("FINDING THE INDEX NUMBER OF MANGO AND NUMBER IS",food.index("mango"))
print("ADDING MANGO TO THE END OG LIST")
food.append("mango")
print(food)
print(food.pop(4))
print("REMOVING MANGO FROM LIST ",food.remove("mango"))
print(food)
#pop() is used when we wants to remove value from list nut we know index number and do not know the value on it.
#where as remove() is also use to removie value from list but it is use when we know value but not it's index number.
#remove() will only remove the value how's index number is lower. It will not remove the duplicate value if present. 
print(food.sort())
prise=["25Rs","60Rs","45Rs","100Rs"]
food=food.__add__(prise)
print(food)
#You can use food=food.__add__(prise) or food=food.copy()+prise.copy() to concatenet another string to food 




