a="aabcddddadnss"
b=[]
ch=a[0]
result=""
count=0
a=a+""
i=0
while i<len(a):
    # b.append([])
    # print(a[i])
    if a[i]==ch:
        count+=1
    else:
        result=result+str(count)+ch
        # b.append([])
        b.append(result)
        ch=a[i]
        count=1
        # b.append(result)
    i+=1
print(result)
print(b)

