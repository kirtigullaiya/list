# nested list of consecutive numbers.doc question37
a=[1,2,3,4,5,6]
i=0
b=[]
while i<len(a)-1:
    b.append([])
    res=a[i],a[i+1]
    b[i].append(res)
    # b[i].append(a[i+1])
    # j=0
    # while j<len(a):
        # b[i].append(a[j],a)
        # b[i].append(a[j])
        # j+=1
    i+=1
print(b)




