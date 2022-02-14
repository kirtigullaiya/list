a=[[1,4,8],[5,6,7],[3,5,6]]
sum=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum+=a[i][j]
        # print(sum)
        j+=1
    i+=1
print(sum)
