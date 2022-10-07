# Lecture 13, October 5, 2022

## In-class Errata / Additional Discussion

We started class by going over the brief overview of tuples, sets, and dictionaries, and then wrote [highlights.py](highlights.py) to work with sets and demonstrate the following functions: `union()`, `intersection()`, `difference()` and `symmetric_difference()`.

A student came up after class and asked about the `symmetric_difference()` function. For sets, it gives you all of the items that are not common to either set. The student asked if it was the same as taking the union of two sets and then subtracting the intersection of those sets.  The answer is: yes.  So, while it's easier to write:

```python
group_1 = {"Nichole", "Tyreese", "Mustafa", "Aliza"}
group_2 = {"Aliza", "Nichole", "Judah", "Toby", "Vikki"}

print(group_1.symmetric_difference(group_2))
```

you could also write:

```python
group_1 = {"Nichole", "Tyreese", "Mustafa", "Aliza"}
group_2 = {"Aliza", "Nichole", "Judah", "Toby", "Vikki"}

print(group_2.union(group_1).difference(group_2.intersection(group_1)))
```

I prefer the first way, but the second way gives you the same results.  :)

----

We then worked through some questions about tuples, sets, and dictionaries. I'm writing this summary the day after class and didn't take great notes during class about what we discussed, but I seem to recall we spent a little bit of time talking about the following:

1. [Q4.py](Q4.py), where you can't access sets by position because there's no position in sets. So the code looks good except for `set1[0] = 22` which can't happen because you can't address a position in a set.
2. [Q5.py](Q5.py), which introduced using `intersection()` and `difference()` for more than 2 sets, specifically 3 sets.  The intersection of 3 sets is the same as drawing a venn diagram and where all three sets overlap (i.e., the items that are common in all three sets) is the `intersection()` of multiple sets. The `difference()` of three sets is where you start with the first set and then just keep subtracting anything that is common in any of the other sets; what's left over is the `difference()` of multiple sets.

There were some other discussions, obviously, but those two stood out to me on the next day.

We didn't get to [highlights2.py](highlights2.py), where we would have written a basic dictionary program that asks for a place (the key) and then a location for that place (the value) and then creates a dictionary with those key/value pairs.  The program uses a sentinel-controlled loop to enter as many place/location pairs as the user wants.  Writing this is left as an exercise for you if you would like some practice.

## Music played at the beginning of class

* [Something in the Orange](https://www.youtube.com/watch?v=lA8F9sIhGdg) by Zach Bryan
* [The Lion The Beast The Beat](https://www.youtube.com/watch?v=Ov8uT8DTvlw) by Grace Potter and the Nocturnals
* [What Do You Heart in These Sounds](https://www.youtube.com/watch?v=LwrQXI4_mgo) by Dar Williams
* [Annabelle Lee](https://www.youtube.com/watch?v=O-SLSZ-9748) by Sarah Jarosz


## The topics for this lecture were:

* Tuples
	- Data container in Python
	- `()` notation to create
	- Element
	- Position/index
	- Immutable collection
	- Named tuple

* Sets
	- Container grouping related values
	- Uses `{}` to create a set
	- Mutable (can change)
	- Values are unique
	- `set()`
	- `add()`, `remove()`, `pop()` 
	- `intersection()`
	- `union()`
	- `difference()`
	- `symmetric_difference()`


* Dictionaries
	- Container grouping related values
	- Uses `{}` to create a dictionary
	- Key
	- Value
	- Keys are unique
	- `del`
	- Mutable (can change)


## The highlighted topics for this lecture were

See above.
