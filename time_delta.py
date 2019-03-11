import datetime

t1 = 'Sat 02 May 2015 19:54:36 +0530'
t2 = 'Fri 01 May 2015 13:54:36 -0000'

print(int(abs(datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z') - datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')).total_seconds()))


print(t1)
print(t2)


