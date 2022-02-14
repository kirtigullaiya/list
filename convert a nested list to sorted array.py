# convert a pair of values into a sorted unique array.
l=[(1,2),(3,4),(1,2),(5,6),(7,8),(1,2),(3,4),(3,4),(7,8),(9,10)]
a=[]
i=0
while i<len(l):
    j=0
    while j<len(l[i]):
        if l[i][j] not in a:
            a.append(l[i][j])
        j+=1
    i+=1
print(a)
