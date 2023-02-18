---
title: Speed up your code by using a cache in Python
date: 2018-04-26T11:26:00+02:00
author: "davide_mastromatteo"
excerpt: Did you know you can make your application lot faster just with a couple lines of code and a local cache?
header:
  teaser: https://imgs.xkcd.com/comics/refresh_types.png
categories:
  - Dev
tags:
  - Cache
  - Featured
  - Performance
  - Python
aliases:
  - /2018/04/how-to-make-your-code-faster-by-using-a-cache-in-python
  - /2018/04/how-to-make-your-code-faster-by-using-a-cache-in-python/
  - /dev/how-to-make-your-code-faster-by-using-a-cache-in-python/ 
---
![teaser](https://imgs.xkcd.com/comics/refresh_types.png)

If the first concern of a developer is to be sure that the code they write works well, the second one is to make sure that it run fast. This is expecially true when you're dealing with web applications, where the scalability of your application is a crucial topic. For this reason, one of the most important tool we can use to improve the speed of our code is the use of a cache system.

A cache system is a component that stores data so that future requests for data we already served in the past, could be accomplished faster. There are a lot of solutions that can be used to implement a cache system but today I want to point out a specific solution that allows your Python code to use a cache for everyday use, without setting up a complex (and yet more powerful) system like [Redis](http://redis.io) or other: the package [cachetools](https://pypi.org/project/cachetools/).

As always, let's make the code talk for us! :)

It goes without saying that to use the package cachetools we need to install it, so before trying the code in this article, please install the required package:

```console
pip install cachetools
```

As always, my advise is to install everyting into a virtual environment. If you don't know what a virtual environment is or how to use it, [check my previous article](https://www.thepythoncorner.com/2016/11/using-virtual-environments-with-python/) about this topic.

Now, let's pretend that you have an application with a very time consuming function that you call many times in your code, with 100 different parameters, but the result you get, if the input parameter remain the same, doesn't change very often. To make it more concrete, let's say that your work is to sell candies, and you have 100 different kind of candies in stock.

In the cash register's python source code, you have a function that check the price of a single candy by connecting with a web service of a server in the cloud. Unfortunately, this web service is very slow to response (you should fire the guy who wrote it maybe), so this function that check the price is always very slow.

Here is your code:

```python
import time
import datetime

def get_candy_price(candy_id):
    # let's use a sleep to simulate the time your function spends trying to connect to
    # the web service, 5 seconds will be enough.
    time.sleep(5)

    # let's pretend that the price returned by the web service is $1 for candies with a
    # odd candy_id and $1,5 for candies with a even candy_id

    price = 1.5 if candy_id % 2 == 0 else 1

    return (datetime.datetime.now().strftime("%c"), price)


# now, let's simulate 20 customers in your show.
# They are asking for candy with id 2 and candy with id 3...
for i in range(0,20):
    print(get_candy_price(2))
    print(get_candy_price(3))
```

As you can see, the get_candy_price is very slow (we have put a "sleep" in the function to simulate the slowness due to the bad web service we are relying on).

What can we do?

Well, this seems the perfect function that can benefit from the use of a cache system. The candy price is not going to vary so often and even if it change, we could assume that it's ok if it's updated on our system within 5 minutes, with no hurry.

So, how can we implement this behaviour?
It's super easy, we need just three code lines.

```python
import time
import datetime

from cachetools import cached, TTLCache  # 1 - let's import the "cached" decorator and the "TTLCache" object from cachetools
cache = TTLCache(maxsize=100, ttl=300)  # 2 - let's create the cache object.

@cached(cache)  # 3 - it's time to decorate the method to use our cache system!
def get_candy_price(candy_id):
    # let's use a sleep to simulate the time your function spends trying to connect to
    # the web service, 5 seconds will be enough.
    time.sleep(5)

    # let's pretend that the price returned by the web service is $1 for candies with a
    # odd candy_id and $1,5 for candies with a even candy_id

    price = 1.5 if candy_id % 2 == 0 else 1

    return (datetime.datetime.now().strftime("%c"), price)


# now, let's simulate 20 customers in your show.
# They are asking for candy with id 2 and candy with id 3...
for i in range(0,20):
    print(get_candy_price(2))
    print(get_candy_price(3))
```

Can you spot the three new lines?

The first one is the import statement that we need to use the cachetools package.

The second one is the line to create the cache. We need to specify how many objects we will store (100, because we have just 100 kind of candies) and the time each cached results have to live (300 seconds, 5 minutes for us).

The third line is the decorator, that enable the function to use the cached results.

Now try to execute this program again and you will notice that the first time the function is called (with parameter "2") it takes 5 seconds to be executed (yes, the cache is empty at that time) and so it does the second time the function is called (with parameter "3") because in the cache there's just the result for the candy_id 2 that can't be used since we are asking for the candy_id 3. But from the third call on, every single call is super fast, since the body of the method is NOT executed at all. The results we get are just taken from the cache system. Isn't that cool?

## Cachetools' cache type

In the example above we have used a "Time To Live Cache". This cache associates a time to live value to each item stored in cache. Items that expire because they have exceeded their time-to-live are removed automatically, making room for new values. If no expired items are there to remove, the least recently used items will be discarded first to make space when necessary.

Other kinds of cache that are available in the cachetools package are:

- the *LFUCache* (Least Frequently Used), that counts how often an item is retrieved, and discards the items used least often to make space when necessary.
- the *LRUCache* (Least Recently Used), that discards the least recently used items first to make space when necessary.
- the *RRCache* (Random Replacement), that randomly selects candidate items and discards them to make space when necessary.

And all these cache types can be used in a decorator of a function, like we did it before, or simply by creating a cache object and using it directly, choosing at run time what to add to the cache and when to retrieve the values added.

## The drawbacks

One thing a wise person should always keep in consideration is that

> not all that glitters is gold

A cache system bring also some disadvantages.

The first and more obvious one is that cached data are  (by definition )  "old". That means that when you reuse these old data, you run the risk of presenting data that are no more relevant in the new context. In the example that we've seen before, if you are selling candies you can assume that a five minutes delay in retrieving the candy price from the server is fair enough to reuse the cached data. But if you were in a different context, and you were getting the current Bitcoin value, reuse a five minutes old result could be the most stupid thing to do. :)

Another thing that you have to keep in mind when using a cache is that the data you are caching are not stored in "Eega Beeva's pockets", they are stored in your RAM. So, if you cache 100 complex objects that are 5 Megabytes each, you are storing 500 Megabytes in the ram of your server.

> Developing is often a matter of tradeoffs, think about it not only when you have to decide if to use a cache or not, but always when you start designing a software solution.

Ok, that's all folks, if you want to dig in this topic, go and check [the documentation of the cachetools package](http://cachetools.readthedocs.io/en/latest/).ù

Happy caching! :)

D.
