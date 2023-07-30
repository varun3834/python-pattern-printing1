Limit=int(input('count no of length: '))
r=0

while r<=Limit:
    Range=range(r+1)
    for n in Range:
        print(n,end=" ")
    print()
    r+=1
