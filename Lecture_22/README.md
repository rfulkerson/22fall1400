# Lecture 22, November 9th, 2022

## In-class Errata / Additional Discussion

Today, we discussed that `split()` on a string breaks strings apart based on whitespace characters by default, so it essentially just tokenizes a string into "words" (whatever non-whitespace looks like in a particular string).

When provided with an argument, such as `split('?')` in [Q2.py](Q2.py), Python will return results for something on both sides of the delimiter, since a delimiter separates tokens.  So if the delimeter is at the beginning or end of a string, there will be an empty string that is generated in the list at the front or the back of the list.

Remember that since lists are mutable, there doesnt need to be an explicit `return` statement from a function for any changes to the list to be reflected outside the function, as seen in [Q8.py](Q8.py), for example.

Two other topics that were _briefly_ discussed during our creation of [highlights.py](highlights.py) were the ideas of queues and stacks.  [Here is a nice video introduction](https://www.youtube.com/watch?v=A3ZUpyrnCbM) to the concept of stacks and queues (including octopi!) that gets a _little_ detailed toward implementation at the end, but overall is a nice overview if you're interested.

## The topics for this lecture were:

* String split and join
	* `split()` and `join()`
* Lists review

* Lists
	* Data container in Python
	* `[]` notation to create
	* Element
	* Position/index
	* Mutable collection
* Sequence-type functions
	* Allow us to perform common tasks for a collection.

## Music played at the beginning of class

* [Silver Lining](https://www.youtube.com/watch?v=jVtSSCzASR0) by Rilo Kiley
* [Someone in the Crowd](https://www.youtube.com/watch?v=A7RmBgq4tT4) by 	Emma Stone, Callie Hernandez, Sonoya Mizuno and Jessica Rothe 
* [Sing, Sing, Sing](https://www.youtube.com/watch?v=yCxAi0uFg7w) by Benny Goodman

## The highlighted topics for this lecture were

* `split()`
* Token
* Separator and default separator
* `join()`

* List
* Container
* Index
* Mutable
* In-place modification
* `list()`
* `del` 
* `my_list[x:y]`

* Lists
	* Position/index always starts at `0`
	* Mutable (can change)
	* `list.append(value)`
	* `list.extend([x])`
	* `list.insert(i, x)`
	* `list.pop()`
	* `list.pop(position)`
	* `list.remove(value)`
	* `list.sort()`
	* `list.reverse()`
 
* Sequence-type functions
	* `len(list)`
	* `list1 + list2`
	* `min(list) and max(list)`
	* `sum(list)`
	* `list.index(value)`
	* `list.count(value)`
