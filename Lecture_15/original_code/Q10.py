# What would the second line that is printed by the following code be?
nums = [5, 4, 8]
nums2 = [1, 3]
for i in range(len(nums)):
    for j in range(len(nums2)):
        print(nums[i] * nums2[j], end=' ')
    print()
