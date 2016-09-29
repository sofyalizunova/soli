__author__ = 'student'
A=input().split()
for i in range(0,len(A)//2):
        A[i],A[-1-i]=A[-1-i],A[i]
print(' '.join(map(str, A)))
