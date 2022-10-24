# Lecture 16, March 22nd, 2022

## In-class Errata / Additional Discussion

There were some really good discussions about the questions today.

We wrote a quick number-guessing game in [highlights.py](highlights.py) to start with and discussed `break` as well as utilizing the `enumerate()` to work through a list and output a menu of items in [highlights2.py](highlights2.py).

We had some good discussions about [Q1.py](Q1.py) and [Q3.py](Q3.py). At least [Q3.py](Q3.py) should probably be rewritten because it's tough to know exactly what the intent is of the code. There are still times when the solution to [Q3.py](Q3.py) will still result in the code crashing. Our solution, using a data validation loop to make sure the length of the two strings are equal before moving on.

We were also able to work through a few questions about `enumerate`.

One question that was asked was what if you use `enumerate` but don't unpack the results into two separate variables?  So, here's _normal_ code using `enumerate` from [Q4.py](Q4.py):

```python
nums = [2, 9, 4, 1]
for pos, val in enumerate(nums):
    print(pos * val, end=' ')
```

But what if the code looked like this, in [Q5.py](Q5.py):

```python
nums = [2, 9, 4, 1]
for thing in enumerate(nums):
    print(thing, end=' ')
```

In this instance, `thing` is a tuple that consists of the position and value, such as `(0, 2)`, or `(1, 9)` for the first two tuples.  This demonstrates to us that `enumerate` will return a tuple in the format `(position, value)`.  We can unpack the tuple as in the first example into `pos, val` so that we can access each of those values by name as the `for` loop works through the list.

Lastly, we looked at [Q6.py](Q6.py), which used `enumerate()` to give us positions and values in a list that we then used selection to conditionally print either the position of an item of the value of an item as we moved through the list.

## The topics for this lecture were:

* Incremental Programming
* `break` and `continue`
* `enumerate()`
	* Concept of unpacking
	* Usage of `enumerate()`

## Music played at the beginning of class

* [Theme from Jussasic Park](https://www.youtube.com/watch?v=D8zlUUrFK-M) by John Williams
* [James Bond Theme](https://www.youtube.com/watch?v=U9FzgsF2T-s) by David Arnold
* [Prologue from Harry Potter](https://www.youtube.com/watch?v=UuPb1J_RCJM) by John Williams
* [Main Titles (From "Beetlejuice")](https://www.youtube.com/watch?v=1XVCQPPAx8Y) by Danny Elfman
* [M.I.B. Main Theme](https://www.youtube.com/watch?v=4YDx3LAsb3o) by Danny Elfman
* [Theme from Ant-Man](https://www.youtube.com/watch?v=O_5NwVy8L5M) by Christophe Beck



## The highlighted topics for this lecture were

* Developing code incrementally:
	* Write what you know, put in `# FIXME` comments or basic `print()` statements where you need to flush things out.
	* There's nothing wrong with write/run/test/write/run/test/etc …
* `break` statements
* `continue` statements
* `enumerate()` to get index, value from a list using a `while` loop
