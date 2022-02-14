# remove duplicates from nested.
a=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
i=0
b=[]

while i<len(a):
    # j=0
    # while j<len(a[i]):
    if a[i] not in b:
        # print(a[i][j])

        b.append(a[i])
        # j+=1
    i+=1
print(b)