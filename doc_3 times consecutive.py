list1=[4,5,5,5,3,8]
list2=[1,1,1,64,23,64,22,22,22]
length=len(list1)
length1=len(list2)-2
for i in range(length):
    if list1[i]==list1[i+1]:
        print(list1[i])
    else:
        print("no input is there.")
# for j in range(length1):
#     if list2[j]==list2[j+1]==list2[j+1+1]:
#         print(list2[j])
