from collections import defaultdict

n, m = list(map(int, input().split(" ")))


A=defaultdict(list)
for i in range(n):
    A[input()].append(str(i+1))

for i in range(m):
    print(' '.join(A[input()]) or -1)

