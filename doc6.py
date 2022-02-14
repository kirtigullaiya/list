a=["1","2","3","4","5","6"]
b=[]
i=0
while i<len(a)-1:
    add=a[i]+a[i+1]
    b.append(add)
    i+=1
# print(b)


# remove duplicate value and sum of the list.
a=[1,2,3,4,5,6]
b=[7,8,9,10,3,5]
c=[]
i=0
sum=0
sum1=0
while i<len(a):
    if a[i] not in c:
        c.append(a[i])
        sum+=a[i]
    i+=1
j=0
while j<len(a):
    if b[j] not in c:
        c.append(b[j])
        sum1+=b[j]
    j+=1
print(c)
print(sum+sum1)









