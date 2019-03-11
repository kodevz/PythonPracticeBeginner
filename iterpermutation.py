from itertools import permutations
string,k = input().split()
[print("".join(i)) for i in sorted(list(permutations(string,k)))]