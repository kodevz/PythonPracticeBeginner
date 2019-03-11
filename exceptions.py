
n = int(input())

while n != 0:
    a , b = input().split(' ')
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
    n -= 1
