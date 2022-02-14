# numbers=[50,40,23,70,56,12,5,10,7]
# index=0
# for i in numbers:
#     print(i)
# print("maximum number=",max(numbers))

numbers=[10,20,30,66,99,1,2,5,56]
max=0
for i in numbers:
    if max<i:
        max=i
print("maximum number is-",max)

i=0
while i<len(numbers):
    if max<numbers[i]:
        max=numbers[i]
    i+=1
print(max)


