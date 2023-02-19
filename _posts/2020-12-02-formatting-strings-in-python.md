---
title: "Formatting strings in Python: the easyway by using f-strings"
date: 2020-12-02T22:09:35+01:00
author: "davide_mastromatteo"
excerpt: "Formatting a string is an easy operation in Python that almost any developer can do. But are you sure you're doing it right?"
header:
  teaser: https://imgs.xkcd.com/comics/string_theory.png
categories:
  - Dev
tags:
  - strings
  - concatenating strings
  - formattin strings
  - f-string
  - python
redirect_from:
  - /dev/formatting-strings-in-python/
---
![teaser](https://imgs.xkcd.com/comics/string_theory.png)

Concatenating and formatting strings in Python is a trivial operation that almost any developer should be able to do, right?
And yet, many devs keep using old stuff to format strings, like the `%` operator or the `.format()` method.

But that's the last-century way to format strings! I mean... the `%` method is something prehistoric that was used in Python 2 and the `.format()` method is so... 2008... :)

If you are using at least Python 3.6 (that is 4 years old right now) the way you should format string is by using the f-string syntax.

Let's try some examples.
If you are a cavem... I mean... if you're the oldest man... Ops... no, I mean... If you are an *experienced* Python dev, you are probably used to the `%` operator. That's how it works:

```python
name = "Dave"
print("Hi, I'm %s, and I'm stuck with the %% operator..." % name)
print("Hi %s..." % name)
```
And this is what you get:

```console
Hi, I'm Dave, and I'm stuck with the % operator...
Hi Dave...
```

This is the oldest way to format strings in Python. Note that the `s` after the `%` operator is used to tell the compiler what type of variable we are replacing there (in this case, a string). We could use other types, like `%d` for integers, `%f` for floating-point numbers, or `%x` for hex representation of a number.

Python 3 introduced a *new* way to format strings: the string's `.format()` method.

As you probably know, in Python everything is an object, and a string object has methods that allow you to manipulate the string itself. 
So, starting with Python 3, you can use this method like this:

```python
name = "Dave"
age = 42
print("Hi, I'm {}, I'm just {} but I feel like I'm stuck in 2008...".format(name, age))
print("Hi {}...".format(name))
```
Running this example you will get the following result:

```console
Hi, I'm Dave, I'm just 42 but I feel like I'm stuck in 2008...
Hi Dave...
```

Is this better than the `%` operator? I actually don't think so... I mean... this is too verbose, and in the example above I kept the syntax the most concise I could, without naming the arguments or inserting the ordinal position of the argument in the brackets.

But wouldn't it be great if I could insert into the placeholder the variable that I wanted to print? Well, since Python 3.6, this can be done with f-strings!

You just need to prefix an `f` character before the string and this will allow you to insert in curly braces the variable you want to eplace.
For example:

```python
name = "Dave"
print(f"Hey guys, I'm {name} and I've just learned f-strings!")
```

and that's will print:

```console
Hey guys, I'm Dave and I've just learned f-strings!
```

Super easy and super cool uh?

And note that the substitutions are evaluated at runtime, so you can put inside your strings calls to methods, operation, etc... like in the following example.

```python
name = "Dave"
print(f"Hey guys, I'm {name.upper()}, I'm {2020-1978} and I've just learned f-strings!")
```

And running this example you will get the following output:

```console
Hey guys, I'm DAVE, I'm 42 and I've just learned f-strings!
```

Ok guys, I hope you enjoyed this article that I wanted to keep short, like a small tip. If you need more information go and see [PEP 498](https://www.python.org/dev/peps/pep-0498/) and if you have found this helpful, consider the idea of buying me a coffee by clicking on the banner below. This will help me keep up the site, the newsletter and everything else that makes "The Python Corner" a good place to visit.

Happy coding!
D.
