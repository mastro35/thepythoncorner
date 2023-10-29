---
title: Writing a FUSE filesystem in Python
date: 2017-02-28T00:11:19+01:00
author: Davide Mastromatteo
excerpt: "In this article, we will see how to create a FUSE filesystem in Python. Don't worry, it's easier than you thought,"
header:
  teaser:  https://imgs.xkcd.com/comics/porn_folder.png
categories:
  - Dev
tags:
  - Featured
  - Filesystem
  - Fuse
  - Linux
  - Python
redirect_from:
  - /2017/02/writing-a-fuse-filesystem-in-python
  - /2017/02/writing-a-fuse-filesystem-in-python/
  - /dev/writing-a-fuse-filesystem-in-python/
---
![teaser](https://imgs.xkcd.com/comics/porn_folder.png)

We ran into a problem last week. Our web application produces a lot of documents that have to be accessed frequently for a couple of months after they're created. However, in less than a year these documents will be almost never accessed anymore, but we need to keep them available for the web application and for tons of other legacy apps that *might* need to access them.

Now, these documents take a lot of space on our *expensive but super fast storage system* (let's call it **primary storage system** or **PSS** from now on) and we would like to be able to move them on the *cheaper, not so good and yet quite slow storage system* (that we're going to call **secondary storage system** or **SSS**) when we believe that they will not be accessed anymore.

Our idea was to move the older files to the SSS and to modify all the software that needs to access the storage so to look at the PSS first and in the case, nothing was found, to look at the SSS. This approach, however, meant that we should have to modify all the client software we had...

> "There are no problems, only opportunities" — I.R.

So, wouldn't it be great if we could create a virtual filesystem to map both the PSS and the SSS into a single directory?

And that's what we're gonna do today.

From the client software perspective, everything will remain unchanged, but under the hood all our read and write operations will be forwarded to the correct storage system.

Please note: I'm not saying that this is the best solution ever for this specific problem. There are probably better solutions to address this problem but... we have to talk about Python, don't we?

### What we'll need

To start this project we just need to satisfy a couple of prerequisites:

- Python
- A good OS

I assume that you already have Python (if not... what are you doing here?), and for what about the OS keep in mind that this article is based on **[FUSE](https://en.wikipedia.org/wiki/Filesystem_in_Userspace)**.

According to Wikipedia, **FUSE** is

> a software interface for Unix-like computer operating systems that lets non-privileged users create their own file systems without editing kernel code. This is achieved by running file system code in user space while the FUSE module provides only a "bridge" to the actual kernel interfaces.

FUSE is available for Linux, FreeBSD, OpenBSD, NetBSD (as puffs), OpenSolaris, Minix 3, Android and [macOS](https://osxfuse.github.io/).

So, if you use macOS you need to download and install FUSE, if you use Linux, keep in mind that Fuse has been merged into the mainstream Linux kernel in the 2.6.14 version, originally released in 2005, on October the 27th, so every recent version of Linux has it yet.

If you use Windows... well... I mean... I'm sorry buddy, but you didn't satisfy the second prerequisite...

### The fusepy module

First of all, to communicate with the FUSE module from Python you will need to install the **[fusepy](https://github.com/terencehonles/fusepy)** module. This module is just a simple interface to FUSE and MacFUSE. Nothing more than this, so go on and install it by using `pip`:

```console
pip install fusepy
```

### Let's start

There's a great start point for building our filesystem, and it's the [Stavros Korokithakis](https://twitter.com/stavros) code. What Stavros made is available on [his GitHub repo](https://github.com/skorokithakis/python-fuse-sample) and I will report it here:

```python
#!/usr/bin/env python

from __future__ import with_statement

import os
import sys
import errno

from fuse import FUSE, FuseOSError, Operations


class Passthrough(Operations):
    def __init__(self, root):
        self.root = root

    # Helpers
    # =======

    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    # Filesystem methods
    # ==================

    def access(self, path, mode):
        full_path = self._full_path(path)
        if not os.access(full_path, mode):
            raise FuseOSError(errno.EACCES)

    def chmod(self, path, mode):
        full_path = self._full_path(path)
        return os.chmod(full_path, mode)

    def chown(self, path, uid, gid):
        full_path = self._full_path(path)
        return os.chown(full_path, uid, gid)

    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        st = os.lstat(full_path)
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))

    def readdir(self, path, fh):
        full_path = self._full_path(path)

        dirents = ['.', '..']
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        for r in dirents:
            yield r

    def readlink(self, path):
        pathname = os.readlink(self._full_path(path))
        if pathname.startswith("/"):
            # Path name is absolute, sanitize it.
            return os.path.relpath(pathname, self.root)
        else:
            return pathname

    def mknod(self, path, mode, dev):
        return os.mknod(self._full_path(path), mode, dev)

    def rmdir(self, path):
        full_path = self._full_path(path)
        return os.rmdir(full_path)

    def mkdir(self, path, mode):
        return os.mkdir(self._full_path(path), mode)

    def statfs(self, path):
        full_path = self._full_path(path)
        stv = os.statvfs(full_path)
        return dict((key, getattr(stv, key)) for key in ('f_bavail', 'f_bfree',
            'f_blocks', 'f_bsize', 'f_favail', 'f_ffree', 'f_files', 'f_flag',
            'f_frsize', 'f_namemax'))

    def unlink(self, path):
        return os.unlink(self._full_path(path))

    def symlink(self, name, target):
        return os.symlink(name, self._full_path(target))

    def rename(self, old, new):
        return os.rename(self._full_path(old), self._full_path(new))

    def link(self, target, name):
        return os.link(self._full_path(target), self._full_path(name))

    def utimens(self, path, times=None):
        return os.utime(self._full_path(path), times)

    # File methods
    # ============

    def open(self, path, flags):
        full_path = self._full_path(path)
        return os.open(full_path, flags)

    def create(self, path, mode, fi=None):
        full_path = self._full_path(path)
        return os.open(full_path, os.O_WRONLY | os.O_CREAT, mode)

    def read(self, path, length, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def write(self, path, buf, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

    def truncate(self, path, length, fh=None):
        full_path = self._full_path(path)
        with open(full_path, 'r+') as f:
            f.truncate(length)

    def flush(self, path, fh):
        return os.fsync(fh)

    def release(self, path, fh):
        return os.close(fh)

    def fsync(self, path, fdatasync, fh):
        return self.flush(path, fh)


def main(mountpoint, root):
    FUSE(Passthrough(root), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    main(sys.argv[2], sys.argv[1])
```

Take a minute to analyze Stavros' code. It just implements a "passthrough filesystem", that just mount a directory into a mount point. For each operation requested to the mount point, it returns the python implementation on the real file of the mounted directory.

So, to try this code just save this file as Passthrough.py and run

```console
python Passthrough.py [directoryToBeMounted] [directoryToBeUsedAsMountpoint]
```

That's it! Now, your bare new filesystem is mounted on what you specified in the*[directoryToBeUsedAsMountpoint]* parameter and all the operations you will do on this mount point will be silently passed to what you specified in the *[directoryToBeMounted]* parameter.

Really cool, even if a little bit useless so far... :)

So, how can we implement our filesystem as said before? Thanks to Stavros, our job is quite simple. We just need to create a class that inherits from Stavros' base class and overrides some methods.

The first method we have to override is the _full_path method. This method is used in the original code to take the mount point relative path and translate it to the real mounted path. In our filesystem, this will be the most difficult piece of code, because we will need to add some logic to define if the requested path belongs to the PSS or to the SSS. However, also this "most difficult piece of code" is quite trivial.

We just need to verify if the requested path exists at least in one storage system. If it does, we will return the real path, if not, we will assume that the path has been requested for a write operation on a file that does not exist yet. So we will try to look if the directory name of the path exists in one of the storage systems and we will return the correct path.

A look at the code will make things more clear:

```python
    def _full_path(self, partial, useFallBack=False):
        if partial.startswith("/"):
            partial = partial[1:]

        # Find out the real path. If has been requesetd for a fallback path,
        # use it
        path = primaryPath = os.path.join(
            self.fallbackPath if useFallBack else self.root, partial)

        # If the pah does not exists and we haven't been asked for the fallback path
        # try to look on the fallback filessytem
        if not os.path.exists(primaryPath) and not useFallBack:
            path = fallbackPath = os.path.join(self.fallbackPath, partial)

            # If the path does not exists neither in the fallback fielsysem
            # it's likely to be a write operation, so use the primary
            # filesystem... unless the path to get the file exists in the
            # fallbackFS!
            if not os.path.exists(fallbackPath):
                # This is probabily a write operation, so prefer to use the
                # primary path either if the directory of the path exists in the
                # primary FS or not exists in the fallback FS

                primaryDir = os.path.dirname(primaryPath)
                fallbackDir = os.path.dirname(fallbackPath)

                if os.path.exists(primaryDir) or not os.path.exists(fallbackDir):
                    path = primaryPath

        return path
```

Done this, we have almost finished. If we're using a Linux system we have also to override the "*getattr" *function to return also the ‘st_blocks' attribute (it turned out that without this attribute the "du" bash command doesn't work as expected).

So, we need just to override this method and return the extra attribute:

```python
    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        st = os.lstat(full_path)
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                                                        'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid', 'st_blocks'))
```

And then we need to override the "*readdir*" function, that is the generator function that is called when someone does a "ls" in our mount point. In our case, the "ls" command has to list the content of both our primary storage system and our secondary storage system.

```python
def readdir(self, path, fh):
        dirents = ['.', '..']
        full_path = self._full_path(path)
        # print("listing " + full_path)
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        if self.fallbackPath not in full_path:
            full_path = self._full_path(path, useFallBack=True)
            # print("listing_ext " + full_path)
            if os.path.isdir(full_path):
                dirents.extend(os.listdir(full_path))
        for r in list(set(dirents)):
            yield r
```

We've almost finished, we just need to override the "main" method because we need an extra parameter (in the original code we had one directory to be mounted and one directory to be used as a mount point, in our filesystem we have to specify two directories to be mounted into the mount point).

So here there is the full code of our new file system "dfs" (the "Dave File System" :D )

```python
#!/usr/bin/env python

import os
import sys
import errno

from fuse import FUSE, FuseOSError, Operations
from Passthrough import Passthrough

class dfs(Passthrough):
    def __init__(self, root, fallbackPath):
        self.root = root
        self.fallbackPath = fallbackPath
        
    # Helpers
    # =======
    def _full_path(self, partial, useFallBack=False):
        if partial.startswith("/"):
            partial = partial[1:]
        # Find out the real path. If has been requesetd for a fallback path,
        # use it
        path = primaryPath = os.path.join(
            self.fallbackPath if useFallBack else self.root, partial)
        # If the pah does not exists and we haven't been asked for the fallback path
        # try to look on the fallback filessytem
        if not os.path.exists(primaryPath) and not useFallBack:
            path = fallbackPath = os.path.join(self.fallbackPath, partial)
            # If the path does not exists neither in the fallback fielsysem
            # it's likely to be a write operation, so use the primary
            # filesystem... unless the path to get the file exists in the
            # fallbackFS!
            if not os.path.exists(fallbackPath):
                # This is probabily a write operation, so prefer to use the
                # primary path either if the directory of the path exists in the
                # primary FS or not exists in the fallback FS
                primaryDir = os.path.dirname(primaryPath)
                fallbackDir = os.path.dirname(fallbackPath)
                if os.path.exists(primaryDir) or not os.path.exists(fallbackDir):
                    path = primaryPath
        return path
      
    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        st = os.lstat(full_path)
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                                                        'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid', 'st_blocks')) 

    def readdir(self, path, fh):
        dirents = ['.', '..']
        full_path = self._full_path(path)
        # print("listing " + full_path)
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        if self.fallbackPath not in full_path:
            full_path = self._full_path(path, useFallBack=True)
            # print("listing_ext " + full_path)
            if os.path.isdir(full_path):
                dirents.extend(os.listdir(full_path))
        for r in list(set(dirents)):
            yield r
            
def main(mountpoint, root, fallbackPath):
    FUSE(dfs(root, fallbackPath), mountpoint, nothreads=True,
         foreground=True, **{'allow_other': True})

if __name__ == '__main__':
    mountpoint = sys.argv[3]
    root = sys.argv[1]
    fallbackPath = sys.argv[2]
    main(mountpoint, root, fallbackPath)
```

That's it, now if we issue the command ...

```console
python dfs.py /home/dave/Desktop/PrimaryFS/ /home/dave/Desktop/FallbackFS/ /home/dave/Desktop/myMountpoint/
```

... we get a mount point (/home/dave/Desktop/myMountpoint/) that lists both the content of /home/dave/Desktop/PrimaryFS/ and /home/dave/Desktop/FallbackFS/ and that works as expected.

Yes, it was THAT easy!

### A couple of notes

It worth to be noted that:

- when we instantiate the FUSE object with **foreground=False **we can run the operation in the background.
- The **{‘allow_other': True}** is really important if you need to share the mount point over the network with Samba (omitting this prevents you to share this directory).

That's all folks, now stop reading and start to develop your first filesystem with Python! :)

D.
