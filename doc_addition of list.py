a=[12,67,98,34]
b=[]
for i in a:
    sum=0
    for j in str(i):
        sum+=int(j)
    b.append(sum)
print(str(b))
    # print(str(i))
    # print(int(j))
# print(id(a))
