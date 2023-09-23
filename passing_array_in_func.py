def maxx(a):
    c=a[0]
    for x in a:
        if c <x:
            c=x
    return c

print("Enter numbers:-")
a=input().split(',')
print("Original List is :-",a)
print("Max number in given list is:-",maxx(a))