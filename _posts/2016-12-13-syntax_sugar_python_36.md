---
title: "Syntax sugar in Python 3.6"
date: 2016-12-13T00:00:49+01:00
author: "davide_mastromatteo"
excerpt: "Let's have a quick look at the news about Python 3.6!"
header:
  teaser: https://imgs.xkcd.com/comics/formal_languages.png
categories:
  - Dev
tags:
  - syntax
  - synctactic sugar
  - python 3.6
  - python
redirect_from:
  - /2016/12/syntax-sugar-in-python-3-6
  - /2016/12/syntax-sugar-in-python-3-6/
  - /dev/syntax_sugar_python_36/
---
![teaser](https://imgs.xkcd.com/comics/formal_languages.png)

On December the 8th [Guido van Rossum](https://www.twitter.com/@gvanrossum) (also known to be the [BDFL](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) or the Python project) announced on his twitter account that Python 3.6 rc1 has been officially released. That means that if no major problems will be found with this latest version, the final release is just around the corner and it's scheduled to be released on December the 16th, carrying among other things also some improvements in the Python syntax.

Let's have a look at this new "syntax sugar"!

## Formatted string literals

The formatted string literals are one of my favorite features ever! Since today, if you wanted to create a string with some variable value inside you could do something like:

```python
>>> name = "Dave"
>>> print ("Hi " + name)
```

or:

```pytHON
>>> name = "Dave"
>>> print ("Hi %s" % name)
```

or again:

```python
>>> name = "Dave"
>>> print(str.format("Hi {0}", name))
```

We're not going to describe the pros and cons of these methods here, but the shiny new method to accomplish this task is:

```python
>>> name = "Dave"
>>> print (f"Hi {name}")
```

Pretty cool, uh? And these methods works great also with other variable types like numbers. For example:

```python
>>> number = 10/3
>>> print(f"And the number is: {number:5.3}")
```

Note that in this last example we have also formatted the number specifying the width (5) and the precision (3).

## Underscores in Numeric Literals

This feature is better seen that explained: what's the value of the variable "big_number" after the foloowing assignment?

```python
>>> big_number = 1000000000
```

If you like me needs to count the zeroes to say that big_number is a billion, you will be probabily happy to know that from now on, this assignment can be written like this:

```python
>>> big_number = 1_000_000_000
```

## Syntax for variable annotations

If you need to annotate the type of a variable now you can use this special syntax:

> variable: type

this means that you can write something like

```python
>>> some_list: [int] = []
```

this doesn't do anything more than before, Python is a dinamically typed language and so it will be in the future, but if you read some third party code this notation lets you know that some_list is not just a list, but it's intended to be a list of integers.

Please, note: I say it's *intended to be* just because nothing prevents you from assigning some_list any other kind of value! This new variable annotation is just intended to avoid writing something like:

```python
>>> some_list = [] # this is a list of integers
```

## Asynchronous generators

Asynchronous generators have been awaited since Python 3.5, that introduced the async / await syntax feature. In fact, one of the limitation it had was that it was impossible to use the yield and the await statements in the same body. This restriction has been lifted and in the documentation, there's a quite interesting example that shows a function called "ticker" that generate a number from 0 to a limit passed as a parameter every X seconds (again, passed as a parameter).

```python
import asyncio

async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

async def main():
    async for x in ticker(1,10):
        print(x)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

## Asynchronous comprehensions

If I asked you to modify the previous example so to create a list using the generator you would probabily modify the code this way:

```python
import asyncio
​
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
​
async def main():
    mylist = []
    async for x in  ticker(1,10):
        mylist.append(x)
​
    print (mylist)
​
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

But wouldn't it be great if we could use list comprehensions like we normaly do? Now, we can:

```python
import asyncio
​
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
​
async def main():
​
    mylist = [await x async for x in  ticker(1,10)]
    print (mylist)
​
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

That's all for now, happy coding in Python 3.6!
