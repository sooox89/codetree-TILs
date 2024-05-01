import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
A.sort()
B.sort()
for i in range(n):
    if(A[i]!=B[i]):
        print("No")
        break
    if(i==n-1):
        print("Yes")
    pass