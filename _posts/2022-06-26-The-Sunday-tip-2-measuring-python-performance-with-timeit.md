---
title: "Measuring Python code performance with the timeit module"
date: 2022-06-26T00:04:22+01:00 
author: Davide Mastromatteo
excerpt: "Good code is also code that performs well, here's how you can measure your code's performance in Python"
header:
    teaser: https://imgs.xkcd.com/comics/hypothesis_generation.png
categories:
    - Dev
tags:
    - performance
    - Sunday_Tips
    - python
    - timeit
redirect_from:
    - /posts/2022-06-26-the-sunday-tip-2-measuring-python-performance-with-timeit/
---

![hypotesis_generation](https://imgs.xkcd.com/comics/hypothesis_generation.png)

Hi guys, this week'shttps://thepythoncorner.com/posts/2022-06-26-the-sunday-tip-2-measuring-python-performance-with-timeit/ tip is about measuring the performance of your Python code. 
Maybe you left your cubicle last Friday with some piece of code that wasn't performing well? Well, today you will learn how to measure it! :)

## The timeit module

We all know that Python comes with *batteries included* because in its standard library there are a lot of tools that you can easily use out of the box. 
One of theese tools is the `timeit` module.

The `timeit` module allows you to measure how much time is taken for a specific python piece of code. In short, it takes your piece of code, runs it a million times, and then returns you the execution time of the run.

Ok, let's start with an example. 
You have been asked to write a small function that takes a list of strings and returns a single string that is the concatenation of all the strings in the list.

Here is your piece of code:

```python
def concatenate(list: [str]):
    result = ""
    for string in list:
        result = result + "," + string

    return result
```

It was easy, wasn't it?

Now we need to test it... let's write some code to test it.

```python
def concatenate(list: [str]):
    result = ""
    for string in list:
        result = result + "," + string

    return result
    
if __name__ == '__main__':
    import random
    import string

    my_list = []
    for _ in range(100):
        my_string = ""
        for _ in range(10):
            my_string = my_string + random.choice(string.ascii_uppercase) 
        my_list.append(my_string)

    result = concatenate(my_list)
    print(result)
```

Ok, now we have added some code to create a random list of 100 ten-chars-strings and to call our `concatenate()` function. 
Running the program we can see that the program works... but how fast is it?

Let's find it out with the `timeit()` function of the `timeit` module!

The signature of the function we will use is the following: 

```python
timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
```

So in our code we can import the `timeit` module and use this function, where: 

- `stmt` is the statement to be tested, written as a string
- `setup` is an optional string that you can use to setup the environment before starting
- `timer` is an optional parameter to specify the timer we want to use (by default it is the `time.perf_counter()` timer)
- `number` is the number of times the code has to be executed, by default is a million times
- `globals` is an optional parameter that is useful if you want to specify a namespace where to execute your code

Let's try it: 

```python
def concatenate(list: [str]):
    result = ""
    for string in list:
        result = result + "," + string

    return result
    
if __name__ == '__main__':
    import random
    import string
    import timeit

    my_list = []
    for _ in range(100):
        my_string = ""
        for _ in range(10):
            my_string = my_string + random.choice(string.ascii_uppercase) 
        my_list.append(my_string)

    print(timeit.timeit("concatenate(my_list)", globals=globals()))
```

Please note that in our example it was important to specify the `globals` parameter to specify in which namespace the module could have found the function we wrote.
Running the example on my Intel-based MacBook pro what I got is:

```console
$ python timeit1.py
24.02475388700077
```

Ok, let's face it, this code sucks guys...


> Please note that during the execution, the `timeit()` function disables the garbage collector to have the single measurements more comparable. This is usually ok but sometimes it can be useful to measure it because garbage collections can be an important aspect to consider talking about performance. In this case, consider that you can reenable the garbage collection just by adding `gc.enable()` to the `setup` parameter.


However, as you may know, there's a better way to concatenate strings in Python and it's done by using the `.join()` method of a string object. 
So in our case, our code could be written like this: 

```python
def concatenate(list: [str]):
    return ",".join(list)
    
if __name__ == '__main__':
    import random
    import string
    import timeit

    my_list = [("".join(random.choice(string.ascii_uppercase) for _ in range(10)) for _ in range(100)]
    
    print(timeit.timeit("concatenate(my_list)", globals=globals()))
```

Yes, in the previous code we had /reinvented the wheel/... and by the way: if you are asking how I created the `my_list` list in this last example, check out my article about [list comprehension](https://thepythoncorner.com/posts/2016-11-22-iterators-generators-python/).

Now, let's run this code and see what we get:

```console
$ python timeit2.py
1.2398378039997624
```

Ok, we have optimized our code by 95%, let's call it a day! ;)

## So, what have we learned?

- to measure a Python piece of code the best method is to use the `timeit` module of the standard library
- optimizing your code is super important
- the standard library is your friend :)

The `timeit` module has a lot of other features that we haven't discussed in this article, to find out more, refer to the standard library [official documentation](https://docs.python.org/3/library/timeit.html).

Happy Sunday!

D
