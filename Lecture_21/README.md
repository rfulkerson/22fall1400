# Lecture 21, November 7th, 2022

## In-class Errata / Additional Discussion

Today's class had some good discussions about string processing and slicing.  You can check out the [highlights.py](highlights.py) code for the, well, highlights that were outlined at the beginning of class.

Some quick, key takeaways from group discussions and questions during the highlights coding:

* Remember that strings are immutable, so any operations or functions working on strings don't change the string itself, but rather create new, resultant strings.  So, if you have a variable `foo` and want to use `.upper()` to convert it to all uppercase, you would use `foo.upper()`.  This wouldn't change the contents of `foo`, but rather give you a new string to work with.  Likewise, `foo[3:6]` doesn't change `foo` but rather provides a slice of the characters at positions 3, 4, and 5.
* This applies to functions like `.replace()`, also. See [highlights.py](highlights.py) for examples of using `replace()`.
* String formatting allows you to create a field of characters to output your information to, such as `name = "Hello"` followed by `print(f"{name:60}")` would print the name, left-justified in a field of 60 spaces.  `print(f"{name:>60}")` would print the same text right-justified in a field of 60 spaces.
* When using field widths like that, numbers are right-justified by default.


## Music played at the beginning of class

* [Out of My Head](https://www.youtube.com/watch?v=PmSwUCdQQC4) by First Aid Kit
* [Some Of Us Are Brave](https://www.youtube.com/watch?v=GC5UBAoa6nw) by Danielle Ponder
* [Kings & Queens](https://www.youtube.com/watch?v=jH1RNk8954Q) by Ava Max
* ['Cello Song](https://www.youtube.com/watch?v=R4XUiEWZLas) by Nick Drake

## The topics for this lecture were:

* String slicing
	* Slice notation and operations
	* Slice stride
* Advanced string formatting
	* Field width, alignment, and fill
* String functions
	* Find and replace
	* Comparing strings
	* Creating new strings

## The highlighted topics for this lecture were

* Slice notation
* `foo[start:end]`
* `foo[start:]`
* `foo[:end]`
* `foo[start:end:stride]`
* Slices create new strings

* Field widths such as `{:10}`
* Field alignment using `<`, `>`, and `^`
* Floating point output such as `{:.3f}`

* `replace(old,new)`
* `replace(old,new,count)`

* `find(x)`
* `find(x, start)`
* `find(x, start, end)`
* `rfind(x)`

* `count(x)`

* `==`, `!=`, `>`, `<`, `in`

* `isalnum()`, `isdigit()`, `islower()`, `isupper()`, `isspace()`, `startswith(x)`, `endswith(x)`
* `capitalize()`, `lower()`, `upper()`, `strip()`, `title()`
