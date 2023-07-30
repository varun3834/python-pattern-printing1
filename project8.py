star=int(input('count no of length: '))
counter = 0
while counter<star:
    print(" "*(star-counter-1)+ "* "*(counter+1)+" "*(star-counter-1))
    counter= counter+1

counter = star -2
while counter>=0:
    print(" "*(star-counter-1)+ "* "*(counter+1)+" "*(star-counter))
    counter= counter-1