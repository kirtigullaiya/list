i=0
j=4
list1=[1,2,3,4,5,6,7,8,9]
list2=[]
while i<len(list1):
    if i==j:
        list2.append(20)
        j+=4
    list2.append(list1[i])
    i+=1
    
print(list2)