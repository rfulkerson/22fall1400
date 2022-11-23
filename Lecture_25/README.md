# Lecture 25, November 21st, 2022

## In-class Errata / Additional Discussion

The [highlights.py](highlights.py) file contains a lot of the testing and playing around with the different topics discussed in this lecture. Some of the items that are difficult to understand are the differences between `list.sort()` and `sorted(list)`. I'll refer you ahead one lecture (I'm writing these summaries in reverse this week) to [Lecture 26](../Lecture_26/README.md) for a discussion about that.

A bit of time was spent toward the end of the `highlights.py` file talking about what happens if you try to delete an element out of a dictionary when the key doesn't exist.  If this is attempted, a `KeyError` is raised and the program has a runtime error crash. To avoid this, given what we have this semester, we can either test for the presence of the key before deleting it or use the `pop()` with a default value for failure, like this:

```python
if "potential_to_delete" in dictionary:
   del(dictionary["potential_to_delete"])

# or

dictionary.pop("potential_to_delete","default value for failure")
```

I also wanted to spend some time advocating for coding on your own to practice with Python but ran out of time. Find a topic you're interested in (biology, art, math, computers, English ... it doesn't matter) and then see if there's a way to apply creating a program to do something in that space. A common use of Python in everyday "maker" life is to program small circuit boards as "wearables" that control lighting/sensors in clothing.  Another space to play in is with any of the libraries we've looked at this semester such as `matplotlib` or `Turtle`. Finally, something else you could play with might be pygame, which has about a billion tutorials out there for creating games and animations. [Here is a nice introduction](https://nerdparadise.com/programming/pygame) to some basic pygame programming that helps you create and animate shapes or images that respond to keypresses and/or mouse clicks.

Recently, for fun (because I'm a computer scientist :), I've coded up the Game of Life (one of your recitations) in PyGame instead of matplotlib in preparation of redoing the recitation with PyGame next semester and an implementation of [Hunt the Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus), an old-school text-based adventure game created in 1973.

Regarding the rest of the code for the day, there were questions that addressed the aforementioned `list.sort()` vs. `sorted(list)` differences, as well as some questions about deleting items from a dictionary.

## The topics for this lecture were:

* Sorting Lists
	* Discussion of the built-in sort() method for lists.
	* In-place sorting of the list with sort().
	* Creating copy of sorted list with sorted().
	* Using a sort key to modify the behavior of sorting strings using either method.
	* Sorting numeric or string lists in reverse.
* Dictionaries
	* Dictionaries as a container
	* Key-value pairs
	* Common operations
	* Dictionaries of other containers
* Dictionary Methods
	* foo.clear(), foo.get(key, default)
	* foo.update(foo_2), foo.pop(key, default)

## The highlighted topics for this lecture were

* `sort()`
* `sorted()`
* `key` keyword argument: `str.lower`, `str.upper`, `min`, `max` 
* `reverse` keyword argument: `True` or `False`
* Dictionary comprehension
* Accessing individual elements
* `del`
* `key in dictionary`
* `dictionary.clear()`
* `dictionary.get(key, default)`
* `dictionary.update(other)`
* `dictionary.pop(key, default)`
