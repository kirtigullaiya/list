# comparison points earned by two lists- question6 doc
list=[1,2,3]
list1=[3,2,1]
b=[]
i=0
count=0
count1=0
while i<len(list):
    if list[i]>list1[i]:
        # print(list[i])
        count+=1
    else:
        # print(list1[i])
        count1+=1
    i+=1
b.append(count1)
b.append(count)
print(b)

# list=[1,2,3]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# list=[4,4,1,3]
# count=0
# while i<len(list)-1:
#     if list[i]>=1 and list[i]>=list[i+1]:
#         count+=1
#         # print("yes",list[i])
#     else:
#         print("no")
#     i+=1
# print(count)
    