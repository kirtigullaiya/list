# take those last digit of numbers's square which are even and put them in a list.
l=[123,46,89,4324,89]
i=0
l1=[]
while i<len(l):
    d=l[i]%10
    if d%2==0:
        square=d**2
        l1.append(square)
    i+=1
print(l1)