import time
import pprint

# pprint.pprint(dir(time))
timenow = time.localtime()
# print(type(time))

year = timenow.tm_year
month = timenow.tm_mon
day = timenow.tm_mday
hour = timenow.tm_hour
minute = timenow.tm_min
second = timenow.tm_sec

print(f'The current time is {year}/{month}/{day} {hour}:{minute}:{second}')

day_past_epoch = time.time() / 60 / 60 / 24
print(f'The number of days since the epoch is {day_past_epoch:.0f}')











