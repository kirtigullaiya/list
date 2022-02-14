# q14 of doc difference .
list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[2,4,6,8]
b=[]
i=0
while i<len(list1)-1:
    diff=list1[i+1]-list1[i]
    b.append(diff)
    i+=1
print(b)
