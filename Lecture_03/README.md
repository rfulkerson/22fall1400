# Lecture 03, Monday, August 29th, 2022

## Summary

Today's lecture was all about looking at basic output and basic input. This summary is not comprehensive of all of the topics covered in the book or lecture, but is meant to be representative of the highlights of discussions that took place.

Basic output is accompished with the `print()` function.

By default, the `print()` statement will print a newline at the end of whatever the statement is printing, which means that the next print statement would start it's content at the beginning of a new line.

This behavior can be changed by using the `end=""` parameter for the print statement which changes the last output of the print statement to whatever the `end` parameter is.

For example, the following two statements are identical:

```python
print("Hello world!")
print("Hello world!", end="\n")
```

If the `end` parameter is omitted, then it defaults to a newline escape sequence (`\n`).  Usually, at least in CS1, the `end` parameter is either an empty string or a space to keep the output on the same line:

```python
print("Hello", end=" ")
print("world!")

# identical output below; notice where the space is ... inside the string
# literal instead of in the end parameter:
print("Hello ", end="")
print("world!")
```

We also talked about basic input using the `input()` function.  Without a parameter (something inside the parentheses), the `input()` function just waits for the user of the program to type some input. With a parameter (a string), the string is used as a prompt to tell the user what to enter.

The results of an `input()` function call need to be stored into a variable so that the value can be used later in the program.

```python
# no prompt, store the result of the input into variable my_value
my_value = input()
print("You entered:", my_value)

# this time a prompt, store the result of the input into variable my_other
my_other = input("Please enter something:")
print("You entered:", my_other)
```

All input, by default, is textual or string data. If you need a value to be processed arithmetically later in your program as a number, you need to cast the input to the appropriate data type. To convert textual input to an integer, whole number value, use the `int()` function:

```python
my_age = int(input("Please enter your age:"))
print("You are", age, "years old.")

# because my_age is a number, you can do basic math with it, like this
print("In 10 years, you will be", age + 10, "years old.")
```

If you attempt to do arithmetic with a value read from the user that hasn't been converted to an integer or other type of number, you will receive a TypeError:

```python
# the "number" is read as a string because that's what input() does
my_number = input("Enter a number please:")

# the statement below will fail because Python doesn't know how to operate
# with a string on the lefthand side of the addition operator and an integer
# on the righthand side
print(my_number + 6)
```


## The topics for this lecture:

* Basic Output
  - `print()`
  - Basic outputting options
* Basic Input
  - `input()`
  - Input types and prompts
* Errors
  - 3 main types of errors
  - Detecting Errors practice

## The highlighted topics for this lecture:

* `print()`
* String literal
* `print("A",2)`
* `print("Hello", end=" ")`
* Newline character `\n`
* whitespace
* `input()`
* `input("prompt")`
* String input
* Data type
* `int()`
* Syntax error
* Runtime error
* Logic error
* Bug
* Crash
