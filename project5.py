a=int(input('count no of length: '))
i=1
while i<=a:
  s=(a-i)*2
  if(a==i):
      print('*'*(i-1)+" "*(s-1)+'*'*i)
  else:
       print('*'*i+" "*(s-1)+'*'*i)

  i+=1
i=a
while i>1:
  i-=1
  s=(a-i)*2
  print('*'*i+" "*(s-1)+'*'*i)  