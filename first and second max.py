num=[10,20,30,66,99,1,2]
i=0
max=0
max1=0
while i<len(num):
    if num[i]>max:
        max=num[i]
    i=i+1
print("First maximum number is-",max)
i=0
while i<len(num):
    if num[i]>max1:
        if num[i]!=max:
            max1=num[i]
    i=i+1
print("Second maximum number is-",max1)