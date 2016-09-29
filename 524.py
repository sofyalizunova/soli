__author__ = 'student'
A=input().split()
m=0
for i in A:
  k=A.count(i)
  if k>m:
      m=k
      s=i
print(s)

