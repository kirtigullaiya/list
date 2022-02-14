binary=[1,0,1,1]
a=len(binary)
i=1
j=0
total=0
while i<len(binary)+1:
    b=binary[-i]*2**j
    total=total+b
    j+=1
    print(b)
    i+=1
print("the decimal number is-",total)