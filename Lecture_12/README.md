# Lecture 12, October 3, 2022

## In-class Errata / Additional Discussion

We spent the first 30 minutes of class writing two separate worked examples. The first, [highlights.py](highlights.py), implemented a random password generator. We used the `random` module and the `random.randint(x,y)` function to help pick random characters out of a source string and then apply it to building a password of a specific length.  This allowed us to explore the following concepts:

1. Random number generation with `random`.
2. String processing by position (similar to the way you access list elements by position).
3. Counter-controlled repetition to create passwords of a specific length.

We did some code refinement as we developed the solution, such as creating the `howmany` variable that is the length of the `source` string so that we can add and subtract potential password characters without worrying about modifying our actual password generation loop. All told, we wrote 9 lines of code that will generate strong passwords.

Then we wrote [highlights2.py](highlights2.py) which created a list of high temperatures (Sunday through Saturday). Then, familiarizing ourselves with lists,  we found the highest and lowest high temps, the average high temperature for the week, and printed Sunday's and Friday's high temperatures. Using sequence functions like `len()`, `sum()`, `min()`, and `max()`, we were able to process a list of values in a pretty straightforward manner to accomplish the requested tasks.

----

We then started working on our Peer Instruction questions, and [Q1.py](Q1.py) and [Q2.py](Q2.py) explored counter-controlled loops to see if we could determine the number of executions of the various loops.

Of the five remaining questions, we spent the most time on [Q7.py](Q7.py) which utilzed the `remove()`, `pop()`, and `append()` functions for a list. What most folks wrestled with was whether or not `remove()` deletes only the first instance of the value or all instances of the value in the list. As we found out, [it removes only the first instance](https://www.programiz.com/python-programming/methods/list/remove).


## Music played at the beginning of class

* [Alive](https://www.youtube.com/watch?v=t2NgsJrrAyM) by Sia
* [Head Full Of Doubt/Road Full Of Promise](https://www.youtube.com/watch?v=QeYSqZPzwr8) by The Avett Brothers
* [Fast As You Can](https://www.youtube.com/watch?v=NbxqtbqyoRk) by Fiona Apple
* [Ship to Wreck](https://www.youtube.com/watch?v=HgY7nzGxkD4) by Florence + the Machine


## The topics for this lecture were:

* Counter-controlled loops
	- Counting by 1
 	- Counting in reverse
	- Skip-counting

* Lists
	- Data container in Python
	- `[]` notation to create
	- Element
	- Position/index
	- Mutable collection

* Sequence-type functions
	- Allow us to perform common tasks for a collection.



## The highlighted topics for this lecture were

Sequence-type functions

* `len(sequence)`
* `sequence1 + sequence2`
* `min(sequence) and max(sequence)`
* `sum(sequence)`
* `sequence.index(value)`
* `sequence.count(value)`
