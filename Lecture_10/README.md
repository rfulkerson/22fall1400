# Lecture 10, September 26, 2022

## In-class Errata / Additional Discussion

Class was canceled due to illness.

I did just want to draw your attention to one of the questions, [Q3.py](Q3.py), which you should have encountered in your replacement Progress Check that you took in Canvas. 

This questions addresses the concept that you shouldn't use equality `==` to try and test floating point values.

The code is:

```python
x = float(input("Enter pi: "))
if x == 3.14:
    print("We've got pi!")
```

Entering `3.14` for `x` will result in the test successfully completing. So it's tough to demonstrate that there are times when it won't work. Here's an example value that would cause the test to succeed even though the values are not the same:

```python
3.1400000000000001
```

If that was the input, the result would come back with a True execution of the conditional test and it would output `We've got pi!`.

[Here's a more detailed explanation](https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch07s02.html) of floating point equality testing if you're interested. Where we're headed is testing the absolute value of the differences of two numbers being less than an acceptable threshold. This is usually done when there have been calculations that generate floating point values.

## The topics for this lecture were:

* Comparing Data Types
* Common Errors
* Expanded Order of Evaluation
* Conditional Expressions


## The highlighted topics for this lecture were

* Comparing data and common errors
	- Comparing integers
	- Comparing Strings
	- Comparing floating-point types
	- Comparing disparate data
	- Common syntax errors (=, =>, etc)

* Conditional expressions
	- true_value `if` condition `else` false_value

* Order of evaluation
	- Precedence rules
	- `()`
	- `*` `/` `%` 
	- `+` `-`
	- `<` `<=` `>=` `==` `!=`
	- `not`
	- `and`
	- `or`
