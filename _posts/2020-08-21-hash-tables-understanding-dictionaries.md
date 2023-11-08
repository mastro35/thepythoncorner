---
title: "Python Hash Tables: Understanding Dictionaries"
date: 2020-08-21T06:59:49+01:00
author: Davide Mastromatteo
excerpt: "Dictionaries are a really important part of Python but how can they be so fast and reliable? The answer is about Hash Tables..."
header:
  teaser: https://imgs.xkcd.com/comics/password_strength.png
categories:
  - Dev
tags:
  - hash tables
  - dictionaries
  - python
redirect_from:
  - /dev/hash-tables-understanding-dictionaries/
  - /posts/2020-08-21-hash-
---
![teaser](https://imgs.xkcd.com/comics/password_strength.png)

Hi guys, have you ever wondered how can Python dictionaries be so fast and reliable? The answer is that they are built on top of another technology: **hash tables**.

Knowing how Python hash tables work will give you a deeper understanding of how dictionaries work and this could be a great advantage for your Python understanding because dictionaries are almost everywhere in Python.

## Hash Functions

Before introducing hash tables and their Python implementation you have to know what is a hash function and how it works.

A hash function is a function that can map a piece of data of any length to a fixed-length value, called **hash**.

Hash functions have three major characteristics:

1. They are **fast to compute**: calculate the hash of a piece of data have to be a fast operation.
2. They are **deterministic**: the same string will always produce the same hash.
3. They produce **fixed-length** values: it doesn't matter if your input is one, ten, or ten thousand bytes, the resulting hash will be always of a fixed, predetermined length.

Another characteristic that is quite common in hash functions is that they often are **one-way functions**: thanks to a voluntary data loss implemented in the function, you can get a hash from a string but you can't get the original string from a hash. This is not a mandatory feature for every hash functions but becomes important when they have to be cryptographically secure.

Some popular hash algorithms are [MD5](https://en.wikipedia.org/wiki/MD5), [SHA-1](https://en.wikipedia.org/wiki/SHA-1), [SHA-2](https://en.wikipedia.org/wiki/SHA-2), [NTLM](https://it.wikipedia.org/wiki/NTLM).

If you want to try one of these algorithms by yourself, just point your browser to https://www.md5online.org, insert a text of any length in the textbox, click the `crypt` button and get your 128bit MD5 hash back.

## Common Usages of Hashes

There are a lot of things that rely on hashes, and hash tables are just one of them. Other common usages of hashes are for cryptographic and security reasons.

A concrete example of this is when you try to download open-source software from the internet. Usually, you find also a companion file that is the signature of the file. This signature is just the hash of the original file and it's very useful because if you calculate the hash of the original file by yourself and you check it against the signature that the site provides, you can be sure that the file you downloaded hasn't have tampered.

Another common use of hashes is to store user passwords. Have you ever asked yourself why when you forget the password of a website and you try to recover it the site usually lets you choose another password instead of giving back to you the original one you chose? The answer is that the website doesn't store the entire password you choose, but just its hash. 

This is done for security reasons because if some hacker got the access to the site's database, they won't be able to know your password but just the hash of your password, and since hash functions are often one-way functions you can be sure that they will never be able to get back to your password starting from the hash.

## The Python `hash()` Function

Python has a built-in function to generate the hash of an object, the `hash()` function.
This function takes an object as input and returns the hash as an integer.

Internally, this function invokes the `.__hash__()` method of the input object, so if you want to make your custom class hashable, all you have to do is to implement the `.__hash__()` method to return an integer based on the internal state of your object.

Now, try to start the Python interpreter and play with the `hash()` function a little bit. For the first experiment, try to hash some numeric values:

```pycon
>>> hash(1)
1
>>> hash(10)
10
>>> hash(10.00)
10
>>> hash(10.01)
230584300921368586
>>> hash(-10.01)
-230584300921368586
```

If you are wondering why these hashes seems to have different length remember that the Python `hash()` function returns **integers** objects, that are always represented with 24 bytes on a standard 64 bit Python 3 interpreter.

As you can see, by default the hash value of an integer value is the value itself. Note that this works regardless of the type of the value you are hashing, so the integer `1` and the float `1.0` have the same hash: `1`.

What's so special about this? Well, this shows what you learned earlier, that is that hash functions are often one-way functions: if two different objects may have the same hash, it's impossible to do the reverse process starting from a hash and going back to the original object. In this case, the information about the type of the original hashed object has gone lost.

Another couple of interesting things you could note by hashing numbers is that decimal numbers have hashes that are different from their value and that negative values have negative hashes. But what happens if you try to hash the same number you got for the decimal value? The answer is that you get the same hash, as shown in the following example:

```pycon
>>> hash(0.1)
230584300921369408
>>> hash(230584300921369408)
230584300921369408
>>> hash(0.1) == hash(230584300921369408)
True
```

As you can see, the hash of the integer number `230584300921369408` is the same as the hash of the number `0.1`. And this is perfectly normal if you think of what you learned earlier about hash functions because if you can hash any number or any string getting a fixed-length value since you can't have infinite values represented by a fixed-length value, that implies that there must be duplicated values. They exist in fact, and they are called **collisions**. When two objects have the same hash, it is said that they collide.

Hashing a string is not much different from hashing a numeric value. Start your Python interpreter and have a try hashing a string:

```pycon
>>> hash("Bad Behaviour")
7164800052134507161
```

As you can see a string is hashable and produce a numeric value as well but if you have tried to run this command you could see that your Python interpreter hasn't returned the same result of the example above. That's because starting from Python 3.3 values of strings and bytes objects are **salted** with a random value before the hashing process. This means that the value of the string is modified with a random value that changes every time your interpreter starts, before getting hashed. If you want to override this behaviour, you can set the `PYTHONHASHSEED` environment variable to an integer value greater than zero before starting the interpreter.

As you may expect this is a security feature. Earlier you learned that websites usually store the hash of your password instead of the password itself to prevent an attack to the site's database to stole all the site passwords. If a website stores just the hash as it is calculated it could be easy for attackers to know what was the original password. They just need to get a big list of commonly used passwords (the web is full of these lists) and calculate their corresponding hash to get what is usually called **rainbow tables**.

By using a rainbow table the attacker may not be able to get **every** password in the database, still being able to steal a **vast majority of them**. To prevent this kind of attack, a good idea is to **salt** the password before hashing them, which is modifying the password with a random value before calculating the hash.

Starting from Python 3.3 the interpreter by default salt every string and bytes object before hashing it, preventing possible DOS attacks as demonstrated by Scott Crosby and Dan Wallach on [this 2003 paper](https://static.usenix.org/event/sec03/tech/full_papers/crosby/crosby_html/).

A DOS attack (where DOS stands for Denial Of Service) is an attack where the resources of a computer system are deliberately exhausted by the attacker so that the system is no longer able to provide service to the clients. In this specific case of the attack demonstrated by Scott Crosby, the attack was possible flooding the target system with a lot of data whose hash collide, making the target system use a lot more of computing power to resolve the collisions.

## Python Hashable Types

So at this point, you could wonder if any Python type is hashable.
The answer to this question is no, by default, just immutable types are hashable in Python. In case you are using an immutable container (like a tuple) also the content should be immutable to be hashable.

Trying to get the hash of an unashable type in Python you will get a `TypeError` from the interpreter as shown in the following example:

```pytb
>>> hash(["R","e","a","l","P","y","t","h","o","n"])
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

However, every custom defined object is hashable in Python and by default its hash is derived from it's id. That means that two different instance of a same class, by default have different hashes, as shown in the following example:

```pycon
>>> class Car():
...     velocity = 0
...     direction = 0
...     damage = 0
...
>>> first_car = Car()
>>> second_car = Car()
>>> hash(first_car)
274643597
>>> hash(second_car)
274643604
```

As you can see, two different instances of the same custom object by default have different hash values. However, this behavior can be modified by implementing a `.__hash__()` method inside the custom class.

## Hash Tables

Now that you know what a hash function is, you can start examining hash tables. A hash table is a data structure that allows you to store a collection of key-value pairs.

In a hash table, the key of every key-value pair must be hashable, because the pairs stored are indexed by using the hash of their keys. Hash tables are very useful because the average number of instructions that are necessary to lookup an element of the table is independent of the number of elements stored in the table itself. That means that even if your table grows ten or ten thousand times, the overall speed to look up a specific element is not affected.

A hash table is typically implemented by creating a variable number of **buckets** that will contain your data and indexing this data by hashing their keys. The hash value of the key will determine the correct bucket to be used for that particular piece of data.

In the example below, you can find an implementation of a basic hash table in Python. This is just an implementation to give you the idea of how a hash table could work because as you will know later, in Python there's no need to create your custom implementation of hash tables since they are implemented as dictionaries. Let's see how this implementation works:

```python
import pprint

class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None

    def __str__(self):
        return pprint.pformat(self.buckets) # here pformat is used to return a printable representation of the object

if __name__ == "__main__":
     capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa')
    ]
hashtable = Hashtable(capitals)
print(hashtable)
print(f"The capital of Italy is {hashtable.get_value('Italy')}")
```

Look at the `for` loop starting at line 9. For each element of the hashtable this code calculate the hash of the key (line 10), it calculate the position of the element in the bucket depending on the hash (line 11) and add a tuple in the bucket (line 12).

Try to run the example above after setting the environment varible `PYTHONHASHSEED` to the value `46` and you will get the the following output, where two buckets are empty and two other buckets contains two key-value pairs each:

```console
[[('United States', 'Washington D.C.'), ('Canada', 'Ottawa')],
 [],
 [],
 [('France', 'Paris'), ('Italy', 'Rome')]]
The capital of Italy is Rome
```

Note that if you try to run the program without having set the `PYTHONHASHSEED` variable, you may probably get a different result, because as you already know the hash function in Python, starting from Python 3.3 salts every string with a random seed before the hashing process. 

In the example above you have implemented a Python hash table that takes a list of tuples as input and organizes them in a number of buckets equal to the length of the input list with a modulo operator to distribute the hashes in the table.

However, as you can see in the output, you got two empty buckets while the other two have two different values each. When this happens, it's said that there's a **collision** in the Python hash table.

Using the standard library's `hash()` function, collisions in a hash table are unavoidable. You could decide to use a higher number of buckets and lowering the risk of incurring in a collision, but you will never reduce the risk to zero.

Moreover, the more you increase the number of buckets you will handle, the more space you will waste. To test this you can simply change the bucket size of your previous example using a number of buckets that is two times the length of the input list:

```python hl_lines="3"
class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements) * 2
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)
```

Running this example, I ended up with a better distribution of the input data, but I had however a collision and five unused buckets:

```console
[[],
 [],
 [],
 [('Canada', 'Ottawa')],
 [],
 [],
 [('United States', 'Washington D.C.'), ('Italy', 'Rome')],
 [('France', 'Paris')]]
The capital of Italy is Rome
```

As you can see, two hashes collided and have been inserted into the same bucket.

Since collisions are often unavoidable, to implement a hash table requires you to implement also a collision resolution method. The common strategies to resolve collisions in a hash table are:

* **open addressing**
* **separate chaining**

The separate chaining is the one you already implemented in the example above and consists of creating a chain of values in the same bucket by using another data structure. In that example, you used a nested list that had to be scanned entirely when looking for a specific value in an over occupied bucket.

In the open addressing strategy, if the bucket you should use is busy, you just keep searching for a new bucket to be used. 
To implement this solution, you need to do a couple of changes to both how you assign buckets to new elements and how you retrieve values for a key.
Starting from the `_assign_buckets()` function, you have to initialize your buckets with a default value and keep looking for an empty bucket if the one you should use has been already taken:

```python
    def _assign_buckets(self, elements):
        self.buckets = [None] * self.bucket_size

        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size

            while self.buckets[index] is not None:
                print(f"The key {key} collided with {self.buckets[index]}")
                index = (index + 1) % self.bucket_size

            self.buckets[index] = ((key, value))
```

As you can see, all the buckets are set to a default `None` value before the assignment, and the `while` loop keeps looking for an empty bucket to store the data.

Since the assignment of the buckets is changed, also the retrival process should change as well, because in the `get_value()` method you now need to check the value of the key to be sure that the data you found was the one you were looking for:

```python
    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        while self.buckets[index] is not None:
            key,value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self.bucket_size
```

During the lookup process, in the  `get_value()` method you use the `None` value to check when you need to stop looking for a key and then you check the key of the data to be sure that you are returning the correct value.

Running the example above, the key for `Italy` collided with a previously inserted element (`France`) and for this reason has been relocated to the first free bucket available. However, the search for `Italy` worked as expected:

```console
The key Italy collided with ('France', 'Paris')
[None,
 None,
 ('Canada', 'Ottawa'),
 None,
 ('France', 'Paris'),
 ('Italy', 'Rome'),
 None,
 ('United States', 'Washington D.C.')]
The capital of Italy is Rome
```

The main problem of the open addressing strategy is that if you have to handle also deletions of elements in your table, you need to perform logical deletion instead of physical ones because if you delete a value that was occupying a bucket during a collision, the other collided elements will never be found.

In our previous example, `Italy` collided with a previously inserted element (`France`) and so it has been relocated to the very next bucket, so removing the `France` element will make `Italy` unreachable because it does not occupy its natural destination bucket, that appears to be empty to the interpreter.

So, when using the open addressing strategy, to delete an element you have to replace its bucket with a **dummy value**, which indicates to the interpreter that it has to be considered deleted for new insertion but occupied for retrieval purposes.

## Dictionaries: Implementing Python Hash Tables

Now that you know what hash tables are, let's have a look at their most important Python implementation: dictionaries. Dictionaries in Python are built using hash tables and the **open addressing** collision resolution method.

As you already know a dictionary is a collection of key-value pairs, so to define a dictionary you need to provide a comma-separated list of key-value pairs enclosed in curly braces, as in the following example:

```pycon
>>> chess_players = {
...    "Carlsen": 2863,
...    "Caruana": 2835,
...    "Ding": 2791,
...    "Nepomniachtchi": 2784,
...    "Vachier-Lagrave": 2778,
... }
```

Here you have created a dictionary named `chess_players` that contains the top five chess players in the world and their actual rating.

To retrieve a specific value you just need to specify the key using square brackets:

```pycon
>>> chess_players["Nepomniachtchi"]
2784
```

If you try to access a non existing element, the Python interpreter throws a `Key Error` exception:

```pytb
>>> chess_players["Mastromatteo"]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
KeyError: 'Mastromatteo'
```

To iterate the entire dictionary you can use `.items()` method, that returns an iterable objects of all the key-value pairs in tuples:

```pycon
>>> for (k, v) in chess_players.items():
...     print(k,v)
... 
Carlsen 2863
Caruana 2835
Ding 2791
Nepomniachtchi 2784
Vachier-Lagrave 2778
```

To iterate over the keys or over the values of the Python dictionary, you can use the `.keys()` or the `.values()` methods as well:

```pycon
>>> chess_players.keys()
dict_keys(["Carlsen", "Caruana", "Ding", "Nepomniachtchi", "Vachier-Lagrave"])
>>> chess_players.values()
dict_values([2863, 2835, 2791, 2784, 2778])
```

To insert another element into the dictionary you just need to assign a value to a new key:

```pycon
>>> chess_players["Grischuk"] = 2777
>>> chess_players
{'Carlsen': 2863, 'Caruana': 2835, 'Ding': 2791, 'Nepomniachtchi': 2784, 'Vachier-Lagrave': 2778, 'Grischuk': 2777}
```

To update the value of an existing key, just assign a different value to the previously inserted key.

Please note that since dictionaries are built on top of hash tables, you can only insert an element if its key is **hashable**. If the key of your element is not hashable (like a list, for example), the interpreter throws an `TypeError` exception:

```pytb
>>> my_list = ["Giri", "Mamedyarov"]
chess_players[my_list] = 2764
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

To delete an element, you need to use the `del` statement, specifying the key you want to delete:

```pycon
>>> del chess_players["Grischuk"]
>>> chess_players
{'Carlsen': 2863, 'Caruana': 2835, 'Ding': 2791, 'Nepomniachtchi': 2784, 'Vachier-Lagrave': 2778}
```

Deleting an entry doesn't delete the actual value into the dictionary, it just replaces the key with a dummy value so that the **open addressing** collision resolution method will continue to work, but the interpreter handles all this complexity for you, ignoring the deleted element.

## The Pythonic Implementation of Python Hash Tables

Now you know that dictionaries are Python hash tables but you may wonder how the implementation works under the hood, so in this chapter, I will try to give you some information about the actual implementation of Python Hash Tables.

Bear in mind that the information I will provide here is based on recent versions of Python, because with Python 3.6 dictionaries have changed a lot and are now smaller, faster and even more powerful, as they are now **insertion ordered** (the **insertion ordered** guarantee has been implemented in Python 3.6 but has officially be recognized [by Guido in Python 3.7](https://mail.python.org/pipermail/python-dev/2017-December/151283.html)).

Try to create an empty Python dictionary and check its size and you will find out that an empty Python dictionary takes 240 bytes of memory:

```pycon
>>> import sys
>>> my_dict = {}
>>> sys.getsizeof(my_dict)
240
```

By running this example you can see that the basic occupation of a Python dictionary is 240 bytes. But what happens if you decide to add a value? Well, that's may seem odds, but the size doesn't change:

```pycon
>>> my_dict["a"] = 100
>>> sys.getsizeof(my_dict)
240
```

So, why the size of the dictionary hasn't changed? Because starting from Python 3.6 values are stored in a different data structure and the dictionary contains just a pointer to where the actual value is stored. Moreover, when you create an empty dictionary it starts creating a Python Hash Table with 8 buckets that are just 240 bytes long, so the first element in our dictionary hasn't changed the size at all.

Now try to add some more elements and see how your dictionary behaves, you will see that the dictionary grows:

```pycon
>>> for i in range(20):
...     my_dict[i] = 100
...     print(f"elements = {i+1} size = {sys.getsizeof(my_dict)}")
... 
elements = 1 size = 240
elements = 2 size = 240
elements = 3 size = 240
elements = 4 size = 240
elements = 5 size = 240
elements = 6 size = 368
elements = 7 size = 368
elements = 8 size = 368
elements = 9 size = 368
elements = 10 size = 368
elements = 11 size = 648
elements = 12 size = 648
elements = 13 size = 648
elements = 14 size = 648
elements = 15 size = 648
elements = 16 size = 648
elements = 17 size = 648
elements = 18 size = 648
elements = 19 size = 648
elements = 20 size = 648
```

As you can see, the dict has grown after you have inserted the sixth and the eleventh element, but why? Because to make our Python hash table fast and reduce collisions, the interpreter keeps resizing the dictionary when it becomes full for [two-third](https://mail.python.org/pipermail/python-list/2000-March/048085.html).

Now, try to delete all the elements in your dictionary, one at a time, and when you have finished, check the size again, you will find that even if the dictionary is empty, space hasn't been freed:

```pycon
>>> keys = list(my_dict.keys())
>>> for key in keys:
...     del my_dict[key]
...
>>> my_dict
{}
>>> sys.getsizeof(my_dict)
648
```

This happens because since dictionaries have a really small memory footprint and the deletion is not frequent when working with dictionaries, the interpreter prefers to waste a little bit of space than to dynamically resize the dictionary after every deletion. However, if you empty your dictionary by calling the `.clear()` method, since it is a bulk deletion, space is freed and it goes to its minimum of 72 bytes:

```pycon
>>> my_dict.clear()
>>> sys.getsizeof(my_dict)
72
```

As you may imagine, the first insertion on this dictionary will make the interpreter reserve the space for 8 buckets, going back to the initial situation.

## Conclusions

In this article you have learned what are hash tables and how are they implemented in Python.

A huge part of this article is based on [Raymond Hettinger's speech](https://pyvideo.org/pycon-us-2017/modern-python-dictionaries-a-confluence-of-a-dozen-great-ideas.html) at the Pycon 2017.

[Raymond Hettinger](https://twitter.com/raymondh) is a Python core developer and its contribution to the Python development has been invaluable so far.
