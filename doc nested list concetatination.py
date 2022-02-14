# concatenate element wise three given lists.
a=["0","1","2","3","4"]
b=["red","green","black","blue","white"]
c=["100","200","300","400","500"]
d=[]
i=0
while i<len(a):
    add=a[i]+b[i]+c[i]
    d.append(add)
    i+=1
print(d)