# a=[]
# size=int(input("how many elements you want?: "))
# i=0
# while i<size:
#     val=int(input("please enter number:"))
#     a.append(val)
#     i+=1
# print(a)
# sum=""
# b=0
# while i<len(a):
#     add=a[-1]+b
#     print(add,end="")
#     b*=10
#     print(b)
#     print(a)

list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
list3=[]
i=0
while i<len(list1):
    if list2[i] not in list1:
        print("unique    :",list2[i])
    else:
        print("duplicate :",list2[i])

    # list3.append(list2[i])  
    # list3.append(list1[i])
    i+=1
# print(list3)
# i+=1

