a=[6,7,8,[5,6,[6,7,7]]]
b=[]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
# print(b)

c=[]
i=0
sum=0
sum1=0
while i<len(b):
    if type(b[i])==list:
        j=0
        while j<len(b[i]):
            c.append(b[i][j])
            sum+=b[i][j]
            j+=1
    else:
        c.append(b[i])
        sum1+=b[i]
    i+=1
print(c)
print(sum+sum1)
