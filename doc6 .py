a=[34.67,12,-94.89,"python",0,"c#"]
b=[]
i=0
while i<len(a):
    if type(a[i])==int:
        b.append(a[i])
    i+=1
print(b)

a=input("please enter")
i=0
string=""
while i<len(a)-1:
    string=string+"+"+a[-i]
    i+=1
print(string)
