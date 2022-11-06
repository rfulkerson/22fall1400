# Lecture 20, November 3rd, 2022

## In-class Errata / Additional Discussion

We had good in-class discussions about the topics in this lecture. Writing this a few days after class, I don't recall all of the finer points we discussed, unfortunately.

Discussions about immutable and mutable function arguments was also discussed, as we demonstrated with some code in [highlights.py](highlights.py), with immutable objects such as integers and strings _not_ being changed in functions when passed as arguments and mutable items such as lists having their items changed if they're directly accessed.

Compare the code in [Q1.py](Q1.py) to the code in [Q2.py](Q2.py) and notice that in Q1, since the items in the list are being accessed by position, changes made in the function to the list are reflected outside the function.  Whereas in Q2, since the items are being referenced in a `for` loop (but not by position), those copies of the values are changed but hte list itself remains intact.

Using keyword arguments, we noticed that the order that you call the argments doesn't have to match the parameter list. But if you don't use keyword arguments (i.e., you just pass values), then order does matter.

The last thing we observed is that if you have a mix of parameters in a function that have default values and don't have default values, the parameters that have default values _must_ be the last parameters in the list.  In other words, any required parameters need to be listed first in the list.


## Music played at the beginning of class

* [I and Love and You](https://www.youtube.com/watch?v=T0eSpAgqrWo) by The Avett Brothers
* [Doctor Who Theme](https://www.youtube.com/watch?v=2qmFzUUnsJQ) by Murray Gold
* [The Doctor's Theme](https://www.youtube.com/watch?v=WGDeV4lPADE) by Murray Gold
* [Rose's Theme](https://www.youtube.com/watch?v=Fqogz-g0Jg4) by Murray Gold
* [Blue in Green](https://www.youtube.com/watch?v=TLDflhhdPCg) by Miles Davis

## The topics for this lecture were:

* Function arguments and mutability
* Large parameter lists
* Keyword parameter passing
* Default values for parameters
* Returning multiple values from a function

## The highlighted topics for this lecture were

* Function arguments
	* Immutable: strings, integers, etc.
	* Mutable: lists, etc.
* Use of `[:]` to prevent mutability
* Keyword arguments
* Default parameter values
* Multiple function return values
	* Package as a collection, typically a tuple
	* Unpack on return
