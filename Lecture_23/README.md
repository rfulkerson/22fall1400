# Lecture 23, November 14th, 2022

## In-class Errata / Additional Discussion

Some of the key points to take away from today's discussion:

* [Q1.py](Q1.py) revisited the idea that `split()` splits on whitespace by default, and thus in this question you end up counting the frequency of words using a dictionary `f` that starts off empty.  It's worth taking a look at the `for` loop and how the `if` selection works to either initialize a newly-found word's value to be 1 or increment an existing word's count by 1.  For this question, things we thought about were:
	* Capitalization. Should `The` be counted differently than `the`? If so, then you should normalize the data by converting each word to all lowercase or uppercase, for instance, before adding or updating key-value pairs to the dictionary.
	* Punctuation. Should punctuation be removed from the sentence before it is split on spaces? Which punctuation? Apostrophes should probably be left in, and maybe hyphens and dashes, but question marks, semi-colons, and commas among others should be removed. This can be referred to as sanitizing or cleaning up the data before you process it.

---

Today's lecture also focused on 2-D lists (nested lists). Many people think about nested lists (2-D lists) like spreadsheets.  There is a logical relationship for rows (such as students) and columns (grades). Each row would represent the grades for one student while each column would represent the grades on a single assignment for all students, like this:

```python
grades = [ 
	[ 100, 90, 90, 86, 75, 87, 100 ],
	[ 90, 90, 86, 75, 87, 100, 100 ],
	[ 90, 86, 75, 87, 100, 100, 90 ],
    ]
```

The list `grades` has three rows, one for each of three students, and seven columns, one for each of seven different assignments.  Where a row and column intersect represents a grade for a specific student on a specific assignment.

The one major difference between thinking about this type of data being stored in a spreadsheet and being stored in a Python 2-D list is that for a spreadsheet, you access values using Column-Row notation (column first, row second) but for a Python list, you use Row-Column notation (row first, column second).

----

The other major topic for this lecture centered around list slicing and all of the various ways you can process lists by accessing sublists.

## The topics for this lecture were:

* Iterating over a list
* Enumerate

## The highlighted topics for this lecture were

* List nesting
* Multi-dimensional data structure
* Nested for loops to process nested lists
* Slice notation
* `my_list[START:END]`
* `my_list[START:END:STRIDE]`
* `my_list[START:]`
* `my_list[:END]`
* `my_list[:]`
* Loops modifying lists
