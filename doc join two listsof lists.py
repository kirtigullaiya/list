# adding lists of lists of same index.
l1=[[10,20],[30,40],[50,60],[30,20,80]]
l2=[[61],[12,14,15],[12,13,19,20],[12]]
l3=[]
i=0
while i<(len(l1)):
    a=l1[i]+l2[i]
    l3.append(l1[i]+l2[i])
    # print(l3)
    i+=1
print(l3)