list=[23,14,56,12,19,9,15,25,31,42,43]
sum=0
sum1=0
count=0
count1=0
for i in range(len(list)):
    if list[i]%2==0:
        print(list[i],"::even")
        sum+=list[i]
        count=count+1
        # print("count of even numbers::",count)
        i+=1
        avg=sum/count
        # print(avg)
        # print(sum,"sum")
    else:
        print(list[i],"::odd")
        sum1+=list[i]
        count1+=1
        # print("count of odd numbers::",count1)
        i+=1
        avg1=sum1/count1
        # print(avg1)
print("count of even numbers::",count)
print("count of odd numbers::",count1)
print(sum1,"sum of even numbers")
print(sum,"sum of odd numbers")
print("avg of even numbers::",avg)
print("avg of odd numbers::",avg1)

