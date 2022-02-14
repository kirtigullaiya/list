list=[["g","f","g"],["i","s"],["b","e","s","t"]]
i=0
sum=""
while i<len(list):
    j=0
    while j<len(list[i]):
        # sum=sum+list[i][j]
        print(list[i][j],end="")

        j+=1
    print(sum,end="")
    print()
    i=i+1
print(sum) 

# a=[10,20,30,20,10,50,60,40,80,50,40]
# items=set()
# y=[]
# for i in a:
#     if i not in items:
#         y.append(i)
#         items.add(i)
# print(y)