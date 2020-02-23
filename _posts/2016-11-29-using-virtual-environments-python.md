---
title: "Using Virtual Environments in Python"
date: 2016-11-29T00:00:49+01:00
author: Davide Mastromatteo
excerpt: "virtualenv, virtualenv-wrapper, pyvenv, python3 -m venv... What are they? Here you will find everything you need to know about virtual environments in Python!"
header:
  teaser: https://imgs.xkcd.com/comics/python.png
categories:
  - Dev
tags:
  - Virtual Environments
  - virtualenv
  - environments
  - python
redirect_from:
  - /2016/11/using-virtual-environments-with-python
  - /2016/11/using-virtual-environments-with-python/
---
![teaser](https://imgs.xkcd.com/comics/python.png)

Working with Python is like to have superpowers. When you need to do something and you don't know where to start from, you can google your problem and usually, you get aware that someone has already had your problem and created a library for the community.
Whichever is your need...

> *"there's a lib for that!"*

This is so deep inside the Python culture that if you start your python interpreter and you do a...

```python
>>> import antigravity
```

... you are redirected to [this xkcd comic](https://xkcd.com/353/).

Ok, so Python encourages the usage of third-party libraries but using these libraries you will soon have to deal with the versioning problem.

Let's say that your super new project xxx needs the version 2.5 of the library yyy, but you can't install the 2.5 version of the yyy library because your old project zzz needs the version 1.7 of that library.
Moreover, the old project zzz use Python 2.7 while the new one has been written using Python 3.5.

What are you supposed to do to sort this mess out? The pythonic answer to this common problem is **Virtual environments**.

Using virtual environments you will be able to assign a completely different environment to each project you're working on, installing for each one different library, dependencies and why not, even a different Python interpreter! And all this leaving the global `site-packages` directory on your pc will free from any other third party package.

It sounds cool, uh?

Let's see how to do this.

## virtualenv, virtualenv-wrapper, pyvenv, python3 -m venv... Are you kidding me?

There are several ways to create virtual environments and I think this is the main reason why usually beginners tend not to use virtual environments because it's quite common for the beginner to get lost on this topic. In this article, we'll try to make this subject a little bit clearer.

### virtualenv

The first method you have to create virtual environments is by using [Ian Bicking's *virtualenv*](http://www.virtualenv.org/). This is a tool that has been around for a long time and that allows you to create virtual environments both for Python 2.7 and Python 3.x. When you create a virtual environment, it lets you specify which version of Python to use and it automatically installs the pip utility on the created virtual environment, so that you can just start to `pip install` whatever you need. To install virtualenv just use `pip`:

```console
$ pip install virtualenv
```

Once you've done this, you can create a virtualenv simply typing:

```console
$ virtualenv NameOfYourVirtualEnvironment
```

where `NameOfYourVirtualEnvironment` is the name of the virtual environment you're going to create. This command will create, **in the current directory**, a subdirectory named `NameOfYourVirtualEnvironment` containing all the stuff you need, the python interpreter and the pip utility.

Once you have created a virtual environment you can simply start using it by executing the `activate` script that you will find into the `NameOfYourVirtualEnvironment/bin` directory (if you are using Windows it is named `activate.bat` and it's available under `NameOfYourVirtualEnvironment` directory).

So, to activate your new virtual environment simply type:

```console
$ source ./NameOfYourVirtualEnvironment/bin/activate
```

your prompt will change and you will see the name of your virtual environment inside parentheses at the beginning of the command line, meaning that you have activated the virtual environment in the correct way. Now, let's try to install a package to see what happen:

```console
(NameOfYourVirtualEnvironment) $ pip install pytyler
```

Perfect, if everything was ok now you have installed the package pytyler only on your virtual environment. If you're skeptic, try to start the python interpreter and import the module:

```console
(NameOfYourVirtualEnvironment) $ python -c import tyler
```

and look no importing errors! :) 

To exit from your virtual environment you just need to issue the command `deactivate`

```console
(NameOfYourVirtualEnvironment) $ deactivate
```

doing this, you will see that your command prompt will change again, back to the standard prompt, meaning that you are not anymore inside your virtual environment. Now, try to import the module `tyler` again:

```console
$ python -c import tyler
```

and you will get:

```console
ImportError: No module named tyler
```

This is the expected behavior and proves that you have installed the `pytyler` package ONLY into the virtual environment, so it is not available system-wide.

Ok, if everything is clear so far let's take a step forward. As I said before, when you create a virtual environment the `virtualenv` utility puts inside the environment also the default python interpreter that you have installed on your computer, the one that starts when you just type `python` from the command line that is probably the one that is installed in the `/usr/bin/python` directory (type `which python` if you want to be sure). This usually means python 2.7 (at least on my Debian Jessie machine). But what if you want to use another version of python? Well, this is quite easy actually... try to write:

```console
$ virtualenv -p /usr/bin/python3 AnotherVirtualEnvironmentName
```

and you will create another virtual environment named `AnotherVirtualEnvironmentName` that uses python 3. Deleting a virtual environment is just as easy as removing its directory, so to destroy the virtual environments you have just created type: 

```console
$ rm -rf NameOfYourVirtualEnvironment
```

### virtualenvwrapper

`virtualenvwrapper` is just a wrapper around virtualenv that make easier (yes, it's possible) working with virtual environments. Let's start with the installation of `virtualenvwrapper` (if you use Windows the package name is `virtualenvwrapper-win`)

```console
$ pip-install virtualenvwrapper
```

Please note that `virtualenv` is a dependency for `virtualenvwrapper`, so if you don't have `virtualenv` istalled yet this command will install it for you before actually installing `virtualenvwrapper`. Now, once you've installed the wrapper, you just need to execute the `virtualenvwrapper.sh` script every time you want to use it, so let's put it into your `.bashrc` file:

```
$ cd
$ echo source /usr/local/bin/virtualenvwrapper.sh >> .bashrc
```

Now, quit the current terminal and reopen it to execute the script and start working with virtualenvwrapper. Here there are the basic commands you can use:

- To create a virtual environment:

```
$ mkvirtualenv NameOfTheVirtualEnv
```

- To activate a virtual environment:

```
$ workon NameOfTheVirtualEnv
```

- To delete a virtual environment:

```
$ rmvirtualenv NameOfTheVirtualEnv
```

- To list all the virtual environment previously created:

```
$ lsvirtualenv
```

This is the feature that I like most of this script, and it's made possible by the fact that now, all the environments you create with `mkvirtualenv` are created under the `~/.virtualenvs` directory, so... no more mess on the filesystem! If you want to change the directory where the virtual environments are stored, you just need to specify the directory of your choice in the `WORKON_HOME` bash variable.

### the venv module

Now that you know almost everything about virtual environments you can easily create, activate and destroy virtual environments. So... why you should need to know something about `venv`? The answer is in the [PEP405](https://www.python.org/dev/peps/pep-0405): `venv` is a python module very similar to `virtualenv` but that comes by default as a part of the standard Python library since the release of Python 3.3, that dates back to September the 29th of 2012. It's basically `virtualenv` *written the right way* because being part of the standard distribution of Python it can use some Python internals that couldn't be used by `virtualenv`.

So, while `virtualenv` tries to trick the system with some hack to make everything work, `venv` doesn't. Moreover, `venv` is part of the Python distribution and this means that you don't need to install anything to start using it, if you use a recent version of Python it's already installed and it just works out of the box. The only drawback is that `venv` **is not available for Python versions prior the 3.3**, so, if you work on a project written in Python 2.7 for example, you can't use `venv` and you're stuck with `virtualenv`.

At the first release, to use the `venv` module you could use a script, that was named `pyvenv` but according to the official documentation:

> *The pyvenv script has been deprecated as of Python 3.6 in favor of using python3 -m venv to help prevent any potential confusion as to which Python interpreter a virtual environment will be based on.*

So, since it's going to be deprecated, forgot the `pyenv` script and just use the module as suggested. To create a virtual environment with the `venv` module just type:

```
$ python3 -m venv NameOfTheVirtualEnv
```

To activate the virtual environment use the active script in the `./bin` subfolder of the created virtual environment directory and as always, to delete the virtual environment simply get rid of its directory.

### The bottom line

I hope this article could have made the virtual environment topic clearer. To sum up:

- To create a virtual environment you have just to choose if you want to use `virtualenv` or the `venv` module.
- `virtualenv` works for both Python 2.7 and Python 3.x, the `venv` module is available only for Python 3.3 or higher.
- `virtualenvwrapper` is a wrapper that help you to use `virtualenv`, so if you need `virtualenv` probably the better choice is to use `virtualenvwrapper` (but it's a matter of taste).
- `pyvenv` is just a wrapper around the venv module and it's going to be deprecated. So... forget it right now!

You haven't decided yet?

- If you are still using Python 2.7 my advice is to use `virtualenvwrapper`.
- If you use only Python 3.3 or later, I think the best choice is to use the `venv` module. It's already present on your Python standard library, it's raccomended by the PEP 405, the virtual environments that it creates are smaller and it has also an API if you want to extend it.

Now, stop reading and go coding on a virtual environment! :)

Enjoy!
D.
