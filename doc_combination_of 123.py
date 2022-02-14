list=[1,2,3]
length=len(list)
for i in range(length):
    for j in range(length):
        for k in range(length):
            if j!=k and k!=i and i!=j:
                print(list[i],list[j],list[k])
