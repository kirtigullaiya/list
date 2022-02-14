l=[1,2,3,4]
string=input("please enter string:")
# add=""
i=0
while i<len(l):
    add=string+str(l[i])
    l.append(add)
    i+=1
print(l)
