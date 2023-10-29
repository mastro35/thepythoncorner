---
title: Working with Exception in Python
date: 2017-01-10T19:02:01+01:00
author: Davide Mastromatteo
excerpt: "To know how exception works in Python is really important. Exceptions are not just used to control the program's errors but also to manage the program's flow and in this post, we will discuss this specific topic"
header:
  teaser: https://imgs.xkcd.com/comics/compiler_complaint.png
categories:
  - Dev
tags:
  - Error Handling
  - Exception
  - Featured
  - Programming
  - Python
redirect_from:
  - /2017/01/working-with-exception-in-python
  - /2017/01/working-with-exception-in-python/
  - /dev/working-with-exception-in-python/
---
![teaser](https://imgs.xkcd.com/comics/compiler_complaint.png)

According to the [official documentation]("https://docs.python.org/3/tutorial/errors.html), an exception is "an error detected during execution not unconditionally fatal". Let's start the interpreter and write:

```python
>>> 5/0
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    5/0
ZeroDivisionError: division by zero
```

As you can see we asked the interpreter to divide the number 5 by 0. Even if our request was syntactically correct when the interpreter tried to compute it, it "raised" the *ZeroDivisionError* exception to signal us that we asked something impossible. There are a lot of built-in exceptions in the base library to handle a different kind of errors (system errors, value errors, I/O errors, Arithmetic errors etc...) and to know how to handle this kind of errors is very important for every Python developer.

## Handling exception

Handle an exception means to define what to do when a specific exception happens so that the execution can proceed smoothly.

The basic way to handle an exception is by using the *try* statement. Basically, we need to specify what we want to do, which kind of exceptions we do expect and what to do when one of these exceptions is raised.

To make an example, let's say we want to open a file to read it and show its content. To accomplish this task we can write this script:

```python
f = open("myfile.txt")

for line in f:
    print(line)
```

The problem is: what happens if the file *myfile.txt* does not exist? Let's try...

```console
Traceback (most recent call last):
  File "exceptions.py", line 1, in <module>
    f = open("myfile.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
```

Well, we get a *FileNotFoundException* and the execution stops. So, to handle this exception we could just modify the code as follows:

```python
try:
    f = open("myfile.txt")
    
    for line in f:
        print(line)
    except FileNotFoundError:
        print("The file does not exist")
```

In this way, the interpreter tries to do what's inside the *try* block and, if a *FileNotFoundError* exception is raised, instead of writing the exception's detail on screen and exit, it just continues executing what's inside the *except* block. If the file existed, the exception would not be raised and the except block would be skipped.

Now, executing the script again, the result would be:

```console
The file does not exist
```

It's worth to be noted that we can use more except clauses for a single try block. For example, the code could be modified as follows:

```python
try:
    f = open("myfile.txt")
    for line in f:
        print(line)
except FileNotFoundError:
    print("The file does not exist")
except PermissionError:
    print("You don't have the permission to open the file")
except Exception:
    print("Unexpected error occured")
  ```

In the latest example, we are trapping the exception to handle the case when the file does not exist, the exception to handle the case when the file exists but the user does not have the permission to read from it and any other error that could happen at run time, catching the general *Exception *exception. This is made possible thanks to the fact that in Python, everything is an object, even the exceptions. This means that almost all the exceptions that can be fired at runtime are actually derived from the *Exception* exception.

Here's the complete hierarchy as it appears in the [official docs](https://docs.python.org/3/library/exceptions.html):

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

Finally, you can have the need to execute some code after the try block is executed, whether or not the code in the try block has raised exceptions. In this case, you can add a *finally* clause. For example:

```python
try:
    f = open("myfile.txt")
    for line in f:
        print(line)
except FileNotFoundError:
    print("The file does not exist")
except PermissionError:
    print("You don't have the permission to open the file")
except Exception:
    print("Unexpected error occured")
finally:
    print("The execution will now be terminated")
```    

In this last example, whatever happens, the message "The execution will now be terminated" will be shown before leaving the try/except block.

## Raising exception

Now that we know what an exception is and how to handle exceptions, let's see how is it possible to raise exceptions by ourselves.
Look at this code:

```python
def get_numeric_value_from_keyboard():
    '''Get a value from keyboard, if the value is not a valid number, raise a "ValueError" exception'''
    input_value = input("Please, enter an integer: ")
    if not input_value.isdigit():
        raise ValueError("The value inserted is not a number")

	return input_value

while True:
    try:
        numeric_value = get_numeric_value_from_keyboard()
        print("You have inserted the value " + str(numeric_value))
        break
    except ValueError as ex:
        print(ex)
```

In this example, we have created a function that gets input from the user keyboard. If the input is numeric, it just returns the input to the caller, but if it's not, it raises a "ValueError" exception. Note that in this example, we're not just raising a *ValueError* exception but we are also specifying a custom message for the exception. In the except clause, we grab the exception, assign it to the *ex* variable and then we use the *ex* variable to print the message for the user.

Another possibility you have is to re-raise an exception once it gets caught in an except block. For example, try to modify the code as follows:

```python
def get_numeric_value_from_keyboard():
    '''Get a value from keyboard, if the value is not a valid number, raise a "ValueError" exception'''
    input_value = input("Please, enter an integer: ")
    if not input_value.isdigit():
        raise ValueError("The value inserted is not a number")

    return input_value

while True:
    try:
        numeric_value = get_numeric_value_from_keyboard()
        print("You have inserted the value " + str(numeric_value))
        break
    except ValueError as ex:
        print("Something strange happened...")
        raise
```

Now, if you run this code and insert a non-numeric value, the execution will be interrupted and you will get this message:

```console
Please, enter an integer: asd
Something strange happened...
Traceback (most recent call last):
  File "exceptions.py", line 12, in <module>
    numeric_value = get_numeric_value_from_keyboard()
  File "exceptions.py", line 5, in get_numeric_value_from_keyboard
    raise ValueError("The value inserted is not a number")
ValueError: The value inserted is not a number
```

As you can see, in the except block we've caught the *ValueError* exception, we've done something (we've printed the "Something strange happened..." message) and then we've re-raised the same exception we previously caught. Obviously, since there were no other code blocks to catch our exception, the program has exited and the exception has been shown to the console.

## Define custom exception

Knowing how to raise an exception is important especially if we want to build our custom exception. We've already said that there's a hierarchy of exceptions, so to create our custom exception we just need to create a new class inheriting from the *Exception* class.

So, let's say that we are coding the software for an ATM, we could need a special "WithdrawLimitError" exception to be raised when the user asks for a too high sum of money. In this case, we can create our custom exception like this:

```python
class WithdrawLimitError(Exception):
    pass
```

Now, we can use it in our code just like any other exception.

## The bottom line

There are several programming languages where the developer is asked to use exception just to handle "errors" because the handling of an exception can lead to performance issues. Well, the Python approach is completely different. Python internals relies on exceptions (for example, in a simple "for" loop the StopIteration exception is used to signal that there are no further items to iterate) and is encouraged the use of an exception to indicate failures, even when they are expected on regular basis.

So for example, if you have to open a file don't check whether it exists or not, just open it and handle the exception if something goes wrong. It makes the code more readable, *Pythonic*, and easier to be maintained.

Enjoy!
D.
