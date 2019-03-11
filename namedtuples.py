from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(dot_product)


Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
xyz = Car(Price = 20000, Mileage = 6000, Colour = 'Red', Class = 'X')

n = int(input())
ssheet = input().split()
markidx = ssheet.index('MARKS')
print('%.2f' % sum([int(ssheet[i]) for i in range(markidx + 4,len(ssheet), 4)]) / n)



   


