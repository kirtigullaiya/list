# # question12 function doc.
# a=input("please enter number:")
# i=0
# last=0
# while i<1:
#     if a[i]=="0":
#         last=a[:-1]
#         # print(last)
#     i+=1
# print(last)

a=[1,2,[4,5,6],[7,8,9]]
b=[]
i=0
while i<len(a):
    if type(a[i])==list:
        for j in a[i]:
            b.append(j)
    else:
        b.append(a[i])
    i+=1
print(b)