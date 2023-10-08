---
title: Python cached integers"
date: 2022-06-19T00:07:35+01:00
author: "davide_mastromatteo"
excerpt: "Did you know that Python compiler optimize your program caching small integers?" 
header:
    teaser: https://imgs.xkcd.com/comics/compiling.png
categories:
    - Dev
tags:
    - Internals
    - Sunday_Tips
    - python
    - Interpreter
    - Compiler
---
![compiling](https://imgs.xkcd.com/comics/compiling.png)

Hey guys, today's post is just a small tip about...\

## Python integer cache.

Let's start with an example, open your REPL and try this:

```python
>>> a = 666
>>> b = 666
>>> a is b
>>> False
```

As you can see we have assigned the value `666` to the variable `a` and then the value `666` to the variable `b`.
Unsurprisingly, the two variables are pointing to two different objects.

So, what's strange with that?

Well... nothing... unless the interpreter doesn't behave differently depending on the number we assign... 
Let's try with this second example:

```python
>>> a = 3
>>> b = 3
>>> a is b
>>> True
```

What? Why the two variables `a` and `b` are now pointing to the same obejct?

No, you Python interpreter is not /religious/, it doesn't consider the number `3` better or worse than the 
number `666`, it just cache the values between `-5` and `256` for performance reasons.

That's cool uh?

Yes, but this is what I get with the REPL, would it be the same with the compiler?
Well, apparently the compiler behave in a different way and analyzing your script, it may decide to 
cache also different numbers:

```python
a = 3
b = 3
c = 666
d = 666
e = 5.5
f = 5.5
g = 11 / 2

print (a is b)
print (c is d)
print (e is f)
print (f is g)
```

And running this example you will get:

```console
True
True
True
False
```

## So, what have we learned?

- your compiler *does* optimize more than you think
- what you get in the REPL is not always identical to what you get from the compiler
- even float numbers may be cached
- not *every* number is cached ;)


Happy Sunday!

D
