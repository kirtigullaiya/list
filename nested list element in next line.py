# nested list elements in next line.
a=[["red"],["black"],["green"]]
b=[]
i=0
while i<len(a):
    print(a[i],"\n")
    i+=1

# convert a string into list.
string=input("please enter string:")
a=[]
i=0
while i<len(string):
    j=0
    while j<len(string[i]):
        a.append(string[i][j])
        j+=1
    i+=1
print(a)