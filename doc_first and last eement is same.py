# function doc question.
list=["abc","xyz","aba","1221"]
count=0
for i in list:
    if len(i)>1 and i[0]==i[-1]:
        count+=1
        # print("yes",i)
# print(count)

i=0
while i<len(list):
    if len(list[i])>1 and list[i][0]==list[i][-1]:
        # count+=1
        print("yes",list[i])
        count+=1
    i+=1
print(count)

