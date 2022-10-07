# Given the following two sets of friends, find:

# All the friends (union)
# The friends that are common to both groups (intersection)
# The friends only in group_1 (difference)
# The friends only in group_2 (difference)
# The friends unique to both groups (symmetric_difference)

group_1 = {"Nichole", "Tyreese", "Mustafa", "Aliza"}
group_2 = {"Aliza", "Nichole", "Judah", "Toby", "Vikki"}
print(group_1)
print(group_2)
print()

all_friends = group_1.union(group_2)
print(all_friends)
print()

in_both_groups = group_1.intersection(group_2)
print(in_both_groups)
print()

only_in_g1 = group_1.difference(group_2)
print(only_in_g1)
print()

only_in_g2 = group_2.difference(group_1)
print(only_in_g2)
print()

in_g1_or_g2 = group_2.symmetric_difference(group_1)
print(in_g1_or_g2)
print()

other = group_2.union(group_1).difference(group_2.intersection(group_1))
print(other)
print()

