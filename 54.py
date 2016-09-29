__author__ = 'student'
s=list(map(int, input().split()))
t=int(input())
for i in range(t):
    s.insert(len(s)-s[-1]-1,s[-1])
    s.pop()
print(' '.join(map(str, s)))
