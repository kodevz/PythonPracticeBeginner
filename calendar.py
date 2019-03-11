import calendar
month,day,year = '08 05 2015'.split(" ")
ans = calendar.weekday(int(year), int(month), int(day))
print(calendar.day_name[ans])