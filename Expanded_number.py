def expanded_form(num):
    print(num)
    num = list(str(num))
    p = "123456789"
    b =[]
    for x in num:
        if x in p:
            # print(num.index(x))
            a=len(num)-1-num.index(x)
            b.append(str(int(x)*10**a))
    print(b)
    return " + ".join(b)

expanded_form(420370022)