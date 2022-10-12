# Find and output all Pythagorean triples where a, b, and c range from 1 through 5.

# Remember that a Pythagorean triple satisfies the condition:𝑎^2+𝑏^2=𝑐^2

# How could you modify the code to test larger ranges?
# Modify the code to test ranges based on user input.

import time

howmany = 0

start = time.perf_counter()

for a in range(1,501):
    for b in range(1,501):
        for c in range(1,501):
            if a ** 2 + b ** 2 == c ** 2:
                print(f"a is {a} and b is {b} and c is {c}")
                howmany += 1

end = time.perf_counter()
print(f"Found {howmany} triples in {end-start:.2f} seconds! How amazing!")