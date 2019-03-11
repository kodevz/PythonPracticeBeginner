n,m = map(int, input().split())
S = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum([(i in A)-(i in B) for i in S]))


