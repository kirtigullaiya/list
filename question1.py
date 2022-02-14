# # insert a element in list after every nth element.
# a=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
# i=0
# b=[]
# while i<len(a):
#     if i==4:
#         a.insert(4,20)  

#         # b.append(a[i])
#         # print(b)
#     i+=1
# # a.insert(4,20)
# print(a)

list=["s","d","f","s","d","f","k","o","p","i","w","e","k","c"]
count=0
i=0
letter=input("please enter letter:")
while i in range(len(list)):
    if letter in list:
        count+=1
        print(count)
    i+=1
# 2nd number will be 3.t

num=int(input("enter:"))
if (num//100)%10==3:
    print((num//100)%10,"yes")
else:
    print((num//100)%10,"no")