from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(dot_product)


Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
xyz = Car(Price = 20000, Mileage = 6000, Colour = 'Red', Class = 'X')


s = """ ID         MARKS      NAME       CLASS     
    1          97         Raymond    7         
    2          50         Steven     4         
    3          91         Adrian     9         
    4          72         Stewart    5         
    5          80         Peter      6  """
        
print(s)

ind=(input().split()).index('MARKS')
print(ind)
n = 2
stud = []
Student = namedtuple('Student','Ids Marks Name Class')
for i in range(n):
    ids, marks, clas, name = input().split(' ')
    stud.append(Student(Ids = int(ids), Marks = int(marks), Name = name, Class = int(clas)))

print(sum([stud[i].Marks for i in range(len(stud))]) / 2)
