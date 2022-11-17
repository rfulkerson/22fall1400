# Lecture 24, November 16th, 2022

## In-class Errata / Additional Discussion

This lecture was all about list comprehensions.  Essentially, list comprehensions are just shorthanded, elegant ways to compress looping over a list. We looked at a number of different ways to process lists of data using list comprehensions, including conditional comprehensions. Those conditional comprehensions can use regular relational operators such as `results = [p for p in prices if p <= val]` such as in [Q5.py](Q5.py) or even call functions that return values of `True` or `False`, such as `leap = [x for x in years if isLeapYear(x)]` in [Q6.py](Q6.py).


## Music played at the beginning of class

* [Nowhere to Run](https://www.youtube.com/watch?v=WR9pvGtyiHg) by Martha Reeves and The Vandellas
* [Do You Realize??](https://www.youtube.com/watch?v=lPXWt2ESxVY) by The Flaming Lips
* [Love, Reign O'er Me](https://www.youtube.com/watch?v=PMxwPOoZm_c) by The Who
* [Rivendell](https://www.youtube.com/watch?v=2Ljvae3CaWs) by Howard Shore


## The topics for this lecture were:

* List Comprehensions
* Lists in comprehensions are not mutable
* Conditional list comprehensions


## The highlighted topics for this lecture were

* Lists in comprehensions are not mutable
* Conditional list comprehensions
* `foo = [expr for loop_var in iterable]`
* `foo = [expr for loop_var in iterable if condition]`
