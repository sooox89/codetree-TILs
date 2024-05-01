import sys
arr = str(sys.stdin.readline())
arr = list(arr)
arr.sort()

sorted_str = ''.join(arr)
print(sorted_str)