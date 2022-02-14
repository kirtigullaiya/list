# function question3 doc.
a=[8,2,3,0,7]
i=0
add=0
while i<len(a):
    add=add+a[i]
    i+=1
print(add)

# reverse the string. function question 4 doc.
a="1234abcd"
b=""
i=0
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
print(b)

# duplicate function question5 doc.
a=[1,2,3,3,3,3,4,5]
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)

# even numbers from list function question6 doc.
a=[1,2,3,4,5,6,7,8,9]
b=[]
i=0
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    i+=1
# print(b)

# count of uppercase and lowercase letters function question8 doc.
string="The quick Brow Fox"
i=0
count=0
count1=0
while i<len(string):
    if string[i]>="A" and string[i]<="Z":
        count+=1
    elif string[i]>="a" and string[i]<="z":
        count1+=1
    i+=1
print("count of uppercase letters:",count)
print("count of lowercase letters:",count1)

# question9 of function of doc.
b=[]
i=1
while i<=30:
    if i==1 or i==2 or i==3 or i==4 or i==5 or i==30 or i==29 or i==28 or i==27 or i==26 or i==25 :
        square=i**2
        b.append(square)
    i+=1
print(b)


# question10 function of doc.
a=input("please enter number:")
b=input("please enter number:")
i=0
sum=0
sum=sum+int(a)
total=str(sum+int(b))
print(total)
total+="5"
# print(total)


