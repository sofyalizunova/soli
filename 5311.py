__author__ = 'student'
A=input().split()
for i in range(0,len(A)//2):
      print(A[i]+' '+A[-i-1], end=" ")
if len(A)/2!=0:
  print(A[len(A)//2])

