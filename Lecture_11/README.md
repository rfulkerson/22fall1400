# Lecture 11, September 28, 2022

## In-class Errata / Additional Discussion

There were some good discussions today.

We started off by writing a [highlights.py](highlights.py) file that implemented three counter-controlled loops and a sentinel-controlled loop for data validation. The code wasn't fancy, but accomplished the task of doing counter-controlled looping as well as using a sentinel-controlled loop for data validation.

Sentinel-controlled loops, in general, operate on the principle of entering good data and then processing it and continuing to enter data until a bad value is entered:

```python
total = 0
grade = int(input("Enter a grade to process: "))

while grade >= 0:
    total += grade
    grade = int(input("Enter a grade to process: "))

print("The total of all grades is:", total)
```

Data validation loops, a subset of sentinel-controlled loops, work on the opposite premise: the loop continues while you keep entering bad values. The value that allows you to exit the data validation loop will be a _good_ value.

```python
weight = float(input("Enter a weight greater than 0: "))

while weight <= 0:
    weight = float(input("Enter a weight greater than 0: "))

print("The weight you entered, which is definitely bigger than 0, is:", weight) 
```

-----

There was another worked example, [highlights2.py](highlights2.py), which we didn't quite get to. The purpose of that one is to implement a guessing game. It's left unfinished in the file here so you can write it if you want to for practice.

----

We then had some good discussions about our Poll Everywhere questions.  [Q1.py](Q1.py) asked about how many times a loop would execute. Everyone answered either 11 or 12 based on the code, which was expected. When trying to determine how many times a counter-controlled loop will execute, just make sure to look at the initial value, the final value for testing, and the operator being used to test fo the final value.  In the Q1 example, the initial value was 0, the test was `x <= 11` and the modifcation was `x += 1`.  So it runs from 0 through 11, inclusive, which is 12 times.

----

We had a brief discussion about overflow / underflow (when a number becomes so small or large that it wraps around. I think I misspoke in class because integer values don't typically have hard limits, but floating point values do. Run this code in Thonny to test it that I culled from [https://stackoverflow.com/questions/52151647/integer-overflow-in-python3](https://stackoverflow.com/questions/52151647/integer-overflow-in-python3) and [this brief explanation at python.org](https://docs.python.org/3/library/exceptions.html#OverflowError):

```python
import sys

i = sys.maxsize
print(i)
# 9223372036854775807
print(i == i + 1)
# False
i += 1
print(i)
# 9223372036854775808

f = sys.float_info.max
print(f)
# 1.7976931348623157e+308
print(f == f + 1)
# True
f += 1
print(f)
# 1.7976931348623157e+308
```

----

We discussed what good sentinel values are for [Q3.py](Q3.py). Because the question asked about numeric input for quilt squares, the best option is an impossible integer value size for quilt squares:

```python
size = int(input("enter quilt square size: "))

while size >= 0:
    total += size
    size = int(input("enter quilt square size: "))
```

But arguments _could_ be made for the word `done` or `q` if you did the numeric casting inside the loop:

```python
size = input("enter quilt square size: ")

while size != "done":
    total += int(size)
    size = int(input("enter quilt square size: "))
```

The only problem with this is if you allow textual input and you try to cast it as an integer inside the loop, without proper precautions (which we don't have yet) the code will crash.  So if someone entered `seventeen`, the code would crash trying to cast it with `int()`.

-----

Then in [Q4.py](Q4.py) and [Q5.py](Q5.py) we looked at sentinel-controlled loops that had the same input but produced different results. Q4.py had the correct code, which has the structure of:

* prime the loop with initial value for loop control variable
* while the loop control value hasn't been entered:
	* process the value in whatever fashion makes sense
	* read another value for the loop control variable and then end the loop, to go back to test again.

In Q5, the order of statements inside the loop were reversed, which means that if you enter the loop with a valid value, you immediately throw it away because you read a new value. Then you process that value without testing it for validity and _then_ end the loop and test again.
     
## Music played at the beginning of class

* [The Moladu](https://www.youtube.com/watch?v=l6kqu2mk-Kw) by Smetana, performed by Gimnazija Kranj Symphony Orchestra
* [Song Up In Her Head](https://www.youtube.com/watch?v=kdM89_88cdM) by Sarah Jarosz

## The topics for this lecture were:

* Loop body
* Iteration
* while condition: 
	- statement1
	- statement2

## The highlighted topics for this lecture were

* while loop
* Loop body
* Iteration

* Counter-controlled loop
* Sentinel-controlled loop
* Sentinel value

* Infinite loop
* Pre-test loop

* Requirements for looping:

	1. Loop Control Variable (LCV)
	2. Initial value for the LCV
	3. Modification of the LCV
	4. Test for the final value of the LCV
