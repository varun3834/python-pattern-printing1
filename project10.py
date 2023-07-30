Limit=int(input('limit of numbers: '))+1
r=0
Last=0
while Last<=Limit:
    if Limit in range(Last,r+Last) :
        x=range(Last,Limit)
        for n in x:
            print(n,end=" ")
        print()
    else:
        Range=range(Last,r+Last)
        for n in Range:
            print(n,end=" ")
        print()
    Last=r+Last
    r+=1
