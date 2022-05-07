---
title: Managing Python versions with pyenv
date: 2022-05-07T17:37:47+02:00
author: "davide_mastromatteo"
excerpt: "Are you sure that you are installing Python right?"
header:
    teaser: https://imgs.xkcd.com/comics/retro_virus.png)
categories:
    - Dev
tags:
    - pyenv
    - version
    - python
---
![teaser](https://imgs.xkcd.com/comics/python_environment.png)

# What is pyenv?
Today's article is about one of the most impressive pieces of software Python-related I have ever seen: [`pyenv`](https://github.com/pyenv/pyenv).
`pyenv` is the most clever way of installing Python on your system and allows you to install and manage several different versions of 
Python specifying a different Python version for every project you have.

# The installation process 
If you're on a Mac and you are a [homebrew](https://brew.sh/index_it) user there's a specific [formulae](https://formulae.brew.sh/formula/pyenv) 
for that. If you don't know homebrew, it's a package manager for macOS and it's another great piece of software, go and check it out, don't 
miss it! If you have homebrew installed, you can simply get pyenv by using the following command:

```bash
$ brew install pyenv
```

If you are on Linux, you can simply download it from GitHub but the most convenient way is to use the [pyenv-installer](https://github.com/pyenv/pyenv-installer)
that is a simple script that will install it automatically on your distro, whatever it is, in the easiest possible way.

If you are on Windows... come on man, the 90s are over! ;)
Ok ok, no hard feelings guys, I was just joking! The fact is that this software doesn't exist on Windows but don't lose faith, there are at least two possibilities.
The first one is to use [pyenv-win](https://github.com/pyenv-win/pyenv-win), which is a specific fork working on windows by [Kiran Kumar Kotari](https://github.com/kirankotari).
I have to admit that I have never tried it though, so try it by yourself and leave a comment here to let us know how it was.
The second option (the one I actually use when I'm on Windows) is... to use the Linux version on [WSL2](https://docs.microsoft.com/en-gb/windows/wsl/install).
I know, I know... you may think that this is not a real solution, it's like cheating... but I honestly think that in 2022 if you are a 
developer you should consider moving to Unix or Unix like systems, like macOS or Linux, so even when I'm on Windows I heavily rely on the
Windows Subsystem for Linux, which I consider the best thing Microsoft did in the last 40 years...

However, to write this article since I have already installed and configured `pyenv` on all my systems, I have created a small Linux Lithium 
vm so to be able to start from scratch along with you. If you don't know Lithium, check [their website](https://www.bunsenlabs.org/index.html), it's
a very lightweight distro based on Debian and ideally a continuation of the [#!Linux](https://en.wikipedia.org/wiki/CrunchBang_Linux), 
which was an incredible distro based on Debian discontinued in 2013... 

However, let's start the installation!
Start your Linux terminal and execute the pyenv-installer script by executing `curl https://pyenv.run | bash`.

```bash
dave@hell:~$ curl https://pyenv.run | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   270  100   270    0     0    286      0 --:--:-- --:--:-- --:--:--   286
Cloning into '/home/dave/.pyenv'...
remote: Enumerating objects: 979, done.
remote: Counting objects: 100% (979/979), done.
remote: Compressing objects: 100% (451/451), done.
remote: Total 979 (delta 564), reused 659 (delta 401), pack-reused 0
Receiving objects: 100% (979/979), 481.70 KiB | 9.83 MiB/s, done.
Resolving deltas: 100% (564/564), done.
Cloning into '/home/dave/.pyenv/plugins/pyenv-doctor'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 11 (delta 1), reused 5 (delta 0), pack-reused 0
Unpacking objects: 100% (11/11), done.
Cloning into '/home/dave/.pyenv/plugins/pyenv-installer'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 16 (delta 1), reused 7 (delta 0), pack-reused 0
Unpacking objects: 100% (16/16), done.
Cloning into '/home/dave/.pyenv/plugins/pyenv-update'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 10 (delta 1), reused 5 (delta 0), pack-reused 0
Unpacking objects: 100% (10/10), done.
Cloning into '/home/dave/.pyenv/plugins/pyenv-virtualenv'...
remote: Enumerating objects: 61, done.
remote: Counting objects: 100% (61/61), done.
remote: Compressing objects: 100% (54/54), done.
remote: Total 61 (delta 11), reused 28 (delta 1), pack-reused 0
Unpacking objects: 100% (61/61), done.
Cloning into '/home/dave/.pyenv/plugins/pyenv-which-ext'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 10 (delta 1), reused 6 (delta 0), pack-reused 0
Unpacking objects: 100% (10/10), done.

WARNING: seems you still have not added 'pyenv' to the load path.

# Load pyenv automatically by appending
# the following to 
~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
and ~/.bashrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Restart your shell for the changes to take effect.

# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"
```

Ok, that was easy, wasn't it? Now all you have to do is to add the pyenv root directory **at the beginning** of your `PATH` environment 
variable.

Now edit your ~/.bashrc and add the following lines:
```bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

That's it, now log out and log in again to make your system accept and load these changes.

If everything worked as expected, you can try to execute `pyenv` and if you get something, you did it, the installation was ok, read on.

# Using pyenv

Now that we have `pyenv` installed, we can start using it. On my Lithium system, the default python version that comes installed with the 
system is the 2.7, which is terrible, isn't it? So we will download and install the last Python version available that at the moment is the 3.10.4.
With just a command, `pyenv` will download the source code and build our Python version directly on our system for us!

Before that, however, some libraries has to be installed and that are needed to build Python. 

So, since I'm on a Lithium Linux (that is a flavor of a Debian distro), I have to use the following command to install all the
reccomended dependencies: 

```bash
dave@hell:~$ sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```

If you are on a different distro, you can find the correct command to install all these dependencies [here](https://github.com/pyenv/pyenv/wiki/Common-build-problems/6dae5cd9c3f0c399e368a3a2e5120fb9debac366).

Ok, now that our dependencies are installed we are ready to install Python 3.10.4 by using `pyenv install 3.10.4 -v`:

```bash
dave@hell:~$ pyenv install 3.10.4 -v
...
Looking in links: /tmp/tmpzxxvet16
Processing /tmp/tmpzxxvet16/setuptools-58.1.0-py3-none-any.whl
Processing /tmp/tmpzxxvet16/pip-22.0.4-py3-none-any.whl
Installing collected packages: setuptools, pip
  WARNING: The scripts pip3 and pip3.10 are installed in '/home/dave/.pyenv/versions/3.10.4/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-22.0.4 setuptools-58.1.0
/tmp/python-build.20220506212137.7185 ~
~
Installed Python-3.10.4 to /home/dave/.pyenv/versions/3.10.4
```

The `-v` is just to have a verbose output because the installation won't be super fast and if you don't put this option, you could think 
that the system is hanging. On my Lithium vm, installed on a 2018 MacBook Pro, the installation took about 2 minutes.

Ok, now that we have installed Python 3.10.4, let's ask to pyenv which version we have available now:

```bash
dave@hell:~$ pyenv versions
* system (set by /home/dave/.pyenv/version)
  3.10.4
```

As you can see, we have the *system* version (that is the one bundled with my distro) and the 3.10.4 that I've just installed. 
Since the currently selected version is the *system* version (that's what that asterisk near *system* stands for), if we run the `python` 
command we are welcomed by the system version:

```bash
dave@hell:~$ python
Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

So, if we want to make sure that for the current user, the default Python installation will be the 3.10.4 one, we can just use the `global` 
keyword like this: 

```bash
dave@hell:~$ pyenv global 3.10.4
dave@hell:~$ 
```

Now, if we run the command `python` again we get the 3.10.4 version:

```bash
dave@hell:~$ python
Python 3.10.4 (main, May  6 2022, 21:22:43) [GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

That's cool uh?

Ok, but what if I have a specific project where I would like to use the 3.6.2 version for example?

Let's start by installing this version on our system:

```bash
dave@hell:~$ pyenv install 3.6.2
Downloading Python-3.6.2.tar.xz...
-> https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
Installing Python-3.6.2...
Installed Python-3.6.2 to /home/dave/.pyenv/versions/3.6.2

dave@hell:~$ 
```

Now, let's see the version available on our system:

```bash
dave@hell:~$ pyenv versions
  system
* 3.10.4 (set by /home/dave/.pyenv/version)
  3.6.2
dave@hell:~$ 
```

Cool, now let's enter in our project directory and let's set a specific Python version for that specific project by the `local` 
keyword:

```bash
dave@hell:~/mysupersecretproject$ pyenv local 3.6.2
dave@hell:~/mysupersecretproject$ 
```

Let's remain in our project directory and let's see the Python versions we can use now:

```bash
dave@hell:~/mysupersecretproject$ pyenv versions
  system
  3.10.4
* 3.6.2 (set by /home/dave/mysupersecretproject/.python-version)
dave@hell:~/mysupersecretproject$ 
```

Can you see it? Now the default version is the 3.6.2 and `pyenv` tells us even why this would be the default version for this directory, 
in fact with the `local` keyword we have created a hidden file named `.python-version` that specifies the python version that has to be 
used for our project! Let's do some tests:

```bash 
dave@hell:~/mysupersecretproject$ python
Python 3.6.2 (default, May  6 2022, 21:49:46) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
dave@hell:~/mysupersecretproject$ cat .python-version 
3.6.2
dave@hell:~/mysupersecretproject$ cd ..
dave@hell:~$ pyenv versions
  system
* 3.10.4 (set by /home/dave/.pyenv/version)
  3.6.2
dave@hell:~$ 
```

Great, the versioning is working great and the 3.6.2 is used **only** in the directory we chose for it!

Ok, I know, some of you are thinking "I don't want to use the standard Python installation, I need Jython, or Anaconda or Miniconda or ...". 
Well, the good news is that `pyenv` lets you choose other Python distributions as well. To know all the versions available try to use
the command `pyenv install --list` and hold on tight!

```bash
dave@hell:~$ pyenv install --list
Available versions:
  2.1.3
  2.2.3
  2.3.7
  2.4.0
  2.4.1
...
  3.3.4
  3.3.5
  3.3.6
  3.3.7
  3.4.0
...
  3.10.2
  3.10.3
  3.10.4
  3.11.0a7
  3.11-dev
  activepython-2.7.14
  activepython-3.5.4
  activepython-3.6.0
  anaconda-1.4.0
  anaconda-1.5.0
  anaconda-1.5.1
...
  anaconda3-2021.11
  graalpython-20.1.0
  graalpython-20.2.0
  graalpython-20.3.0
  graalpython-21.0.0
  graalpython-21.1.0
...
  ironpython-2.7.6.3
  ironpython-2.7.7
  jython-dev
  jython-2.5.0
  jython-2.5-dev
  jython-2.5.1
  jython-2.5.2
...
  mambaforge
  mambaforge-4.10.1-4
  mambaforge-4.10.1-5
  mambaforge-4.10.3-10
  micropython-dev
  micropython-1.9.3
  micropython-1.9.4
  micropython-1.10
  micropython-1.11
...
  miniconda3-4.5.11
  miniconda3-4.5.12
  miniconda3-4.6.14
  miniconda3-4.7.10
  miniconda3-4.7.12
...
  stackless-3.4-dev
  stackless-3.4.2
  stackless-3.4.7
  stackless-3.5.4
  stackless-3.7.5
dave@hell:~$ 

```

There are currently more than 560 versions of Python you can choose from. 

# Behind the magic

Now that you know the basic usage of pyenv you might wondering how it works. 
Well, it turns out that as usual, it is easier than you may expect.

Pyenv works by adding a special directory called `shims` in front of your PATH environment variable, like this:

```bash
$(pyenv root)/shims:/usr/local/bin:/usr/bin:/bin
```

and in this directory, there are all the python commands you are used to, like `python`, `pip` etc...
So the command you have inserted is actually hijacked by `pyenv`, which can pass the command to the Python installation you like.

When a shim is executed, the Python version to be used is chosen in the following order: 

- at first, it checks for a Python version specified in the `PYENV_VERSION` environment variable
- then it looks if there is a `.python-version` file in the current directory, created by the `pyenv local` command
- then it checks in order all the parent directories till the root one, looking for `.python-version` files to be used
- in the end, it looks for a `$(pyenv root)/version` file, that is the one that is created when you use the `pyenv global` command

All the Python versions installed by `pyenv` can be found under the directory `$(pyenv root)/versions` and can be uninstalled by the
`pyenv uninstall` command.

# To sum up

In this article, we have seen how easy it is to manage different Python versions either on a per-user or a per-project basis with pyenv.
For more information visit the [official GitHub page of the project](https://github.com/pyenv/pyenv#how-it-works) and feel free to submit
pull requests or file bugs on the issue tracker, the project is active and actively supported by hundreds of contributors.

Happy coding!
D.

