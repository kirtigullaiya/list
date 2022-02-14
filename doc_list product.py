list=[6,1,3,5,6,3,1]
list1=[]
multiply=1
for i in range(len(list)):
    if list[i] not in list1:
        list1.append(list[i])
        multiply*=list1[i]
    i+=1
print(list1)
print(multiply-30)
