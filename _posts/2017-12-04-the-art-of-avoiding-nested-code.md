---
title: The art of avoiding nested code
date: 2017-12-04T23:34:42+01:00
author: "davide_mastromatteo"
excerpt: |
  The fifth statement of Tim Peter's "Zen of Python" is: "Flat is better than nested". So, let's explore some tips to make our code flatter and avoid nested code in Python! :)
header:
  teaser: https://imgs.xkcd.com/comics/flatland.png
categories:
  - Dev
tags:
  - Featured
  - Functools
  - List Comprehension
  - Maps
  - Python
redirect_from:
  - /2017/12/the-art-of-avoiding-nested-code
  - /2017/12/the-art-of-avoiding-nested-code/
  - /dev/the-art-of-avoiding-nested-code/
---
![teaser](https://imgs.xkcd.com/comics/flatland.png)

Today's article is about nested code and how to avoid it.

Why we should try to avoid nested code? Well the answer is inside your heart, and in your Python interpreter...

Start your REPL and write:

```python
>>> import this
```

you will get the "Zen Of Python" by Tim Peters.

```console

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one — and preferably only one — obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let's do more of those!
```

Now relax, breath, and read carefully all the statements, three times each.
Stop at the fifth statement and start meditating about that.

> Flat is better than nested
> Flat is better than nested
> Flat is better than nested

Do you get it?
***FLAT IS BETTER THAN NESTED!!***

So, let's start making your program *flatter*! :)

---

## Tip #1 — List Comprehension

Raise your hand if you have ever written code like this:

```python
my_input_numbers = [1,2,3,4,5,6,7,8]
my_odd_numbers = []

for number in my_input_numbers:
    if number % 2 != 0:
        my_odd_numbers.append(number)

print(my_odd_numbers)
```

Come on, don't be shy! Raise your hand!
Ok, are you looking at this article with a hand raised?

**SHAME ON YOU!**

you probably don't know anything about *List Comprehension*, do you?

List comprehension is a (great) way of defining a list in Python, just like you'd do in math. For example, by using list comprehension the previous code could be rewritten like this:

```python
my_input_numbers = [1,2,3,4,5,6,7,8]
my_odd_numbers = [x for x in my_input_numbers if x%2 != 0]
print (my_odd_numbers)
```

Pretty cool uh? And it's definitely flatter!

But list comprehension makes possible to do something more than just filter out even numbers from a list, for example, we can also manipulate the elements of the list:

```python
my_squared_odd_numbers = [x*x for x in my_input_numbers if x%2 != 0]
```

Or again, let's say that you want to create a list of tuples where you will put all the combinations of the (integer) numbers between 1 and 90 taken 2 at a time (quite common if you play the Italian lottery), how can you do this?

```python
ambi = [(x, y) for x in range(1,91) for y in range(x+1,91)]
```

Yes, that's so easy!
One line of code instead of two-nested-for-loops, that's it.

---

## Tip #2 — Map, Filter and Reduce

If you have liked list comprehension you will probably like also the three functions we're going to discuss here.

### The map function

> map (*function*, *iterable*, *...*)

The "*map*" function lets you execute a function on all the items of an iterable and returns an iterator with the result of this operation.

For example, let's write this one:

```python
my_numbers = [1,2,3,4,5,6,7,8,9,10]
my_squared_numbers = map(lambda x:x*x, my_numbers)
print(list(my_squared_numbers))
```

and we will have as a result:

```console
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Ok, ok, I know that some of you are now thinking "why don't you use list comprehension to make that?"
Yes, it's true, I could have written something like this:

```python
my_squared_numbers = [x*x for x in my_numbers]
print(my_squared_numbers)
```

but it's not the same. Look carefully to the two examples again...

Did you get that?

In the former example, after we used the *map *function we had to use the "list" class to print out the results. That's because "*map"* returns an iterator, not a real list.

If you are wondering what are iterators, go and check my [previous article](https://medium.com/the-python-corner/iterators-and-generators-in-python-2c3929a144b) about the topic.

### The filter function

> filter (*function*, *iterable*)

The "*filter*" function lets you filter out a list for certain values that meets a certain condition. Just like the the "*map*" function, the filter one return an iterator object with the results.

So, for example:

```python
my_numbers = [1,2,3,4,5,6,7,8,9,10]
my_odd_numbers = filter(lambda x: x%2!=0, my_numbers)
print(list(my_odd_numbers))
```

Like before, if you don't need an iterable or if you do need a list, you can achieve the same result with list comprehension.

### The reduce function

> functools.reduce (*function*, *iterable*[, *initializer*])

The "*reduce*" is the last function we are going to discuss today. It lets you take an iterable and... reduce it literally to a single element by applying a function of two arguments cumulatively to the items of the iterable input. For example:

```python
import functools
my_numbers = [1,2,3,4,5,6,7,8,9,10]
my_sum = functools.reduce(lambda x,y : x+y, my_numbers)
print(my_sum)
```

And the result will be 55!

That's great, isn't it?

As you can see we had to import the functools library to use the reduce function because since the release of Python 3 this function is no more a built-in standard function and it's now part of the functools library.

---

## Tip #3 — Ternary conditional operator

If you are used to languages like Swift or C# you have probabilly seen the ternary conditional operator before.

For example, in Swift you can write something like this:

```swift
let x = 5
// let's get x*x only if x is an odd number...
let squared_if_odd = x%2 == 0 ? x : x*x
```

this operator is very handy because it avoids you to write code like this:

```swift
let x = 5
var squared_if_odd = x

if x%2 != 0 {
    squared_if_odd = x*x
}
```

This handy ternary conditional operator is available also in Python, even if the syntax it a little different from what we could expect:

```python
x=5
squared_if_odd = x if x%2==0 else x*x
```

Really convenient and definitely flat!

That's all folks, go back to your code and start using these techniques; your code will be far more readable from now on.

Enjoy!
D.
