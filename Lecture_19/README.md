# Lecture 19, November 1st, 2022

## In-class Errata / Additional Discussion

This lecture and the [previous lecture](../Lecture_18) are both kind of summary/bridge lectures for function material.  We've been talking about a lot of these concepts so far and now we're just formalizing what we've been experiencing in our in-class discussions as well as in your labs, etc.

Today we started talking about [highlights.py](highlights.py) and wrote three separate functions, `demo_one()`, `demo_two()`, and `demo_three()` which all demonstrate various concepts about local and global scope. Variables that aren't declared inside any functions are considered to have global scope.  Variables declared explicitly within functions have local scope; that includes parameter lists.

I did misspeak a little later on when talking about variables like `a` in the following example code:

```python
for a in range(5):
    d = 6
    print("Do a thing")
print(a)
print(d)
```

In class, I mentioned that `a` would be locally scoped to the loop and then disappear when the loop was done.  That is not the case. I was conflating my programming languages, some of which _do_ locally scope variables like `a` solely to their loops. In the above example, `a` has local scope, but it _does_ "leak" out of the `for` loop with the last value it had and you _can_ print it outside the loop. The same goes for variable `d` created inside the loop; it also "leaks" out of the loop and you have access to it after the loop.

This is different than our `demo_one()` function that looks like this:

```python
def demo_one():  # demo_one has global scope
    x = 12  # local scope
    print(x)
    
demo_one()
print(x)
```

In this example, `x` has local scope, but it belongs solely to the function and does not escape out for us to have access outside the function.

This is where programming starts to get very tricky because there are some consistent behaviors and some seemingly inconsistent behaviors. This is where incremental devleopment can come in handy; test as you develop to make sure that the code is behaving the way you think it should and it's easier to catch issues like `a` or `d` leaking out of the loops. I'm using the term "leak" to give it a sense of "you should be aware of this because maybe the use of `a` or `d` later on is unintended".

We also had some good discussions about [Q1.py](Q1.py) being a void function and returning something (the value `None`), which would be printed because Python is calling function `generate()` in a `print()` statement.

[Q3.py](Q3.py) let us investigate how we need to be careful with `return` values not being created/initialized. Function `determine(inc)` would sometimes work (if the value of `inc` is in one of the tested ranges) and sometimes not work (if it's outside the tested ranges).  Full testing of your functions should be a priority to make sure that all situations are handled correctly.

Question [Q4.py](Q4.py) counts lowercase vowels in function `mystery(w)`. It's a good example of working code that could be made more literate or legible if variables like `word` were used instead of `w` and `vowels` instead of `v` or `count` instead of `a`.  Legibility really helps in situations like this.  We also talked about modifying the `if` statement to look like `if w[z].lower() in v:` to test lower- or upper-case letters without having to modify the list of vowels. I mentioned that "less is more", so the less you do with the list of vowels, the better. Meaning that you could expand the list of vowels to look like this:

```python
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
```

There's nothing wrong with that, but it's easier to forget a vowel, possibly, like this:

```python
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U']
```

Debugging this isn't necessarily difficult, but it's easy to do a quick scan of that line of code and think that all of the vowels are there.

Instead, if you keep the list to just the 5 vowels in all lowercase, then adding the `w[z].lower()` does the "heavy-lifting" of converting any capital letters to lowercase and testing against a smaller known good set of data.

We wrapped up talking about namespaces, namely local, global, and built-in, with [Q5.py](Q5.py).

Overall, great discussions in class today!

## The topics for this lecture were:

* Functions with branches
* Functions with loops
* Copy-paste errors
* Return errors
* Variable scope
* Function scope
* Namespaces
* Scope resolution

## The highlighted topics for this lecture were

* Scope
* Local variables
* Global variables
* global
* Namespace
* Scope resolution
