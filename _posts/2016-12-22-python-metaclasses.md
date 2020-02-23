---
title: Python Metaclasses
date: 2016-12-22T12:31:01+01:00
author: Davide Mastromatteo
excerpt: |
  "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't". That's what Tim Peters once said. But aren't you curious to know something about them? :)
header:
  teaser: https://imgs.xkcd.com/comics/code_quality.png
categories:
  - Dev
tags:
  - Abstract Base Classes
  - Featured
  - Metaclasses
  - Programming
  - Python
redirect_from:
  /2016/12/python-metaclasses
---
![teaser](https://imgs.xkcd.com/comics/code_quality.png)

Working with Python means working with objects because, in Python, **everything** is an object. So, for example:

```python
>>> type(1)
<class 'int'>
>>> type('x')
<class 'str'>
```

As you can see, even basic types like integer and strings are objects, in particular, they are respectively instances of *int* and *str* classes. So, since everything is an object and given that an *object* is an instance of a *class*... what is a class?

Let's check it:

```python
>>> type(int)
<class 'type'>
>>> type(str)
<class 'type'>
```

It turns out that classes are an object too, specifically they are instances of the "type" class, or better, they are instances of the "type" *metaclass*.

A metaclass is *the class of a class* and the use of metaclasses could be convenient for some specific tasks like logging, profiling and more.

So, let's start demonstrating that a class is just an instance of a metaclass. We've said that *type* is the base metaclass and instantiating this metaclass we can create some class so... let's try it:

```python
>>> my_class = type("Foo", (), {"bar": 1})
>>> print(my_class)
<class '__main__.Foo'>
```

Here you can see that we have created a class named "Foo" just instantiating the metaclass *type*. The parameters we have passed are:

- The class name (Foo)
- A tuple with the class superclasses (in this example we are creating a class without specifying any superclass)
- A dictionary of attributes for the class (in this example we are creating the attribute "bar" with an int value of 1)

If everything is clear so far, we can try to create and use a custom metaclass. To define a custom metaclass it's enough to subclass the type class.

Look at this example:

```python
class Logging_Meta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        print(str.format("Allocating memory space for class {0} ", cls))
        return super().__new__(cls, name, bases, attrs, **kwargs)

    def __init__(self, name, bases, attrs, **kwargs):
        print(str.format("Initializing object {0}", self))
        return super().__init__(name, bases, attrs)

class foo(metaclass=Logging_Meta):
    pass

foo_instance = foo()
print(foo_instance)
print(type(foo))
```

on my PC, this code returns:

```console
Allocating memory space for class <class '__main__.Logging_Meta'>
Initializing object <class '__main__.foo'>
<__main__.foo object at 0x000000B54ACC0B00>
<class '__main__.Logging_Meta'>
```

In this example we have defined a metaclass called *Logging_Meta* and using the magic methods *__new__* and *__init__* we have redefined the behavior of the class when the object is created and initialized. Then, we've declared a foo class specifying which is the metaclass to use for this class and as you can see, our class behavior is changed according to the *Logging_Meta* metaclass implementation.

## A concrete use-case: Abstract Base classes (ABC's)

A concrete use of metaclasses is the *abc* module. The *abc* module is a module of the standard library that provides the infrastructure for defining an abstract base class. Using abc you can check that a derived class that inherits from an abstract base class implements all the abstract methods of the superclass **when the class is instantiated**.

For example:

```python
from abc import ABCMeta, abstractmethod

class my_base_class(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

class my_derived_class(my_base_class):
    pass

a_class = my_derived_class()
```

If you try this example, you will see that the last line (the one that tries to instantiate the derived class) will raise\n
the following exception:

```console
TypeError: Can't instantiate abstract class my_derived_class with abstract methods foo
```

That's because *my_derived_class* does not implement the method foo as requested from the abstract base class.

It's worth to be said that if you subclass a base class that uses a specific metaclass, your new object will use the metaclass as well. In fact, since Python 3.4 the module abc now provide also the ABC class that is just a generic class that uses the ABCMeta metaclasses. This means that the last example can be rewritten as follows:

```python
from abc import ABC

class my_base_class(ABC):
    @abstractmethod
    def foo(self):
        pass

class my_derived_class(my_base_class):
    pass

a_class = my_derived_class()
```

This was just a brief introduction to metaclasses in Python. It's more or less what *I* think should be known about this topic because it could lead to a better understanding of some internals of Python.

But let's be clear: this is not something that every single Python user needs to know in order to start working in Python. As the "Python Guru" Tim Peters once said:

> "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why)."  — Tim Peters*

Enjoy!
D.
