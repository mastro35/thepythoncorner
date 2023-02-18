---
title: When To Use Generators in Python
date: 2018-04-17T11:46:00+02:00
author: "davide_mastromatteo"
excerpt: "Let's talk about when to use generators in Python"
header:
  teaser: https://imgs.xkcd.com/comics/goto.png
categories:
  - Dev
tags:
  - Featured
  - Generators
  - Python
aliases:
  - /2018/04/generators-in-python-should-i-use-them
  - /2018/04/generators-in-python-should-i-use-them/
  - /dev/generators-in-python-should-i-use-them/
---
![teaser](https://imgs.xkcd.com/comics/goto.png)

Following a request of a reader, today we're going to discuss when to use iterators and generators in Python.

First of all, it's important to know what iterators and generators are, so if you don't know exactly what they are, I suggest to have a look at [my previous article](https://www.thepythoncorner.com/2016/11/iterators-and-generators-in-python/) on this topic.

Now that everything is clear, we can start analyzing when to use these features.

---

Let's start saying that if you have read my previous article, the use of the iterator protocol should be quite clear: you use iterator protocol when you have a custom object that you want to be "*iterable*".

That's it, so easy.

If you want to use your custom object in a loop with something like

```python
for i in my_object():
    # do something
    pass
```

you just need to adopt the iterator protocol.
But what about generators?

When am I supposed to write a generator instead of a simple function that returns a list of objects?

Well, I have to admit that this can be a little bit tricky for a beginner... so let's try to answer this question pretending to be there to write a function that returns a list of objects and let's answer the following questions.

## Do I need all the items of the returned list?

This is the first question you should ask yourself when writing a function that returns a list of objects. If the answer is "no", that probably means that a generator would be a better choice because its main feature is the "lazy evaluation".

With a generator, you generate a result **only when you really need it**, so if you're not going to use all the items in the list, why bother creating them?

You will save time and resources not creating them and your users will be happier!

To make an example, have a look at this program.

```python
import time
import random

def get_winning_numbers():
    random.seed()
    elements = []
    for i in range (0,10):
        time.sleep(1) # let's simulate some kind of delay
        elements.append(random.randint(1,10))

    return elements

random.seed()
my_number = random.randint(1,10)
print ("my number is " + str(my_number))

for winning_number in get_winning_numbers():
    print(winning_number)
    if my_number == winning_number:
        print ("you win!")
        break
```

The function "get_winning_numbers" is a time-consuming function that generates 10 random "winning numbers" (to simulate the "time-consuming function" we have added a delay of a second for every number generated).

The winning numbers are then checked against "my_number"; if my_number is in these 10 numbers, the player wins and the execution ends.

Made in this way, however, you have always to wait at least 10 seconds because all the winning numbers **are all generated before **the check against the player lucky number. That's a waste of time because if the first of the winning numbers were the player's number, we'd had generated 9 other winning numbers (using a time-consuming function) that we don't need and that we will never use.

Using a generator, we can solve this problem pretty easily:

```python
import time
import random

def get_winning_numbers():
    random.seed()
    for i in range(0,10):
        time.sleep(1)  # let's simulate some kind of delay
        yield random.randint(1,10)

random.seed()
my_number = random.randint(1,10)
print ("my number is " + str(my_number))

for winning_number in get_winning_numbers():
    print(winning_number)
    if my_number == winning_number:
        print ("you win!")
        break
```

We don't need to make a big change to our program, we have the same result but the execution is often faster than the old version. In fact, now if the first winning number is equal to the lucky number of the player, we generate just that number, the player wins and the execution ends in just one second.

## Do I need to be notified while the results of the list are generated?

If the answer to this question is yes, well, you will probably need a generator.

Think about a function that searches something on your filesystem or any other slow device and returns a list of results. If your function takes 5 seconds to find every single element and there are just 4 elements to be found, you have to wait 20 seconds before getting the results.

```python
import time

def elements():
    elements = []
    for i in range (0,4):
        # simulate a slow search
        time.sleep(5)
        elements.append(i)
    return elements

print("start")
print(elements())
print("end")
```

In this case, even if you need all the four elements before going on, your app will seem to be frozen for 20 seconds, and this could be annoying for the user.

Wouldn't it be better to be notified after every result, even just to have the time to update the user interface, maybe showing the partial results found or even a simple progress bar?

```python
import time

def elements():
    elements = []
    for i in range (0,4):
        # simulate a slow search
        time.sleep(5)
        yield(i)

print("start")
for i in elements():
    # show a "console style" progress bar  :)
    print(".", end="", flush=True)
print()
print("end")
```

## Is the memory footprint of the function I'm writing relevant?

If the answer is "yes", it's probably a good idea to use a generator.

That's because with a generator you create a result just when you need it and after the result has been created you can start working on it, removing it from the memory when you have finished and before asking for another item.

Let's say that your function is supposed to return a huge list of big objects, to return a single list you have to create that list and keep it all in memory.

```python
import time

def get_elements():
    elements = []
    for i in range (0,10000):
        elements.append("x"*10240)
    # return a list of 10.000 items, each of 10KB...
    return elements

characters_count = 0

my_elements=get_elements()
# in this moment, our program has a memory footprint of more than 100MB!!!

for i in my_elements:
    characters_count = characters_count + len(i)

print(characters_count)
```

As you see, in this case, we are allocating more than 100MB RAM before actually doing anything... But using a generator...

```python
def get_elements():
    for i in range (0,10000):
        yield("x"*10240)

characters_count = 0

my_elements=get_elements()

for i in my_elements:
    characters_count = characters_count + len(i)

print(characters_count)
```

we get the same result with just 10KB RAM used at a time.

---

Now I can hear you wondering "well, I have to use generators if the function that creates an element is time-consuming, if the memory footprint of that function is relevant or if I don't need all the elements of the list, but in every other case it's ok to create a list, right?"... Well, it could be ok... but... even in this case, why not to use a generator? A generator, for me, is always a better choice and consider that if you have a generator, converting it in a list is a trivial operation that can be done by using the "list" keyword like that.

```python
mylist = list(my_generator())
```

or by using list comprehension syntax

```python
mylist = [element for element in my_generator()]
```

To sum up: **ask not** "*why should I use a generator?*" but ask "*why shouldn't I?*"

:)

Happy Coding!

D.
