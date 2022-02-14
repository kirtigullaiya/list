m=[]
for i in range(3):
    m.append([])
    for j in range(3):
        m[i].append(j)
print(m)
# and upper one question is an example of converting into nestedlist.
# q47 of doc :: convert a list of strings into list of lists.
a=["red","maroon","yellow","olive"]
i=0
b=[]
while i<len(a):
    b.append([])
    j=0
    while j<len(a[i]):
        b[i].append(a[i][j])
        j+=1
    i+=1
print(b)
