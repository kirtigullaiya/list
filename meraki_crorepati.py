kitna_paisa_hai=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
a=[]
b=[]
c=[]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        print("index::",i,"::","crorepati")
        a.append(kitna_paisa_hai[i])
        # count+=1
        i+=1
    elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<=9999999:
        print("index::",i,"::","lakhpati")
        b.append(kitna_paisa_hai[i])
        i+=1
    else:
        print("index::",i,"::","dilwale")
        c.append(kitna_paisa_hai[i])
        i+=1
print(a,"::crorepati")
print(b,"::lakhpati")
print(c,"::dilwale")
