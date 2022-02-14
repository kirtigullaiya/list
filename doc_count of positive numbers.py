a=[2,-7,5,-64,-14]
i=0
count=0
count1=0
while i<len(a):
    if a[i]>0:
        print("positive numbers:",a[i])
        count+=1
    else:
        print("negetive numbers:",a[i])
        count1+=1
    i+=1
print("total count of positive numbers::",count) 
print("total count of negetive numbers::",count1)   



