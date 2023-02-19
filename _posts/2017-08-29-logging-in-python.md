---
title: Logging in Python
date: 2017-08-29T13:02:52+02:00
author: "davide_mastromatteo"
excerpt: "Do you always write log routines to make your program be verbose in the production environment? No? Well, you'd better have a look at this article."
header:
  teaser: https://imgs.xkcd.com/comics/git_commit.png
categories:
  - Dev
tags:
  - Featured
  - Logging
  - Python
redirect_from:
  - /2017/08/logging-in-python
  - /2017/08/logging-in-python/
  - /dev/logging-in-python/
---
![teaser](https://imgs.xkcd.com/comics/git_commit.png)

One of the most underestimated topics that I've seen in my working experience is logs management. A lot of people don't care at all about logging the execution of their programs and I've seen a lot of code released in the production environment that doesn't log anything. To log seems to be a waste of time to them, especially if the code they're writing is apparently simple. So, why bother logging the execution of a program if the program can run great with no logs?

Actually, logging the execution of your own program avoids you lots of headaches when something goes wrong in production and make your coding experience easier. Besides, logging a lot of debug information can save you time in writing comments, because your code is just well documented by the use of the logging, so to log is always a good idea in production as it is during the development, and that is true for any language you're using to code, not just in Python.

But Python is not "any language", Python is a great language that comes with "batteries included", isn't it?

In fact, although in other languages you need to write your own logging facility or to download some third-party libraries that solve this problem for you, in Python it just means to use the built-in logging module.

So, what are we waiting for? Let's start logging in Python!

The first thing that we have to bear in mind is that a log can contain a different kind of messages and each message has its own level of importance. These levels, in Python, are defined in order of verbosity (from the most verbose to the less verbose) as follows:

- DEBUG: Detailed information, typically of interest only when diagnosing problems.- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low'). The software is still working as expected.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

So, each time we want to write something in our log we have to decide what kind of message we are writing to the log, and hence what level it should have.

The second thing that we have to know is how to configure a logger in Python. It's really easy actually, we just need three components:

- a logger: the object that our code will use to log
- at least one handler: the object that will handle the writing of our log to the target device
- a formatter: an object that defines the format of our log for the handler

Ok, too much talk, let's start coding.

Let's start by importing the logging module:

```python
import logging
```

Then, let's create the the logger:

```python
logger=logging.getLogger(__name__)
```

as you can see, to create a logger we just have to call the "getLogger" method of our logging module passing to it a name for the logger. Usually, it's a good idea to use the **name** special variable to specify the name of the logger. Doing this you will have different loggers for different modules by design, and you will be able to configure differently every single logger.

Now we have to specify the default log level of our logger. This configuration ensures you that just the log messages with this level or with a less verbose level will be recorded. This enables you to have a super detailed log with all the debug information when you are developing or testing your application and a less verbose log when you deploy your program to the production environment.

```python
# define the default level of the logger. 
# We could specify a greater (LESS VERBOSE) level on the single handler 
logger.setLevel(logging.DEBUG)
```

Now we have to create our second object: the formatter. As we said before, the formatter is the object that specifies the format we want for our log. In this example, I'm creating a formatter that will output every single message specifying its timestamp and its log level. There are plenty of variables you can use to configure the format of your log, to have a complete list check the [official documentation](https://docs.python.org/3/library/logging.html#logrecord-attributes).

```python
# creating a formatter. 
# to see all the attributes you can use
formatter=logging.Formatter('%(asctime)s | %(levelname)s -> %(message)s')
```

Now we need to create the handler (or the handlers) that will take care of writing our logs to the target device. Usually I create a file handler to log on a file on the filesystem all the information with an INFO level or greater (it's a must for the production environment) and a stream handler to log every single information also to the console (it's quite convenient while I'm coding and prevent me to misuse the "print" function). Note that we can specify a different level for each handler unless it is greater or equal to the main level specified for the logger. Even the format can be different (we could need different information for the console and for the log file for example).

```python
# creating a handler to log on the filesystem
file_handler=logging.FileHandler('mylogfile.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# creating a handler to log on the console
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
```

Ok, we have almost finished now, we just need to put everything together...

```python
# adding handlers to our logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
```

and that's it! We have configured our logger. It wasn't a pain, was it? Now, to log a message we will just need to call the "info", "warning", "error", "debug", or "critical" method passing the message we want to log as a parameter. For example:

```python
logger.info('this is a log message...')
```

and we'll get:

```console
2017-08-29 12:41:42,154 | INFO -> this is a log message...
```

Now, if we were creating a program to divide two given numbers and log the result, we could have done something like this:

```python
a=50
b=10

try:
    c=a/b
    logger.info(f"Operation {a}/{b} gave the result {c}")
except:
    logger.error(f"Error occured during the division of {a} and {b}")
```

And the output would be:

```console
2017-08-29 12:41:42,204 | INFO -> Operation 50/10 gave the result 5.0
```

It's worth to be said that to log the exceptions there's also an "exception" method of the logger that write a message with the "ERROR" level but add to it also some more information from the exception, like the stacktrace and the exception message. So for example, in this example it was far better to write something like this:

```python
a=50
b=0

try:
    c=a/b
    logger.info(f"Operation {a}/{b} gave the result {c}")
except:
    logger.error(f"Error occured during the division of {a} and {b}")
```

And the output would be:

```console
2017-08-29 12:41:42,242 | ERROR -> Error occured during the division of 50 and 0
Traceback (most recent call last):
  File "<ipython-input-10-9b4751150eb5>", line 5, in <module>
    c=a/b
ZeroDivisionError: division by zero
```

As always, for more information and for advanced topics I encourage you to check the [official documentation](https://docs.python.org/3/library/logging.html#module-logging) and the [original PEP](https://www.python.org/dev/peps/pep-0282/).

That's all folks, happy coding and...
happy logging! :)

D.
