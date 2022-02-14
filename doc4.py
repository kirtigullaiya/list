# question14 doc list:
# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
list=[7,9,8,9,79]
i=0
b=[]
# max=[[0]]
while i<len(list):
    j=0
    c=[]
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count+=1
        j+=1
    c.append(list[i])  
    c.append(count) 
    if c not in b:
        b.append(c)
    i+=1
print(b)
