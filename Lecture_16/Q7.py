# What does this code do?

numbers = [-3, 6, 0, -5, 11, 9]
this_one = numbers[0]
this_index = 0
for (pos, num) in enumerate(numbers):
    if pos > this_index:
        this_one = num
        this_index = pos
print(this_index, this_one)

