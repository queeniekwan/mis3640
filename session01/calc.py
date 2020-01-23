# 1. How many seconds are there in 42 minutes 42 seconds?
a = 42 * 60 + 42
print(a)


#2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
b = 1.6 * 10
print(b)

#3. If you run a 10 kilometer race in 42 minutes 42 seconds, 
# what is your average pace (time per mile in minutes and seconds)? 
# What is your average speed in miles per hour?
pace_sec = a / b
pace_min = pace_sec / 60
speed_hr = 1 / (pace_min / 60)

print('pace in second', pace_sec)
print('pace in minute' , pace_min)
print('speed in hour' , speed_hr)

