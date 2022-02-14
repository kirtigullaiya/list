# remove 10 from list and merge both the lists.
a=[3,5,7,9,10]
b=[2,4,6,8]
i=0
while i<len(a):
    if a[i]==10:
        pass
    else:
        b.append(a[i])
        # c.append(b)
    i+=1
print(b)
