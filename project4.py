a=int(input('count no of length: '))
i=0
while i<a:
  i+=1
  s=a-i
  print(" "*s,'*'*i)

i=a
while i>0:
  i-=1
  s=a-i
  print(" "*s,'*'*i)
