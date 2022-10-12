# Lecture 15, October 12, 2022

## In-class Errata / Additional Discussion

For today's class, we looked more at the `for` loop and investigated how to use the very versatile `range()` function. We also looked at nested loops (loops within loops).

To start with, we wrote the code in [highlights.py](highlights.py), which finds all Pythagorean triples that satisfy $a^2 + b^2 == c^2$.  This required three nested loops, which can be seen in the code.

Each loop uses the `range(1,501)` function to test numbers from 1 to 500.  So if we have three nested loops, the innermost `if` conditional test will execute $500^3$ times, or 125,000,000 times.

I added some time code to the program we wrote to test how long it took to test and output 125,000,000 combinations of a, b, and c. On my computer, it took about 91 seconds to test all 125,000,000 combinations and find 772 Pythagorean triples.

We then applied this to having a password and trying to guess the password.

We set up four nested loops and then five, all using a source string of characters to test.  In the version that is found here, [password_equals.py](passwordequals.py), the source string has 53 characters (lowercase letters, uppercase letters, and an exclamation point). This amounts to $53^5$ possibile combinations which is 418,195,493 passwords.  Nearly three times as many combinations as what we were trying with 3 nested loops for the previous example.

When run, it takes only 25.62 seconds on my machine to find `JeFf!`, the password, and a total of only 75.35 seconds to test all 415 million possibilities.

### Code execution time comparison
How can it be that testing 415 million possibilities takes less time than 125 million possiblities? If you look at the action inside the loops, the "work" being done to guess passwords is straightforward and not very time-consuming:

1. Build a password with `guess = f'{a}{b}{c}{d}{e}'`
2. Test that password with an equality test `if guess == password`

With the Pythagorean triples, however, the "work" at the innermost portion of the loop looks like this:

1. `if a ** 2 + b ** 2 == c ** 2`.  

Even though it's also "just" a test, there's a lot more work happening here arithmetically, and it's the exponentiation of each variable and then the test that's taking the extra time for only one third of the tests.  Very interesting!

----

We then took a look at some Peer Instruction questions and worked through some stuff with `range()`.  For [Q1.py](Q1.py) and [Q2.py](Q2.py), it was pretty clear what the output would be.

When introducing the step argument (which I consistently yet inaccurately called the stride, my apologies), that gave us a little bit of pause in [Q3.py](Q3.py), [Q4.py](Q4.py), and [Q5.py](Q5.py).  Just remember that in a `for` loop, the `range(start,end,step)` function will always produce valid values to process as long as `start`, `end`, and `step` are all congruent.  Meaning that if the `start` is `1` and the `end` is `8`, the `step` needs to be a positive number to get you from `start` to `stop`, such as `range(1,8,2)`.  If the `start` is `10` and the `end` is `-5` (i.e., setting up a descending loop), then the `step` needs to be negative to get you from `start` to `stop`.  If the `start`, `end`, and `step` are incongruent, no range is produced, like:

```python
print(list(range(1,15,2)))  # [1, 3, 5, 7, 9, 11, 13]
print(list(range(1,15,-2))) # []
```

---

Some other random observations from all questions, including [Q8.py](Q8.py):

1. If you have a list to process, you can use the `len()` function as the argument to `range()` to give you an accurate loop of valid indices to process in the list. In the following example, the range for `pos` would run from `0` through `5` because `len(my_list)` will return `6`.

	```python
	my_list = [5, 10, 15, 20, 25, 30]
	for pos in range(len(my_list)):
		print(my_list[pos], end=" ")
	```
2. You can access items from the back of a list using negative indexing, as seen in [Q5.py](Q5.py).  So the following would print the last two elements of the list:

	```python
	my_list = [5, 10, 15, 20, 25, 30]
	print(my_list[-2])
	print(my_list[-1])
	```

## Music played at the beginning of class

* [Surface Pressure](https://www.youtube.com/watch?v=tQwVKr8rCYw) from "Encanto" (Jessica Darrow)
* [Singin' in the Rain](https://www.youtube.com/watch?v=swloMVFALXw) from "Singin' in the Rain" (Gene Kelly)
* [City of Stars](https://www.youtube.com/watch?v=VFUos9sYbHs) from "La La Land" (Ryan Gosling and Emma Stone)
* [You're the One That I Want](https://www.youtube.com/watch?v=itRFjzQICJU) from "Grease" (Olivia Newton-John and John Travolta)
* [My Beloved Monster](https://www.youtube.com/watch?v=FKcFAihjzck) from "Shrek" (Eels)


## The topics for this lecture were:

* `range()`
	* start
	* end
	* increment value / stride
* `while` vs `for`
* Nested loops


## The highlighted topics for this lecture were

* `for` loop revisited
* `range()`
* `range(x)`
* `range(x, y)`
* `range(x, y, z)`

* Any counter-controlled while loop can be rewritten as an equivalent for loop.

* Nested loops
	* Outer loop
	* Inner loop
