# Lecture 26, November 28th, 2022

## In-class Errata / Additional Discussion

Today's lecture focused on quite a bit of content. The [highlights.py](highlights.py) file demonstrated a number of different aspects of the `.items()`, `.keys()`, and `.values()` functions for dictionaries.

When calling `sorted()` on the results of something like `dictionary.items()`, as in [Q2.py](Q2.py), the sorting happens on the keys regardless of whether you would like to process the keys and/or the values.  Sorting on values requires the use of a lambda expression, which is not covered in this class.

One thing to remember is the difference between `sorted(list)` vs `list.sort()`.  The `list.sort()` version is an in-place sort of `list` with no return value.  The `sorted(list)` version returns a sorted version of the list without affecting the original `list` value ordering.

When processing something like `sorted(data, reverse=True).pop()` as illustrated in [Q4.py](Q4.py), the call to `sorted()` generates an anonymous list (since the result is never stored to a named variable) that then has a value popped off of it at the end. The anonymous list _does_ get modified by removing that last element, but the result of the code is the result of the last thing that gets done, which is the `pop()`.

The last main thing we talked about was with [Q6.py](Q6.py), accessing values stored in nested dictionary structures. An analogy is to think about accessing an apartment in an apartment building in a specific apartment complex in a suburb, etc.  To access the `Sleep` spell in the structure in question 6, we're accessing the element in position `1` of the list (apartment number) that is attached to the `Spells` key (apartment building) that itself is in a dictionary that is attached to the `Wizard` key (the apartment complex) in the characters dictionary (the suburb the complex is located in).

Navigating nested structures is tricky and the best way to get comfortable with them is to practice, practice, practice!

## Music played at the beginning of class

* [Level Up](https://www.youtube.com/watch?v=U4n_8R5lKnw) by Vienna Teng
* [Preachin' Blues](https://www.youtube.com/watch?v=cEWiJR9qeoc) by Larkin Poe
* [Off the Ground](https://www.youtube.com/watch?v=H8aNK3XMP5w) by The Record Company
* [6 Underground](https://www.youtube.com/watch?v=2eBZqmL8ehg) by Sneaker Pimps

## The topics for this lecture were:

* Dictionary iteration
	* `items()`
	* `keys()`
	* `values()`
* Dictionary nesting


## The highlighted topics for this lecture were

* View objects for dictionaries
	* `dictionary.items()`
	* `dictionary.keys()`
	* `dictionary.values()`
* Nested dictionaries
