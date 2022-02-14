# list=[[1,2,4],[2,4,4],[1,2]]
# b=[]
# i=0
# sum=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         sum+=list[i][j]
#         print(list[i][j])
#         j+=1
#     i+=1

# make a list on how much length of lists inside a list:
list=[[1,2],[2,4],[2,4,3]]
b=[]
count=0
for i in range(len(list)):
    row=len(list[0])
    coloumn=len(list)
    # print(row,coloumn)  
    # b.append(row)
    # b.append(coloumn)
    # print(b)
    count+=1
b.append(row)
b.append(coloumn)
print(b)
# print(id(list))




