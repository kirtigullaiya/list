# a=[1,2,3,4]
# b=[5,6,7,8]
# i=0
# while i<len(b):
#     a.append(b[i])
#     i+=1
# print(a)

# check two lists are circularly identical.
a=[10,10,0,0,10]
b=[10,10,10,0,0]
c=[1,10,10,0,0]
i=0
while i<len(b):
    if a[i] in b:
        # print(True)
        i+=1
print(True)
i=0
while i<len(c):
    if a[i] in c:
        # print(False)
        i+=1
print(False)

