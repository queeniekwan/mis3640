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

day_past_epoch = time.time() // 60 // 60 // 24
print(f'The number of days since the epoch is {day_past_epoch:.0f}')

# method 2
current = time.time()
second2 = current % 60
minute2 = current // 60 % 60
hour2 = current // 60 // 60 % 24
day2 = current // 60 // 60 // 24

print(f'CURRENT TIME: {int(day2)} days, {int(hour2)} hours, {int(minute2):d} minutes, {int(second2)} seconds past the epoch')















