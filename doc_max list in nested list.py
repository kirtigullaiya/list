# # maximum length of list in a list.
a=[[0],[1,2,3],[5,7],[9,11],[13,15,17]]
i=0
max=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if max<j:
            max=i
        j+=1
    i+=1
print(max)
# print(a[i])
# print(a[i][j])
# print(id(a))

# for i in a:
#     if len(i)>max:
#         max=len(i)
#         b=i
# print(b)
# print(i)






