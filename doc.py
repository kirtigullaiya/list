

a=[1234,122,1984,19372,100]
length=len(a)
for i in range(length):
    rev=a[i]%10
    a[i]=a[i]//10
    print(rev)