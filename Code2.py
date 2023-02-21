inp=list(input("Enter a string: "))
nrp=[]
for i in range(len(inp)):

    if inp[i] not in nrp and chr(ord(inp[i])+32) not in nrp and chr(ord(inp[i])-32) not in nrp:
        if inp[i]==" " :
                continue
        else:
            nrp.append(inp[i])
a=""
for i in range(len(nrp)):
    a+=nrp[i]

print(a)
