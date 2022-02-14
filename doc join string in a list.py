# join adjacent numbers in alist.question doc 36


list=["1","2","3","4","5","6","7","8"]
l=[]
i=0
while i<len(list)-1:
    add=list[i]+list[i+1]
    l.append(add)
    i+=1
print(l)


# converting nested to flat list.
a=[1,2,[2,3,4],[5,6,8]]
b=[]
i=0
while i<len(a):
    # print(a[i])
    if type(a[i])==type(list): 
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
# print(b)



