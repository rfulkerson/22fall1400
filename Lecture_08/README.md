# Lecture 08, September 19th, 2022

## In-class Errata / Discussion

In today's class, we focused on introducing relational operators into our repertoire of operators. We introduced equality `==` and inequality `!=` in our [last lecture](../Lecture_07). Now we have less than `<`, less than or equal to `<=`, greater than `>`, and greater than or equal to `>=` to work with.

These operators allow us to test for ranges of values. Since, in this lecture, we don't have logical operators yet, we can test for ranges of values using just single conditions in a [cascaded `if`/`elif`/`else` structure](https://kodify.net/python/if-else/cascaded-if/). Or we can utilize [chained operators](https://www.geeksforgeeks.org/chaining-comparison-operators-python/) to test ranges, also.

We demonstrated this in our [highlights.py](highlights.py) code, which implemented a speeding ticket calculator. Both the cascading if/else and chained operator versions are present in the code, and both have their plusses and minuses. Our discussion focused around the simplicity and consistency of the cascading if/else using the same test (less than) for all tests and investigating how in a cascading if/else, if one range test fails then the number being tested must meet a certain threshold. 

For example, if the test `speed < 40` fails, we know that `speed` must be 40 or above, which we can feed into another test to cap the range of values for `speed`.  See the code in [highlights.py](highlights.py) to refresh yourself on the tests that were written. 

Using a chained operator condition such as `40 <= speed <= 60` allows you to more readily see the exact range of values being tested (as opposed to having to keep track of what values failed in a previous test to know where part of the range lies), but may result in some uses of other operators like `>=`, which leads to inconsistency in testing, i.e. some tests use less than while some use greater than.

Ultimately, if the code works correctly, that's a win. But we want to make legible, readable, maintainable code. For some, that might be using the cascading if/else structure with simple conditions and for others that might be using the cascading if/else structure with chained operator conditions. As long as you find oe approach that works for you and you keep consistently using that approach, that's probably acceptable unless there are specific requirements for the code.

Most of our discussion focused on the code found in [Q3.py](Q3.py) and determining which range of values would output `Hello`, `Goodbye` and `What's up?`. The code in [Q3.py](Q3.py) is not well-written code by any stretch of the imagination but illustrates the potential difficulties in mixing and matching operators in tests (`x >= 0` and `x < 20`) and using single conditions to test ranges.

```python
x = int(input())
if x >= 0:
   print("Hello")
elif x < 20:
   print("Goodbye")
else:
   print("What's up?")
```

* All non-negative values `x >= 0` will trigger `Hello` being output.
* If that test fails, then we _know_ that `x` must be negative and despite the test in the next `elif` being for `x < 20`, only negative values will output `Goodbye`. So the test succeeds but not for the values listed in the condition itself (i.e., 15 is less than 20 but is caught by the first test).
* The text `What's up?` will never be reached because every possibly numeric value is handled by the first two conditions.

The last question, [Q8.py](Q8.py) is a sequential series of `if`/`elif` and `if`/`else` structures. It mostly works correctly for pringing what are essentially letter grades A through F, but will always print a trailing `Z` if the grade is A, B, C, or D because of the last `if`/`else`.

## The topics for this lecture were:

* Detecting ranges with branches
	- Relational operators
	- Detecting ranges with `if`-`elif`-`else` statements
	- Operator chaining


## The highlighted topics for this lecture were

* Detecting ranges with branches (general)
	- Relational operators
	- Multi-branch `if`/`elif`/`else` to detect ranges

* Detecting ranges with branches
	- Relational operators `<`, `>`, `<=`, `>=`
	- Detecting ranges with `if`-`else` branches
	- Operator chaining

## Music played at the beginning of class

* [Head Cheerleader](https://www.youtube.com/watch?v=6clF3e1m80U) by Pom Pom Squad
* [Black Sheep](https://www.youtube.com/watch?v=1xcSDYy3Dl4) by Metric (feat. Brie Larson)
* [Wish I Knew You](https://www.youtube.com/watch?v=o0Pt7M0weUI) by The Revivalists
* [Living in the Past](https://www.youtube.com/watch?v=m__wmsIn99E) by Jethro Tull
