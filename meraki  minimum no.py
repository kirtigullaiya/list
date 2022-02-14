numbers=[10,20,30,66,99,1,2,5,88]
min=numbers[0]
for i in numbers:
    if min>i:
        min=i
print("minimum number is -",min)
numbers.sort()
print(numbers)
print(numbers[-2])