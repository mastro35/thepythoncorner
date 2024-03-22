---
title: "Object Serialization in Python With the Pickle Module"
date: 2016-12-06T00:00:49+01:00
author: Davide Mastromatteo
excerpt: "In this post, we will learn to serialize objects for storing the state of an object and cloning objects. Cool stuff, right?"
header:
  teaser: https://imgs.xkcd.com/comics/expiration_date_high_score.png
categories:
  - Dev
tags:
  - serialization
  - pickle
  - python
redirect_from:
  - /2016/12/object-serialization-in-python
  - /2016/12/object-serialization-in-python/
  - /dev/object-serialization-python-pickle/
  - /posts/2016-12-6-object-serialization-python-pickle/
---
![teaser](https://imgs.xkcd.com/comics/expiration_date_high_score.png)

**DISCLAMER**:  There's a newer (and probably better) [article](https://realpython.com/python-pickle-module/) about this topic that I wrote for [Real Python](https://realpython.com) website.

It's longer and more detailed and it also have a section about the security concern when using the pickle module, so... I want to be honest and I suggest you to read [that article](https://realpython.com/python-pickle-module/) ... but if you like it, don't forget to come back here and [buy me a coffe](https://www.buymeacoffee.com/mastro35)! :) 

---

Today we're going to explore a wonderful feature that the Python library offers to you out of the box: the serialization. To serialize an object means to transform it in a format that can be stored, so as to be able to deserialize it later, recreating the original object from the serialized format. To do all these operations we will use the pickle module.

## Pickling

Pickling is the name of the serialization process in Python. By pickling, we can convert an object hierarchy to a binary format (usually not human readable) that can be stored. To pickle an object we just need to import the pickle module and call the dumps() function passing the object to be pickled as a parameter.

For example:

```Python
import pickle
​
class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color
​
class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)
​
mary = Sheep("white")
​
print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))
my_pickled_mary = pickle.dumps(mary)
​
print ("Would you like to see her pickled? Here she is!")
print (my_pickled_mary)
```

So, in the example above, we have created an instance of a sheep class and then we've pickled it, transforming our sheep instance into a simple array of bytes.
It's been easy, hasn't it?

Now we can easily store the bytes array on a binary file or in a database field and restore it from our storage support in a later time to transform back this bunch of bytes in an object hierarchy.

Note that if you want to create a file with a pickled object, you can use the dump() method (instead of the dumps() one) passing also an opened binary file and the pickling result will be stored in the file automatically.

To do so, the previous example could be changed like this:

```Python
import pickle
​
class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color
​
class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)
​
mary = Sheep("white")
​
print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))
my_pickled_mary = pickle.dumps(mary)
​
binary_file = open('my_pickled_mary.bin', mode='wb')
my_pickled_mary = pickle.dump(mary, binary_file)
binary_file.close()
```

## Unpickling

The process that takes a binary array and converts it to an object hierarchy is called unpickling.

The unpickling process is done by using the load() function of the pickle module and returns a complete object hierarchy from a simple bytes array. Let's try to use the load function on the example above:

```Python
import pickle
​
class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color
​
class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)
​
# Step 1: Let's create the sheep Mary
mary = Sheep("white")
​
# Step 2: Let's pickle Mary
my_pickled_mary = pickle.dumps(mary)
​
# Step 3: Now, let's unpickle our sheep Mary creating another instance, another sheep... Dolly!
dolly = pickle.loads(my_pickled_mary)
​
# Dolly and Mary are two different objects, in fact if we specify another color for dolly
# there are no conseguencies for Mary
dolly.color = "black"
​
print (str.format("Dolly is {0} ", dolly.color))
print (str.format("Mary is {0} ", mary.color))
```

In this example you can see that after having pickled the first sheep object (Mary) we have unpickled it to another variable (Dolly) and so we have — in a sense — cloned Mary to create Dolly (Yes, we're cloning sheep... lol!).

It goes without saying that changing an attribute value on one of these objects the other one remain untouched because we haven't just copied the reference to the original object, we have actually cloned the original object and its state to create a perfect copy in a completely different instance.

>Note: in this example we have cloned an object using the trick of pickling it and unpickling the resulting binary stream in another variable.
>This is ok and there are several languages where this approach could even be advised, but if you need to clone an object in Python it's probably better to use the copy module of the standard lib. Since it's designed to clone objects, it works far better.

## Some notes about pickling

All I've said so far is just to whet your appetite because there's a lot more we could say about pickling. One important thing to be known is that there are several types (or protocols) of pickling because this technic is evolving as the language evolves.

So, there are currently 5 protocols of pickling:

According to the [official documentation](https://docs.python.org/3.4/library/pickle.html#data-stream-format):

>Protocol version 0 is the original "human-readable" protocol and is backwards compatible with earlier versions of Python.
>Protocol version 1 is an old binary format which is also compatible with earlier versions of Python.
>Protocol version 2 was introduced in Python 2.3. It provides much more efficient pickling of new-style classes. Refer to PEP 307 for information about improvements brought by protocol 2.
>Protocol version 3 was added in Python 3.0. It has explicit support for bytes objects and cannot be unpickled by Python 2.x. This is the default protocol, and the recommended protocol when compatibility with other Python 3 versions is required.
>Protocol version 4 was added in Python 3.4. It adds support for very large objects, pickling more kinds of objects, and some data format optimizations. Refer to PEP 3154 for information about improvements brought by protocol 4.

Another thing that is important to keep in mind is that not every object is picklable. Some objects (like DB connections, handles to opened files etc...) can't be pickled and trying to pickle an unpicklable object (or to unpickle an object that is not a valid pickle), a pickle.PickleError exception or one of its subclasses (PicklingError and UnpicklingError) is raised.

For example:

```Python
import pickle
​
my_custom_pickle = bytes("this is unpicklable", encoding="UTF-8")
​
# this next statement will raise a _pickle.UnpicklingError
my_new_object = pickle.loads(my_custom_pickle)
```

The problem when you have unpicklable object in the hierarchy of the object you want to pickle is that this prevents you to serialize (and store) the entire object. Fortunately, Python offers you two convenient methods to specify what you want to pickle and how to re-initialize (during the unpickling process) the objects that you haven't pickled before. These methods are __setstate__() and __getstate__()

For example:

```Python
import pickle
​
class my_zen_class:
   number_of_meditations = 0
​
    def __init__(self, name):
        self.number_of_meditations = 0
        self.name = name
​
    def meditate(self):
        self.number_of_meditations = self.number_of_meditations + 1
​
    def __getstate__(self):
        # this method is called when you are 
        # going to pickle the class, to know what to pickle
​
        state = self.__dict__.copy()
​
        # You will never get the Buddha state if you count 
        # meditations, so 
        # don't pickle this counter, the next time you will just 
        # start meditating from scratch :)
        del state['number_of_meditations']
​
        return state
​
    def __setstate__(self, state):
        # this method is called when you are going to 
        # unpickle the class,
        # if you need some initialization after the 
        # unpickling you can do it here.
​
        self.__dict__.update(state)
​
# I start meditating
my_zen_object = my_zen_class("Dave")
for i in range(100):
    my_zen_object.meditate()
​
# Now I pickle my meditation experience
print(str.format("I'm {0}, and I've meditated {1} times'", my_zen_object.name, my_zen_object.number_of_meditations))
my_pickled_zen_object = pickle.dumps(my_zen_object)
my_zen_object = None
​
# Now I get my meditation experience back
my_new_zen_object = pickle.loads(my_pickled_zen_object)
​
# As expected, the number_of_meditations property 
# has not been restored because it hasn't been pickled
print(str.format("I'm {0}, and I don't have a beginner mind yet because I've meditated only {1} times'", my_new_zen_object.name, my_new_zen_object.number_of_meditations))
```

## The security concern

Now you know about what does it means to serialize and deserialize objects in Python but... have you ever tought at what could it means from a security perspective? If not, go ahead and have a loot to [this article I wrote for "Real Python"](https://realpython.com/python-pickle-module/). It has a lot of details and a specific section about the security topic.  

Enjoy!
D.
