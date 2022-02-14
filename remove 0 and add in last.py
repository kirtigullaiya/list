# doc question
# remove 0 and append at last in the list.
a=[1,5,0,6,7,0,2,3,0,10,0,6,0,0,8,0]
i=0
count=0
while i<len(a):
    if a[i]==0:
        count+=1
        pass
    i+=1

k=0
m=[]
while k<len(a):
    if a[k]!=0:
        m.append(a[k])
    k+=1
j=1
while j<=count:
    m.append(0)
    j+=1
print(m)