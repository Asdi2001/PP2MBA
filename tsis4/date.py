#1
import datetime
today = datetime.datetime.now()
substract= today - datetime.timedelta(days=5)

print(substract)

#2
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)

#3
import datetime
now = datetime.datetime.now().replace(microsecond=0)

print(now)

#4
import datetime
date1 = datetime.datetime(2024, 3, 21, 14, 18, 0)
date2 = datetime.datetime(2024, 3, 18, 8, 0, 0)
diff = (date1 - date2).total_seconds()

print(diff)
