# Write a Python program to get the every nth element in a given list
# w3 recources q269.
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=int(input("plaese enter number:"))
b=[]
i=0
while i<len(a):
    if i==n:
        pass
        n+=n
    else:
        b.append(a[i])
    i+=1
print(b)