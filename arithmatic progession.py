# Write a Python program to generate a list of numbers in the arithmetic
#  progression starting with the given positive integer and up to the specified limit. 
size=int(input("plaese enter:"))
num=int(input("please enter number:"))
a=[]
i=1
while i<=size:
    # num=int(input("please enter number:"))
    table=num*i
    a.append(table)
    i+=1
print(a)

        
