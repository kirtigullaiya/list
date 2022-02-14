list=[1,2,3,1,2,2]
list1=[]
i=0
while i<len(list):
    if list[i] not in list1:
        list1.append(list[i])
    i+=1
print(list1)