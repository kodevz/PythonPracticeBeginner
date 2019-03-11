n = 5 #Total no of pages
p = 1 #To be find page number

pages = [p for p in range(1, n + 1 )]
mincnt = 0


mincnt = 0
for i in pages:
    mincnt += 1/2
    if i == p:break

maxcnt = 0
for i in pages[::-1]:
    maxcnt += 1/2
    if i == p:break

print(0 if int(mincnt) == 1 else int(mincnt))
print(0 if int(maxcnt) == 1 else int(maxcnt))
