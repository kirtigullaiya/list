# add n number in list elements.question44(doc)
# a=[3,8,9,4,5,0,5,0,3]
# add=int(input("please enter number to add:"))
# b=[]
# for i in range(len(a)):
    # sum=add+a[i]
    # b.append(sum)
# print(b)

# l=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
# ins=int(input("please enter number to insert:"))
# b=[]
# count=0
# for i in range(len(l)):
#     if i%2==0:
#         l[i]=ins
#         count+=1
#         b.append(l[i])
# print(b)

list=[[1,2,4],[2,4,4],[1,2]]
list1=[]
i=0
while i<len(list):
    j=0
    add=0
    while j<len(list[i]):
        add=list[i][j]+list[i][j]
        # list1.append(add)
        print(add)
        j+=1
    i+=1
# print(list1)
