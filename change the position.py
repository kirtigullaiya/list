

l=[11,33,50]
string=""
i=0
while i<len(l):
    string+=str(l[i])
    i+=1
print(string)

words=["ask","be","call","do","come","find","use","feel"]
i=0
while i<len(words):
    j=0
    count=0
    while j<len(words[i]):
        if words[i][0]>="a" and words[i][0]<="z":
            print(words[i][0],"word-",words[i])
        count+=1
        j+=1
    i+=1
    # count+=1
# print(words[i][0],"word-",words[i])
print(count)
