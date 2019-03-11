students = list([['Harry', 37.21], ['Berry', 37.21], ['Tina', 39], ['Akriti', 41], ['Harsh', 39]])


marks = []
names = []
for st in students:
    marks.append(st[1])

mMax = max(marks)
v = 0
while v < len(marks):
    if marks[v] == mMax:
        marks.pop(v)
    v = v+1

secondMarks = max(marks)

secondRankStudents = []
for st in students:
    if st[1] == secondMarks:
        names.append(st[0])


print(names.sort())
