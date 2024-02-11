#1
from datetime import datetime, timedelta
curr = datetime.today()

print(curr - timedelta(days=5))

#2
today = datetime.today()
yesterday = datetime.today() + timedelta(days = 1)
tomorrow = datetime.today() - timedelta(days = 1)
print(yesterday)
print(today)
print(tomorrow)
 
#3
d = datetime.today().replace(microsecond=0)
print(d)
 
#4
d1 = datetime(2020, 5, 17)
d2 = datetime(2020, 12, 22)

if(d1 > d2):
    print((d1-d2).total_seconds())
else:
    print((d2-d1).total_seconds())






