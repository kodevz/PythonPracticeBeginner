from collections import Counter

mylist = '2 3 4 5 6 8 7 6 5 18'
mylist = list(map(int,mylist.split(' ')))
mylist = Counter(mylist)
noofcust = 6
totprize = 0


while noofcust != 0:
    
    size, price = map(int, input().split())
    if mylist[size]:
        print(mylist)
        mylist[size] -= 1
        noofcust -= 1
        totprize +=price
    print(totprize)

    
   
    
    
