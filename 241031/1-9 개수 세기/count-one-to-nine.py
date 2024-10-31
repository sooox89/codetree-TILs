n = int(input())

data =list(map(int,input().split()))

count = [0 for i in range(9)]

for i in data:
    count[i-1] += 1
for i in count:
    print(i)