a=["1","2","3","4","5","6","7","8"]
length=len(a)
string=""
l=[]
i=0
j=0
while i<length:
    while j<length:
        a[j]=a[i]+a[i+1]
        string+=a[j]
        # print(string)
        l.append(string)
        print(l)
        i+=1
        # print(l)
for i in a:
    # for j in i:
    i+=(i+1)
    l.append(j)
    print(l)
        