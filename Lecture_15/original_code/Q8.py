# What would the first line that is printed by the following code be?
nums = [5, 4, 8]
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i] * nums[j], end=' ')
    print()
