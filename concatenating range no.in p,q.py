a=["p","q"]
b=[]
i=0
k=int(input("please enter:"))
while i<len(a):
    j=1
    while j<=k:
        sum=a[i]+str(j)
        b.append(sum)
        j+=1
    i+=1
print(b)
