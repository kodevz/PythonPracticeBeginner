import itertools
s = 'fedcbabcd'
scollect = []
for c in itertools.permutations(s):
    scollect.append(c)

print(scollect)
print(*sorted(scollect)[1],sep="")


    


