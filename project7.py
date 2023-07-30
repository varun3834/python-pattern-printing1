star=int(input('count no of length: '))
counter = star
while counter>=0:
    print(" "*(star-counter)+ "* "*(counter+1)+" "*(star-counter))
    counter= counter-1