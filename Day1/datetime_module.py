import datetime

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)

d = datetime.datetime(2006,10,26)
delta = datetime.timedelta(days=30)
print(d + delta)