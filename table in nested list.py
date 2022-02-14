# table in nested list.
num=int(input("please enter num:"))
b=[]
c=[]
i=1
d=num
while i<=10:
    m=i*num
    b.append(m)
    c.append(b)
    d-=1
    i+=1
# c.append(b)
print(c)
