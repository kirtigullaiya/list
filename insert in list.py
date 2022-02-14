# insert emp in list.
a=[1,2,3,4]
b=[]
i=0
while i<len(a):
    string="emp"+str(a[i])
    b.append(string)
    i+=1
print(b)

l=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
i=0
while i<len(l):
    j=0
    add=0
    while j<len(l[i]):
        add+=l[i][j]
        j+=1
    i+=1
print(add)