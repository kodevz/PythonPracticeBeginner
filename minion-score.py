string = 'AABCAAADA'
k = 3
for part in zip(*[iter(string)] * 3):
    d = dict()
    print(''.join([d.setdefault(c,c) for c in part if c not in d]))



    
