---
title: "How To Open a File in Python Without Locking It"
excerpt: "Opening a file on Windows with Python without locking it could be tricky. I've lost a couple of hours on trying to understand how do it. If you want to save this time, keep reading!"
header:
  teaser: https://imgs.xkcd.com/comics/still_in_use.png
categories:
  - Dev
tags:
  - file
  - lock
  - python
redirect_from:
  /2016/10/python-how-to-open-a-file-on-windows-without-locking-it
---
When I use python I’m usually on Linux or macOS but last week I had to write a python script on Windows.  
Yes, Windows! You know... that place where slashes are misoriented, drives are named with a single alphabet letter and “tail” and “grep” commands are usually considered less important than "Clippy".

![clippy](https://cdn-images-1.medium.com/max/800/1*eTEvMXSe7JqbnYEu6U2d5w.jpeg){: .align-center}

However, working on windows I’ve discovered something I considered weird: opening a file on Windows with the open() method, actually locks the file and prevents it from deletion.
So, while this is being executed...

```python
for line in open(prova.log):
    print(line)
```

... you can’t delete the “prova.log” file.

But this doesn’t happen on Linux or macOS.
So, if you need to open a file without locking it, you need to use Mark Hammond’s [pypiwin32](https://pypi.python.org/pypi/pypiwin32), the Python extensions for Microsoft Windows that provide access to much of the Win32 API.

In fact, by using the Win32 API you can ...

```python
import os
import win32file
import msvcrt

filename = prova.log

# get an handle using win32 API, specifyng the SHARED access!
handle = win32file.CreateFile(filename,
                                win32file.GENERIC_READ,
                                win32file.FILE_SHARE_DELETE |
                                win32file.FILE_SHARE_READ |
                                win32file.FILE_SHARE_WRITE,
                                None,
                                win32file.OPEN_EXISTING,
                                0,
                                None)

# detach the handle
detached_handle = handle.Detach()

# get a file descriptor associated to the handle
file_descriptor = msvcrt.open_osfhandle(
    detached_handle, os.O_RDONLY)

# open the file descriptor
file = open(file_descriptor)

for line in file:
    print(line)
```

... you can delete the file while you are reading from it.

That’s cool, isn’t it?

Happy coding!  
D.
