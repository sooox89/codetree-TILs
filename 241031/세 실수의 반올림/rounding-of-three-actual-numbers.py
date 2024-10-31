import sys

data = [float(sys.stdin.readline()) for i in range(3)]

for i in data:
    print("%0.3f"%round(i,3))