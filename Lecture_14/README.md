# Lecture 14, October 10, 2022

## In-class Errata / Additional Discussion

Today, we looked at the membership and identity operators as well as the `for` loop in Python.

After the basic overview, we wrote [highlights2.py](highlights2.py), which implemented building a 5x5 word search from a single string of 25 characters. Through iterative development (write/test/write/test), we use the `for` loop and membership operator `in` to move through every character in a string and output it, one character per line. 

Then we modified it so all characters were printing on a single line with a space between each one. Finally, we added in a selection statement and a counter so that every X characters (to start with, X was 5), we would output a newline. Then we talked about how we could expand the string to 64 characters or 100 characters to make an 8x8 or 10x10 grid.  

If we modified the length of the source string, we found that we had to modify the selection statement in the `for` loop each time to make sure we were outputting the correct number of characters per line.  Thinking about it a little, we realized that if we have the length of the string, we can find the square root of that length using `math.sqrt()` and then use _that_ value in our selection statement to determine how many characters to print per line.

----

During our Peer Instruction questions [Q1.py](Q1.py), [Q2.py](Q2.py), and [Q3.py](Q3.py), we looked at the identity (`is`) and membership (`in`) operators and discussed how the identity operator only evaluates to true if the lefthand and righthand operators are the same object in memory.  This is usually reserved for small numeric values and short strings. Usually, for beginning programming students, what is usually intended is an equality test when `is` is used instead. Here's a really nice explanation of `is` vs `==`: [https://www.youtube.com/watch?v=CZ8bZPqtwU0](https://www.youtube.com/watch?v=CZ8bZPqtwU0)

----

We also looked at using the membership operator with dictionaries in [Q4.py](Q4.py). What we discovered is that the `in` operator when used with a dictionary only looks at the keys of a dictionary. Later this semester, we'll look at the `.values()` function we can call on a dictionary to find the values and use that instead if we want to look at using `in` with the values of a dictionary.

----

[Q5.py](Q5.py) had as work through using the `in` operator with a `for` loop and a list to iterate through. We did really well with this question, understanding that the `for x in [10, 20, 30, 40, 50]` allows us to just move through all values in a list of values.

As an extension of this, I proposed the following situation:

```python
y = [10, 20, 30, 40, 50]
for x in y:
    x *= 2
print(y)
```

I asked what would happen to list `y` and what would print. A straw poll had people split between printing `[10, 20, 30, 40, 50]` and `[20, 40, 60, 80, 100]`. The answer is the former, because `for` loops like this don't affect the original list at all.  Variable `x` takes on copies of values in the list, so any modifications to `x` don't change the original list.

----

[Q6.py](Q6.py) asked about using a `while` loop to move through a string, but we discussed that the way the loop is written, it's missing a loop control variable modification so it's an infinite loop stuck printing nothing but the first letter of the string you entered.

[Q7.py](Q7.py) remedied this by implementing a `for` loop like the one we implemented in [highlights2.py](highlights2.py). Using a `for` loop like this, you don't have to keep track of your position in a string (or list, tuple, set, or keys of a dictionary) because the `for` loop will just work from beginning to end, first element to last element.

----

We didn't get a chance to work through [Q8.py](Q8.py), [Q9.py](Q9.py), or [Q10.py](Q10.py).

## Music played at the beginning of class

* [B-A-B-Y](https://www.youtube.com/watch?v=WvL---NdeS8) by Carla Thomas
* [Bellbottoms](https://www.youtube.com/watch?v=7ARFyrM6gVs) as seen in "Baby Driver" by The Jon Spencer Blues Explosion
* [Hounds of Love](https://www.youtube.com/watch?v=VerK4zwMRQw) by Kate Bush
* [Sanctuary](https://www.youtube.com/watch?v=uBkN9y9zf9Y) by Hiss Golden Messenger


## The topics for this lecture were:

* Membership Operators
	* in / is
* Summary of Types so far
* For loops
	* Structure
	* Use of in
	* Processing lists, tuples, sets, dictionaries, and strings

* Membership and Identity
	* `in`
	* `not in`
	* Can be used on containers or strings
	* Used quite a bit!

	* `is`
	* `is not`
	* These don’t check values, but rather if two variables are the same object (reference the same item in memory)
	* Not used that much, but good to know


## The highlighted topics for this lecture were

```python
for var in container:
    # loop body
```

* The container can be a string, list, tuple, set, or dictionary.
* Variable `var` takes on the values of the container in a read-only manner.
* Must work through the entire container front to back, and there's no easy way to "skip-count" through elements.

* Strings: each character
* Lists, tuples, sets: each value
* Dictionaries: keys

