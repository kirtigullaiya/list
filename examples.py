# i=2
# for i in range(2,21,2):
#     print(i)
# else:
#     print("program terminated")

# for i in range(1500,2700):
#     if i%7==0 and i%5==0:
#         print(i)
# print("that's it.")


# maximum value till index.output-[3,3,3,6,9,9]
a=[3,1,-4,6,9,2]
max=0
m=[]
i=0
while i<len(a):
    if max<a[i]:
        max=a[i]
    m.append(max)
    i+=1
print(m)