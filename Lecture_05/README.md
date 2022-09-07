# Lecture 05, Wednesday, September 7th, 2022

## In-class Errata / Discussion

Today we talked about a lot of interesting arithmetic things. Math is huge in programming, but not intimidatingly so. If you remove the input (keyboard, microphone, video) and output (screen, audio, video), programs basically reduce down to doing arithmetic and making decisions. So we spend a lot of time on arithmetic and shoring up our understanding of those features.

In addition to the basic stuff talked about, here are some of the highlights that I noted as we were discussing things:

* Activities/worked examples we didn't quite get to
* How to understand `SyntaxError` messages in Python
* Arithmetic results, including is the result an integer or a float? Specifically, results of `/` and `//`.
* Precedence of operators.
* Input is always a string until you convert it, and `+` and `*` work with strings and mixed data but `-` doesn't.
* Data types again, but dynamic data types.
* How to *really* learn Python (find your passion!)

----

I added a few activities/worked examples that we would have covered in class into the [activity.py](activity.py) file. The examples include converting temperatures, calculating the area of a cone, and calculating Body Surface Area, which is used in medical prescription calculations.

----

We talked about how to debug syntax errors that zyBooks or Thonny may generate. You might get an error that looks like this when you run code in either platform:

```unix
Traceback (most recent call last):
  File "highlights.py", line 7
    d = a +  # 15
                ^
SyntaxError: invalid syntax
```

This means that by the time Python got to this point in your code, it was expecting something else.  In this instance, if you look at the line of code listed, you can see that the line is missing a right-hand side to the addition operator (`a +` plus what?

Sometimes the line listed will be perfectly fine, but if there's a `SyntaxError`, it implies the error is on a previous line.

----

The results of an arithmetic expression in Python will either be int or float and usually depends on if there is a floating point value introduced into the equation. Typically, if two integer values are involved, the result will be an integer result, such as `6 + 5` being `11` or `8 * 77` being `616`.  The exception is if you are doing division, which always results in floating point results, such as `8 / 2` being `4.0` or `7 / 2` being `3.5`.

Floored division, `//` results in integer values if both operands are integers but floating point if one or both are already floats.

If you use the floored division operator `//` your result will be different. Using it with the same numbers, if you use the `//` operator, your result will be an integer:

```python
print( 18 // 5 )  # output result is 3
```

But if you use the floored division operator `//` with a floating point value, the result will be a "whole" number but your result will be a floating point value:

```python
print( 18.0 // 5 )  # output result is 3.0
```

This is a similar statement, just using a float in the divisor.

```python
print( 18 // 5.0 )  # output result is 3.0
```

----

We didn't explicitly talk about precedence of operators in the [highlights.py](highlights.py) part of lecture, but [here's a nice resource](https://www.programiz.com/python-programming/precedence-associativity) that talks about it if you would like a different presentation than what was given in the textbook.

----
We looked at [Q6.py](Q6.py), which introduced that the code mostly looks good except that the input is always input as a string. The code will end up with a runtime error when the subtraction is attempted later in the program.  The multiplication `*` results in a very long string because when used with a string, `*` is a repetition operator.  But in the next statement where a string and an integer are thrown together for subtraction, Python complains and crashes because it doesn't know how to subtract an integer from a string.

----

We looked at [Q7.py](Q7.py), which brought us to a discussion of dynamic data types. If a variable at one point stores a floating point value, that doesn't mean it can't change and store an integer value or a string later on.  Variables in Python shift and change to adapt to the type of data you are storing into them.  This brings back the idea of immutability, which is the idea that variables  that store floating point, integer, or string values are immutable. This means that you don't change the value of a variable _in place_, but rather if you store new values into a variable, an entirely new location in memory is created with the same name and the new value:

```python
value = 1
# right now, variable value holds an integer
print(value)
print(id(value))
# we just printed the value itself and the id/memory location of variable value

value = "Hello"
# now variable value holds a string. since it's now a different type of data, the old
# location is discarded and a new location is allocated to store value.
print(value)
print(id(value))
```

----

Lastly, we talked about, "How can I learn Python better and more deeply?" The answer I always give is to find something that you're passionate about and dive deep. 

* Do you like robotics? Get a Raspberry Pi and some servos and write some code to build an insect walker. 
* Do you like collecting data? Get a Raspberry Pi and a camera module and/or temperature sensor and collect images or temperature data.  
* Do you like art? Look into graphics libraries and see if you can write programs that make or modify art (think: writing filters). 
* Make a basic video game. 
* Process DNA sequences. 
* Send emails to your friends ... but from inside a program! 
* Process stock market data!
* Predict fantasy sports leagues!
* Make music!
* Get some low-cost boards and create interactive wearables for cosplay.

Essentially, if you have a passion, you can probably apply Python to it in some way. The possibilities are, truly, limited only by what you can think up.

## The topics for this lecture

* Arithmetic Expressions
  - Expressions
  - Literals
  - Operators
  - Evaluating Expressions
  - Precedence Rules
* Python Expressions
  - Coding style: single space
  - Compound operators

* Division and modulo
  - Division produces floating point results
  - Floored division produces whole number results (rounded down/truncated)
  - Modulo produces integer remainders
* Math module
  - math module
  - Functions
  - Function calls
  - Function arguments
  - Importing modules in Python

## The highlighted topics for this lecture

* Arithmetic expressions
 - Expressions
 - Literal
 - Operator
 - Precedence rules
* Python expressions
 - Arithmetic operators `+`, `-`, `/`, `*`, `%`, `**`
 - Compound operators `+=`, `-=`, etc.
 - Single space around binary operators

* Division and modulo
 - Modulo using `%`
 - Division using `/`
 - Floored division using `//`
* Math module
 - Module
 - Use of import statement
 - Function
 - Function argument

## Music played at the beginning of class

* [Sleep to Dream](https://www.youtube.com/watch?v=L9Wnh0V4HMM) by Fiona Apple
* [Mine Forever](https://www.youtube.com/watch?v=yOz3VJD4L0o) by Lord Huron
* [Your Light](https://www.youtube.com/watch?v=1OijD72t4XY) by The Big Moon
* [Got Your Number](https://www.youtube.com/watch?v=mRo8glkpE5g) by Serena Ryder
