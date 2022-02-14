# hackerrank question number10 of doc-
# find the difference of diagonals.
l=[[1,2,3],
   [4,5,6],
   [9,8,9]]
i=0
j=0
add1=0
while i<len(l):
    print(l[i][j])
    add1=add1+l[i][j]
    j+=1
    i+=1
k=0
m=len(l)-1
add=0
while k<len(l):
    print(l[k][m])
    add=add+l[k][m]
    k+=1
    m-=1
print(add)
print(add1)
print(add-add1,"difference")
