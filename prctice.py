l=[1,2,0,3,0,8,9,0,6,0,8,0,2,7,0,0,0]
li=[]
l1=[]
for i in l:
    if i==0:
        li.append(i)
    else:
        l1.append(i)
for j in li:
    l1.append(j)
print(l1)
# print(li)


a=[123,423,523]

# a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
sum=0
for i in a:
    for j in str(i):
        # print(j)
        sum=sum+int(j)
    b.append(sum)
    sum-=sum
print(b)



a={"one":{1:2,3:4},"two":{5:4,3:6}}
b={}
for k,v in a.items():
    for i in v.keys():
        b[k]=v[i]
        break
print(b)








