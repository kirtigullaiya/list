input_list=[1,2,2,5,8,4,4,8]
l=[]
count=0
for i in range(len(input_list)):
    if input_list[i] not in l:
        l.append(input_list[i])
        count+=1
    i+=1
print(l)
print(count)

