import sys
n,k = map(int,input().split())
data = list(map(int,sys.stdin.readline().split()))
data.sort()

print(data[k-1])