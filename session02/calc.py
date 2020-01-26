#1. The volume of a sphere with radius r is (4/3)\pi r^3.
# What is the volume of a sphere with radius 5?
def sphere_volume(r):
    v = (4 / 3) * 3.14159 * r ** 3
    print(f'The volume of a sphere with radius {r} is {v}')

sphere_volume(5)

#2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?
def wholesale_cost(x):
    c = (24.95 * 0.4) * x + 3 + 0.75 * (x-1)
    print(f'The total wholesale cost for {x} copies of the book is {c}')

wholesale_cost(60)

#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
# what time do I get home for breakfast?
easy_pace = 8 + 15/60
tempo = 7 + 12/60
total_time = 2 * easy_pace + 3 * tempo
start_time = 6 * 60 + 52
end_time = start_time + total_time
end_time_hr = end_time // 60
end_time_min = end_time % 60
print(f'I will get home at {end_time_hr:.0f}:{end_time_min:.0f} am for breakfast')

#4. If my average grade rises from 82 to 89. What is the percentage of the increase? 
# Format the result as 'xx.x%'. Keep one figure after decimal point.
percent_increase = (89 - 82) * 100 / 82
print(f'The percentage of the increase from 82 to 89 is {percent_increase:.1f}%')
