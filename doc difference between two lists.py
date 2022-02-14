# a=[3,8,10]
# b=[5,2,10,4]
# c=[]
# i=0
# while i<len(a):
#     diff=a[i]-b[i]
#     c.append(diff)
#     i+=1
# print(c)
# convert a list of characters into astring.

# a=["k","i","r","t","i"]
# string=""
# i=0
# while i<len(a):
#     string+=a[i]
#     i+=1
# print(string)

a=[[1],[2],[3]]
b=[]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    i+=1
print(b)