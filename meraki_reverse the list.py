places=["delhi","gujrat","rajasthan","punjab","kerala"]
a=len(places)
i=0
while i<=1:
    n=places[i]
    places[i]=places[a-i-1]
    places[a-i-1]=n
    i+=1
print(places)

# same question in for loop:-
# places=["delhi","gujrat","rajasthan","punjab","kerala"]
# a=len(places)
# for i in range(1):
#     n=places[i]
#     places[i]=places[a-1]
#     places[a-1]=n
#     print(places)