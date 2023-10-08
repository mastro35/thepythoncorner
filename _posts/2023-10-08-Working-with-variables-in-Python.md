---
title: "Working with variables in Python"
date: 2023-10-08T00:05:35+01:00 
author: "davide_mastromatteo"
excerpt: "Have you ever wondered how variables works in Python? Well, this article will help you find it out."
header:
    teaser: https://imgs.xkcd.com/comics/proxy_variable.png
categories:
    - Dev
tags:
    - python
    - variables
    - c
---

![Proxy Variable](https://imgs.xkcd.com/comics/proxy_variable.png)

One of the mistakes I often see (mainly) by beginners is to underestimate some basic aspects of Python. The most underestimated one is that about variables, a topic that is often treated very lightly, especially by those who come from other languages and therefore assume that basically there are no big differences because, after all, a variable is just a variable, right?

Well, maybe not...

## Object types in Python

Let's make a premise right away: in Python, anything is an object, and when I say "anything" I mean literally **anything**. 
Seriously. 
Even a simple integer is an object in Python. 

Objects, in Python, fall into two categories: 

- `mutable`
- `immutable`

`mutable` objects are those that as the name suggests can change or mutate.
`immutable` objects, on the other hand, have the fundamental characteristic that they can never change; once created they remain as such until they are destroyed.

Among `immutable` objects we find, for example, objects of type:

- `String`
- `Int`
- `Float`
- `Tuple`

while `List`, `Dict`, or `Set` are `mutable` objects.

Now you may be wondering why this premise was made, right? 

## How variables work in Python (and in C)

Consider the following program written in C:

```c
#include <stdio.h>
int main(void) {
    int a = 1000;
    printf("The address of 'a' is %p and the value is %d \n", &a, a);
    a++;
    printf("The address of 'a' is %p and the value is %d \n", &a, a);
}
```

Executing this C program your output will be similar to this one: 

```console
$ ./a.out 
The address of 'a' is 0x7ff7bd77b61c and the value is 1000 
The address of 'a' is 0x7ff7bd77b61c and the value is 1001 
```

What happened when we ran the program? Very simple, the variable `a` was defined, with an initial value of `1000`. The variable occupied an area of memory with the size of an `int` identified by the address `0x7ff7bd77b61c`. Then we took this variable and added one unit to its value. Now the variable `a` is worth `1001` and occupies the same address as before. 

Let's do the same thing in Python:


```python
a = 1000
print(f"The address of `a` is {hex(id(a))} and the value is {a}")
a = a + 1
print(f"The address of `a` is {hex(id(a))} and the value is {a}")
```
```
    The address of `a` is 0x1034cedb0 and the value is 1000
    The address of `a` is 0x1034ce7f0 and the value is 1001
```

As you can see Python behaved differently. 
The variable was first put at a certain memory address, then it was incremented by one unit and now... we find it at a different address!

But how come?

Simple, we said it before, remember? Integers in Python are immutable objects, so it was not possible to *modify* the object, it was necessary to create a new one (in a new memory area) and make the `a` variable no longer point to the old memory area but to the new one. This is because, in Python:

> A variable is nothing more than a mnemonic label that refers to an object

In the previous example, initially, the label `a` identified the object with the value `1000`, now it identifies the object with the value `1001` present at a completely different address.

Okay, let's complicate things a bit and bring a second variable into play.
This is the program in the C language:

```c
#include <stdio.h>
int main(void) {
    int a = 1000;
    printf("The address of 'a' is %p and the value is %d \n", &a, a);
    int b = a;
    printf("The address of 'b' is %p and the value is %d \n", &b, b);
}
```

Running this program we get the following output:

```Console
~ $ ./a.out 
The address of 'a' is 0x7ff7bafcc62c and the value is 1000 
The address of 'b' is 0x7ff7bafcc628 and the value is 1000 
```

Basically, we created a second variable `b`, and gave it the same value as the variable `a`. In fact in the C program what has happened is that we now have two separate variables, each in a different area of memory and both containing the value `1000`. 

Simple, but what will Python do in this case? 


```python
a = 1000
print(f"The address of `a` is {hex(id(a))} and the value is {a}")
b = a 
print(f"The address of `b` is {hex(id(b))} and the value is {b}")
```
```
    The address of `a` is 0x1034ce850 and the value is 1000
    The address of `b` is 0x1034ce850 and the value is 1000
```

It seems incredible but again, the result is different from what a C programmer would have expected.
This time a and b ... point to the same area of memory! 
But if you think about it it is awfully logical, as we said before variables in Python are nothing more than labels that identify a value, in this case, the object with the value `1000` that was identified by the name `a`, is now identified by both the name `a` and the name `b`. What does this example teach us? Simple, it teaches us that. 

> **Simply assigning a value to a variable does NOT ever create a new object**.

Mind you, this "double pointing" only works because we are pointing to the same object, not an object from the same value. 
In the example above, for example, if we had done something as simple as adding `0` to the value of `a`, we would end up with a new object because it was the result of an arithmetic operation and thus we would have found it in a different memory area.


```python
a = 1000
print(f"The address of `a` is {hex(id(a))} and the value is {a}")
b = a + 0
print(f"The address of `b` is {hex(id(b))} and the value is {b}")
```
```
    The address of `a` is 0x1034cc3f0 and the value is 1000
    The address of `b` is 0x1034ce730 and the value is 1000
```

Note, as we discussed in a [previous post](https://thepythoncorner.com/posts/2022-06-18-the-sunday-tip-1-python-cached-integer/), integers between -5 and 256 are cached by the interpreter so they always keep the same address. This is why in these examples I am using integers that are not in this range, but this is just because of a matter of performance, so don't be fooled by this fact.

## Consequences when working with mutable objects

At this point, it should be clear that Python and C treat variables very differently, but at first glance, one might think that all in all these are just formal and internal language differences and consequently that from the programmer's point of view this is completely transparent. After all, in the previous examples the Python and C programs returned the same results, right?

Actually, the examples were returning the same results only because we were working with immutable objects. 
Working with mutable objects can have unexpected consequences.

To understand what I am talking about let's start with this example, that works with Integers and therefore with immutable objects.
If you have understood what has been said so far it should be easy for you to understand how it works:

```python
a = 1000
b = a

print(f"a is located at ({hex(id(a))}) and its value is {a}")
print(f"b is located at ({hex(id(b))}) and its value is {b}")


b = b + 1 

print(f"a is located at ({hex(id(a))}) and its value is {a}")
print(f"b is located at ({hex(id(b))}) and its value is {b}")

```

```console
    a is located at (0x1034cc490) and its value is 1000
    b is located at (0x1034cc490) and its value is 1000
    a is located at (0x1034cc490) and its value is 1000
    b is located at (0x1034ce770) and its value is 1001
```

In this example `a` and `b` initially point to the same object. Then we changed the value of `b` by adding `1` to its value and as a result, a new object worth `1001` was created to which `b` was pointed.

Now we do the same thing but using a mutable object such as a list.


```python
a = ['I', 'am', 'a', 'list']
b = a

print(f"a is located at ({hex(id(a))}) and its value is {a}")
print(f"b is located at ({hex(id(b))}) and its value is {b}")


b.append('hooray!!!')

print(f"a is located at ({hex(id(a))}) and its value is {a}")
print(f"b is located at ({hex(id(b))}) and its value is {b}")

```

```console
    a is located at (0x1034fab00) and its value is ['I', 'am', 'a', 'list']
    b is located at (0x1034fab00) and its value is ['I', 'am', 'a', 'list']
    a is located at (0x1034fab00) and its value is ['I', 'am', 'a', 'list', 'hooray!!!']
    b is located at (0x1034fab00) and its value is ['I', 'am', 'a', 'list', 'hooray!!!']
```

Did you see what happened? We changed the object pointed by `b` and as a consequence, the value of `a` also changed. 
But this no longer surprises us, right? Because after what we said before, we now know that `a` and `b` pointed to the same object, and since it is a mutable object, although the value of the object changed, the object remained the same.

Now do you see why it is important to understand what happens "under the hood" of Python when working with variables? 
Because otherwise, you would not understand this behavior, which is terribly logical instead.

## Passing arguments to a function

Now that we are finally all clear on how variables work in Python we can take this opportunity to answer once and for all a question we often hear from beginners: in Python are variables to functions passed by value or by reference?

This question is quite usual because in many programming languages, you can choose whether to pass a variable by value or by reference, with the consequence that if you pass it by value you are in fact passing a copy of it, so modifying it within the function will not affect the original copy, whereas if you pass it by reference, you are passing its memory address and thus any modification within the function will affect also the original copy.

In Python, arguments are actually passed by *assignment*. Basically, you assign the passed objects to the parameter names of the called function, just as if they were simple variable assignments, and consequently, everything we have said so far applies. 

Consider the following example:

```python
def my_function (anInt:int, aList:list):
    anInt = anInt + 1
    aList = aList.append("super simple!")

myInt = 3500
myList = ["Python", "is", "..."]

my_function(myInt, myList)

print(myInt)
print(myList)
```
```console
    3500
    ['Python', 'is', '...', 'super simple!']
```

In this example, the call to the `my_function` function does nothing more than pass the object pointed to by `myInt` to the `anInt` argument and the object pointed by `myList` to the `aList` argument. It's just that, there's no magic here.

Consequently, the change to the object pointed to by `anInt` (since it is an immutable object) is lost as soon as we exit the function, while the one made on `aList`, since it directly modifies the value of the object, also affects the source variable.

We just have to keep in mind that parameters are passed by assignment, and for that reason, we must always pay attention to their type (whether they are mutable or immutable objects), and if we are dealing with mutable objects we must always consider what kind of operations we are doing on them and whether they are operations that "mutate" the original object or not. 

Consider now the following example:


```python
def my_function (anInt:int, aList:list):
    anInt = anInt + 1
    aList = aList + ["super simple!"]

myInt = 3500
myList = ["Python", "is", "..."]

my_function(myInt, myList)

print(myInt)
print(myList)
```
```
    3500
    ['Python', 'is', '...']
```

If you just look at the code at first glance it may look very similar to the previous one, correct? Yet simply using the `+` operator changes everything because by using this operator Python creates an entirely new object, that is pointed to by `aList` and at this point, the change is not reflected on the source object. 

A beginner who had experienced this himself before reading this article might have been scared off by this, right? But now everything should be much clearer and in fact I expect it to be incredibly logical to you.

To close, one last example:


```python
def my_function (anInt:int, aList:list):
    anInt = anInt + 1
    aList += ["super simple!"]

myInt = 3500
myList = ["Python", "is", "..."]

my_function(myInt, myList)

print(myInt)
print(myList)
```
```
    3500
    ['Python', 'is', '...', 'super simple!']
```

Okay, if you are getting nosebleeds at this point, I understand.... :)
What is going on here? Why on earth does `aList = aList + ["super simple!"]` behave differently from `aList += ["super simple!"]`?

Actually, this is completely logical as well. 
When you use the `+` operator on a list you are in fact calling the `__add__()` method, which performs concatenation and returns a new list to the caller. On the other hand, when you use the `+=` operator, you are calling the `__iadd__()` method, which internally does an append operation on the list, thus modifying it but not creating a new list.

## In conclusion

There is a big difference between knowing how to write a few lines of code and really knowing how a programming language works. In this case, knowing how variables really work in Python, besides saving you from several headaches and hours of debugging will help you understand and appreciate our favorite programming language much more. 

Anyway, if I have managed to even save you a headache... consider buying me a coffee by clicking on the button below! :)

Byez
D.
