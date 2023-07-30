# p1= open("/home/varun/Documents/study/code/29-7-2023/project2.py","r")
# p2= open("/home/varun/Documents/study/code/29-7-2023/project3.py","r")
# print(p1)
# print(p2)

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