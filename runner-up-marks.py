student_marks = {}
line = "25 50 60".split()
scores = list(map(float, line))

line1 = "45 90 57".split()
scores1 = list(map(float, line))

student_marks['malika'] = scores
student_marks['karthi'] = scores1

print(student_marks)
student_marks = student_marks
print("{0:.2f}".format([sum(student_marks[a]) / len(student_marks[a]) for a in student_marks if a == 'karthi'][0]))