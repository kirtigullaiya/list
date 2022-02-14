a=[1234,122,1984,19372,100]
length=len(a)
# i=0
# for i in range(length):
    # c=(a[i]//10000)%10
    # b=(a[i]//1000)%10
    # rev=(a[i]//100)%10
    # b=(a[i]//10)%10
    # c=(a[i]//100)%10
    # print(c,b,rev)
for i in range(length):
    temp=str(a[i])
    if temp[0]=="1":
        print("true")
    else:
        print("false")
    # i+=1
    

