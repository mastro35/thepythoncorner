---
title: Using Environment Variables in Python
date: 2025-01-12T18:19:00+01:00
author: Davide Mastromatteo
excerpt: "A great place were to store sensitive information that have to been used by your application is "environment variables". If you are interested in learning how to use them in Python, just have a look at this article."
header:
  teaser: https://imgs.xkcd.com/comics/xkcde.png
categories:
  - Dev
tags:
  - Environment Variables
  - dotenv
  - Python
---
![teaser](https://imgs.xkcd.com/comics/xkcde.png)


Environment variables are a powerful way to configure applications and manage sensitive information such as API keys, database credentials, and other configuration settings. 
In this article, we'll explore what environment variables are, why they are useful, and how to use them effectively in Python.

## What Are Environment Variables?

Environment variables are key-value pairs that are set in the operating system and can be accessed by applications running on that system. They provide a way to configure applications without hardcoding values into the source code. This makes it easier to manage different configurations for development, testing, and production environments.

For example, you might have an environment variable called `DB_CONNECTING_STRING` that contains the connecting string of your database. Instead of hardcoding this URL into your application, you can access it through the environment variable, making it easy to change the connection without modifying the code.

## Why Use Environment Variables?

Now you may be wondering why you should start to use environment variables, right?
Well, there are at least three good reasons for that:

1. **Security**: Storing sensitive information such as API keys and passwords in environment variables keeps them out of your source code, reducing the risk of accidental exposure.
2. **Configuration Management**: Environment variables allow you to manage different configurations for different environments (e.g., development, testing, production) without changing the code. 
3. **Portability**: Environment variables make it easier to deploy your application to different environments, as you can configure the necessary settings through the environment rather than modifying the code.

## Using Environment Variables 

Before talking about Python, let's see how to use environment variables on different operative systems:

### Windows

If you are using Windows, to set an environment variable you can use the `set` command in the Command Prompt:

```cmd
C:\set MY_VARIABLE=value
```

To get back the value from an environment variable previously set, you can simply put it between a pair of `%`:

```cmd
C:\echo %MY_VARIABLE% 
```

### macOS and Linux

To set an environment variable in macOS or Linux, using bash or zsh, you can use the `export` command in the terminal:

```bash
$ export MY_VARIABLE=value
```

and to get back the value, you can just prepend a `$` before the name of the variable:

```bash
$ echo $MY_VARIABLE
```

## Using Environment Variables in Python

In Python, to use os features you need to use the `os` module. 
The `os` module provides a dictionary-like object called `environ` that contains all the environment variables.

Here's an example of how to access an environment variable in Python:

```python
import os

# get the value of an environment variable
database_connection = os.environ['DATABASE_CONNECTION']

# print the value of the environment variable
print(f'Database connection string: {database_connection}')
```

You can also set environment variables in Python using the `os` module (altough this is somehow less usual). 
Here's an example:

```python
import os

# Set an environment variable
os.environ['DATABASE_CONNECTION'] = '[put here you db connection string]'
```

Another small tip, when you want to retrieve a value and you need a fallback value if the variable is not set, you can use the method `get` providing a second value as the default value of the variable you are trying to retrieve.

For example:

```python
import os

# get the value of an environment variable
my_number= os.environ.get('MY_NUMBER',0)

# print the value of the environment variable that will be MY_NUMBER if the variable has been set or 0 otherwise...
print(my_number)
```

## Using Environment Variables with `dotenv`

Managing environment variables can become cumbersome, especially when you have many variables to set, but the `python-dotenv` package provides a convenient way to manage environment variables by storing them in a `.env` file.

You can install the `python-dotenv` package using `pip`:

```bash
pip install python-dotenv
```

Then you will need to create a file called `.env` in the root directory of your project and add your environment variables to it:

```
DATABASE_CONNECTION=[this is my connection string]
SECRET_KEY=mysecretkey
BEST_PYTHON_BLOG=https://thepythoncorner.com
```

Now, to load the environment variables you just need to use the `load_dotenv` function from the `dotenv` module, like this:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print(f"Database Connection String: {os.environ['DATABASE_CONNECTION']}")
print(f"Secret Key: {os.environ['SECRET_KEY']}")
print(f"Best Python Blog: {os.environ['BEST_PYTHON_BLOG']}")
```

## Best Practices for Using Environment Variables

Here are some best practices for using environment variables in your Python applications:

1. **Keep Sensitive Information Secure**: Store sensitive information such as API keys and passwords in environment variables to keep them out of your source code.
2. **Use a `.env` File for Local Development**: Use a `.env` file to manage environment variables for local development and remember to add the `.env` file to your `.gitignore` file to prevent it from being committed to version control.
3. **Document Your Environment Variables**: Document the environment variables your application requires in a `README` file or a separate configuration file. Since your .env file will not be distribuited with the app, you need to make it clear for other developers that your codebase require some environment variables.

## Conclusion

Environment variables are a powerful tool for configuring applications and managing sensitive information. 
By using environment variables, you can keep your configuration settings secure, manage different environments more easily, and make your applications more portable. 
With the help of the `os` module and the `python-dotenv` package, you can easily access and manage environment variables in your Python applications.

