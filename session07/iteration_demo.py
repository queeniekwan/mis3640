# for loop
current_sum = 0

for i in range(0, 101, 2):
    print(f'The value of i is {i}')
    current_sum = current_sum + i
    print(f'Currently, the sum is {current_sum}')
    print()

# while loop 1
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

# countdown(10)

# while loop 2
iteration = 0 
count = 0
while iteration < 5:
    for letter in 'hello, world':
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration +=1

# break - break out of the for loop completely 
iteration = 0
while iteration < 5:
    count = 0
    for letter in 'hello, world':
        count += 1
        if iteration % 2 == 0:
            break
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1

# continue - skip the remaining lines of current iteration and start the next iteration
for i in range(10):
    print(i)
    if i == 5:
        break

for i in range(4):
    print(i)
    if i >= 2:
        continue
    print(i * i)
    print()



