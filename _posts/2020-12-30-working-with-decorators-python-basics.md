---
title: "Working with decorators in Python - The Basics"
date: 2020-12-30T12:55:36+01:00
author: "davide_mastromatteo"
excerpt: "Decorators are a powerful feature that Python offers out of the box to write better and reusable code. Do you know them?"
header:
  teaser: https://imgs.xkcd.com/comics/bad_code.png
categories:
  - Dev
tags:
  - decorators
  - functions
  - python
redirect_from:
  - /dev/working-with-decorators-python-basics/
---
![teaser](https://imgs.xkcd.com/comics/bad_code.png)

Hi Guys, in today’s article, we will discuss Python decorators.

Decorators are not a python-only feature, they exist in many other languages and are important if you aim to write clean, professional, and reusable code.

A decorator is a function that extends other functions that are passed as a parameter, adding new features without the need of changing their code.

This can seem a little magical to a beginner's eye, but it's really easy actually because all you have to do is to create a function (the so-called "*decorator function*") that takes another function as an argument (the "*decorated function*") and returns **a completely new function** that simply modify the behavior of your decorated function. That's made possible by the fact that in Python, functions are **first-class citizens** and can be passed as arguments to other functions. I [wrote a post](http://thepythoncorner.com/dev/lambdas-and-functions-in-python/) about that if you're interested in this topic.

It may seem something difficult that needs a 5000 words article to be explained... but it's not! Let's see a practical example.

Let's pretend we are writing a program that prints out 10 integers between 0 and 100.
This is a possible implementation:

```python
import random

def get_rnd():
    return random.randrange(100)

for i in range(1,11):
    my_random_number = get_rnd()
    print (f"Number {i}: {my_random_number}")
```

This script is quite trivial and if you run it you will see 10 random numbers. This is the output I got:

```console
Number 1: 54
Number 2: 28
Number 3: 82
Number 4: 12
Number 5: 94
Number 6: 14
Number 7: 57
Number 8: 73
Number 9: 51
Number 10: 72
```

> Nice formatted output uh? That's because I've used f-strings! Go and check out more [with my article about f-strings](https://thepythoncorner.com/dev/formatting-strings-in-python/).

Now let's pretend that you are asked to extract not just 10 numbers, but 10 **odds** numbers. How can you modify your program? One possibility is to test the number inside the `get_rnd()` function and just keep extracting until an odd number gets extracted. This is a solution, but another approach could be leaving the `get_rnd()` function unmodified and create a *decorator function* to modify the behavior of the get_rnd() function. 

Let's try it! 
At first we will write a *decorator function* named `only_odd()` that will take a function as a parameter (later we will pass the `get_rnd()` function as a parameter). Inside this function, we will define **another** function (the `inner()` function) that just keeps calling the `get_rnd()` functions until an odd number is returned.

Here's the code of our decorator:

```python
def only_odd(func):
    def inner(): # here we define a new function that will be returned
        while True: 
            my_number=func() # this function will just keep calling func
            if my_number%2!=0:  # until a odd number is returned
                return my_number
            else:
                print(f"{my_number} is even, retry...")
    return inner
```

Yes, this is a decorator. 
Now, our program could be modified like this:

```python
import random

def only_odd(func):
    def inner():
        while True:
            my_number=func()
            if my_number%2!=0:
                return my_number
            else:
                print(f"{my_number} is even, retry...")
    return inner

def get_rnd():
    return random.randrange(100)

for i in range(1,11):
    # here we create a decorated function...
    my_new_decorated_function_to_get_random_odd = only_odd(get_rnd)
    # ... that we will call to get a random odd
    my_random_number = my_new_decorated_function_to_get_random_odd()
    print (f"Number {i}: {my_random_number}")
```

And now, if I run this program, what I get is:

```console
Number 1: 85
Number 2: 97
Number 3: 21
10 is even, retry...
Number 4: 21
Number 5: 57
52 is even, retry...
50 is even, retry...
42 is even, retry...
70 is even, retry...
Number 6: 17
Number 7: 7
Number 8: 79
44 is even, retry...
Number 9: 95
Number 10: 83
```

You can see that our decorator has worked great and each time the `get_rnd()` function returned an even number, it kept calling it again to wait for an odd one.

Cool! But look at our new call:

```python
    # here we create a decorated function...
    my_new_decorated_function_to_get_random_odd = only_odd(get_rnd)
    # ... that we will call to get a random odd
    my_random_number = my_new_decorated_function_to_get_random_odd()
    print (f"Number {i}: {my_random_number}")
```
We decided to use a decorator because we wanted to modify the behavior of our `get_rnd()` function without affecting the caller, that's not what we have now.
Luckily, Python here helps us with some "syntax sugar".

In fact, we can decorate our `get_rnd()` just by using the `@` symbol, followed by the name of our decorator function, before the declaration of the function we want to decorate.
Doing this, we don't need anything else to call our decorated function, and our program could be like this:

```python
import random

def only_odd(func):
    def inner():
        while True:
            my_number=func()
            if my_number%2!=0:
                return my_number
            else:
                print(f"{my_number} is even, retry...")
    return inner

@only_odd # this decorate our get_rnd() function
def get_rnd():
    return random.randrange(100)

for i in range(1,11):
    my_random_number = get_rnd() # look, no change to the caller!
    print (f"Number {i}: {my_random_number}")
```

Isn't that cool?
And the coolest part is that our `@only_odd` decorator can be reused on all the functions that return a single integer. 
For example, let's say that we have also a function that takes a numeric input from user keyboard and returns an integer, like this:

```python
def square_input():
 while True:
    input_text=input("Enter a number:")
    try:
        input_number = int(input_text)
        return(input_number**2)
    except:
        print("not a number")
```

If we wanted to keep asking for numbers until the result is an odd number, we just need to decorate our function. 

Here's our example modified:

```python
import random

def only_odd(func):
    def inner():
        while True:
            my_number=func()
            if my_number%2!=0:
                return my_number
            else:
                print(f"{my_number} is even, retry...")
    return inner

@only_odd # this decorate our get_rnd() function
def get_rnd():
    return random.randrange(100)

@only_odd # this decorate our square_input() function
def square_input():
 while True:
    input_text=input("Enter a number:")
    try:
        input_number = int(input_text)
        return(input_number**2)
    except:
        print("not a number")

print("Your odd numbers:")
for i in range(1,11):
    my_random_number = get_rnd() # look, no change to the caller!
    print (f"Number {i}: {my_random_number}")

print("---")

print("Now, let's play with squares:")
my_squared_input = square_input()
print (f"The square of your number is {my_squared_input}")
```

And running the previous example I got this output:

```console
Your odd numbers:
28 is even, retry...
54 is even, retry...
Number 1: 81
Number 2: 81
62 is even, retry...
2 is even, retry...
44 is even, retry...
26 is even, retry...
Number 3: 59
Number 4: 87
60 is even, retry...
Number 5: 29
78 is even, retry...
Number 6: 83
Number 7: 25
Number 8: 79
Number 9: 71
50 is even, retry...
82 is even, retry...
70 is even, retry...
0 is even, retry...
36 is even, retry...
Number 10: 3
---
Now, let's play with squares:
Enter a number:4
16 is even, retry...
Enter a number:77
The square of your number is 5929
```

Ok guys, let's call this an article! :)
In this first part, I introduced you to the wonderful world of decorators, in the next one I will show you some other powerful use of decorators, like how to use decorators with arguments or how to decorate a function that can take arguments itself.

So... stay tuned for the next one! 

Happy Coding and ... happy new year!
D.

Note: All the code above has been tested using [Pyto](https://apps.apple.com/it/app/pyto-python-3/id1436650069) iOS app on a simple iPhone. It has been great being able to write an article without having access to a real full-size computer running a Python interpreter, so let me reccomend this great piece of freemium software. 
