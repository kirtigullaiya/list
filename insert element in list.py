# insert element after every element.
a=["red","black","green"]
ele=input("please enter string:")
inc=0
i=0
b=[]
while i<len(a):
    if i==inc:
        b.append(ele)
        inc+=1
        b.append(a[i])
    i+=1
print(b)
