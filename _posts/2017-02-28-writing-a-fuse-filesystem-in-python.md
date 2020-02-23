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
  /2017/02/writing-a-fuse-filesystem-in-python
---
We ran into a problem last week. Our web application produces a lot of documents that have to be accessed frequently for a couple of months after they’re created. However, in less than a year these documents will be almost never accessed anymore, but we need to keep them available for the web application and for tons of other legacy apps that <em>might</em> need to access them.

Now, these documents take a lot of space on our <em>expensive but super fast storage system</em> (let’s call it <strong>primary storage system</strong> or <strong>PSS</strong> from now on) and we would like to be able to move them on the <em>cheaper, not so good and yet quite slow storage system</em> (that we’re going to call <strong>secondary storage system</strong> or <strong>SSS</strong>) when we believe that they will not be accessed anymore.

Our idea was to move the older files to the SSS and to modify all the software that needs to access the storage so to look at the PSS first and in the case, nothing was found, to look at the SSS. This approach, however, meant that we should have to modify all the client software we had…

<h4>“there are no problems, only opportunities” — cit I.R.</h4>

So, wouldn’t it be great if we could create a virtual filesystem to map both the PSS and the SSS into a single directory?

And that’s what we’re gonna do today.

From the client software perspective, everything will remain unchanged, but under the hood all our read and write operations will be forwarded to the correct storage system.

Please note: I’m not saying that this is the best solution ever for this specific problem. There are probably better solutions to address this problem but… we have to talk about Python, don’t we?

<h4>What we’ll need</h4>

To start this project we just need to satisfy a couple of prerequisites:

<ul>
    <li>Python</li>
    <li>A good OS</li>
</ul>

I assume that you already have Python (if not… what are you doing here?), and for what about the OS keep in mind that this article is based on <a href="https://en.wikipedia.org/wiki/Filesystem_in_Userspace" target="_blank" rel="noopener noreferrer">FUSE</a>.

According to Wikipedia, FUSE is

<blockquote><em>a software interface for Unix-like computer operating systems that lets non-privileged users create their own file systems without editing kernel code. This is achieved by running file system code in user space while the FUSE module provides only a “bridge” to the actual kernel interfaces.</em></blockquote>

FUSE is available for Linux, FreeBSD, OpenBSD, NetBSD (as puffs), OpenSolaris, Minix 3, Android and<a href="https://osxfuse.github.io/" target="_blank" rel="noopener noreferrer">macOS</a>

So, if you use macOS you need to download and install FUSE, if you use Linux, keep in mind that Fuse has been merged into the mainstream Linux kernel in the 2.6.14 version, originally released in 2005, on October the 27th, so every recent version of Linux has it yet.

If you use Windows… well… I mean… I’m sorry buddy, but you didn’t satisfy the second prerequisite…

<h4>The fusepy module</h4>

First of all, to communicate with the FUSE module from Python you will need to install the <a href="https://github.com/terencehonles/fusepy" target="_blank" rel="noopener noreferrer"><strong>fusepy</strong></a> module. This module is just a simple interface to FUSE and MacFUSE. Nothing more than this, so go on and install it by using pip:

<pre><code>pip install fusepy</code></pre>

<h4>Let’s start</h4>

There’s a great start point for building our filesystem, and it’s the <a href="https://twitter.com/stavros" target="_blank" rel="noopener noreferrer">Stavros Korokithakis</a> code. What Stavros made is available on <a href="https://github.com/skorokithakis/python-fuse-sample" target="_blank" rel="noopener noreferrer">his GitHub repo</a> and I will report it here:

https://gist.github.com/mastro35/0c87b3b96278ef1bd0a6401ff552195e

Take a minute to analyze Stavros’ code. It just implements a “passthrough filesystem”, that just mount a directory into a mount point. For each operation requested to the mount point, it returns the python implementation on the real file of the mounted directory.

So, to try this code just save this file as Passthrough.py and run

<pre><code>python Passthrough.py [directoryToBeMounted] [directoryToBeUsedAsMountpoint]</code></pre>

That’s it! Now, your bare new filesystem is mounted on what you specified in the<em>[directoryToBeUsedAsMountpoint]</em> parameter and all the operations you will do on this mount point will be silently passed to what you specified in the <em>[directoryToBeMounted]</em> parameter.

Really cool, even if a little bit useless so far… :)

So, how can we implement our filesystem as said before? Thanks to Stavros, our job is quite simple. We just need to create a class that inherits from Stavros’ base class and overrides some methods.

The first method we have to override is the _full_path method. This method is used in the original code to take the mount point relative path and translate it to the real mounted path. In our filesystem, this will be the most difficult piece of code, because we will need to add some logic to define if the requested path belongs to the PSS or to the SSS. However, also this “most difficult piece of code” is quite trivial.

We just need to verify if the requested path exists at least in one storage system. If it does, we will return the real path, if not, we will assume that the path has been requested for a write operation on a file that does not exist yet. So we will try to look if the directory name of the path exists in one of the storage systems and we will return the correct path.

a look at the code will make things more clear:

https://gist.github.com/mastro35/6ae5e47f29334f89c0ebfbb088184767

Done this, we have almost finished. If we’re using a Linux system we have also to override the "<em>getattr" </em>function to return also the ‘st_blocks’ attribute (it turned out that without this attribute the “du” bash command doesn’t work as expected).

So, we need just to override this method and return the extra attribute:

https://gist.github.com/mastro35/8f55e87811c05ccdc5a860058d950354

And then we need to override the "<em>readdir</em>" function, that is the generator function that is called when someone does a “ls” in our mount point. In our case, the “ls” command has to list the content of both our primary storage system and our secondary storage system.

https://gist.github.com/mastro35/fc1937dfb13653c6d6a8848864384abf

We’ve almost finished, we just need to override the “main” method because we need an extra parameter (in the original code we had one directory to be mounted and one directory to be used as a mount point, in our filesystem we have to specify two directories to be mounted into the mount point).

So here there is the full code of our new file system “dfs” (the “Dave File System” :D )

https://gist.github.com/mastro35/9ae0e4f4bbe6bda0c540986cb9f7c47c

That’s it, now if we issue the command …

<pre><code>python dfs.py /home/dave/Desktop/PrimaryFS/ /home/dave/Desktop/FallbackFS/ /home/dave/Desktop/myMountpoint/</code></pre>

… we get a mount point (/home/dave/Desktop/myMountpoint/) that lists both the content of /home/dave/Desktop/PrimaryFS/ and /home/dave/Desktop/FallbackFS/ and that works as expected.

Yes, it was THAT easy!

<h4>A couple of notes</h4>

It worth to be noted that:

<ol>
    <li>when we instantiate the FUSE object with <strong>foreground=False </strong>we can run the operation in the background.</li>
    <li>The <strong>**{‘allow_other’: True}</strong> is really important if you need to share the mount point over the network with Samba (omitting this prevents you to share this directory).</li>
</ol>

That’s all folks, now stop reading and start to develop your first filesystem with Python! :)

D.