---
title: "Working with EBCDIC in Python"
date: 2020-04-30T00:18:49+01:00
author: "davide_mastromatteo"
excerpt: "In this tutorial, you will learn how to work with EBCDIC code in Python"
header:
  teaser: https://imgs.xkcd.com/comics/the_history_of_unicode.png
categories:
  - Dev
tags:
  - EBCDIC
  - python
  - encoding
  - IBM
  - Mainframe
redirect_from:
  - /dev/working-with-ebcdic-python/
---
![teaser](https://imgs.xkcd.com/comics/the_history_of_unicode.png)  
A couple of months ago I had to rewrite a program that used to be executed on a IBM System Z9. For those of you who don't know what I'm talking about... "it's a [mainframe](https://en.wikipedia.org/wiki/IBM_System_z9), kiddo"!

However, even if I do know what a mainframe is, when I looked at the input files I was having to work with, I was like... "oh my gosh, what is this stuff?!?!"

It took me a while to understand that what I was seeing wasn't a set of standard ASCII files but a set of weird EBCDIC files. EBCDIC is an eight bit character encoding used on IBM mainframe, or to tell it in other words... "it's 1960's technology, baby"!

It's something so old that it's standard has been thought to be "Punched card friendly". What? You don't know what a punched card is? Lucky you, kiddo... [check this out](https://en.wikipedia.org/wiki/Punched_card).

However... when I looked at this EBCDIC encoded files I felt lost... "why am I still doing this work?" I kept repeating. And then, since I'm a Pythonista, without even notice it, I started my console and I tried ...

```console
$ pip install ebcdic
Collecting ebcdic
  Downloading ebcdic-1.1.1-py2.py3-none-any.whl (128 kB)
     |████████████████████████████████| 128 kB 1.9 MB/s
Installing collected packages: ebcdic
Successfully installed ebcdic-1.1.1
```

Wait... what? No error? Are you telling me that someone wrote an EBCDIC package to handle this stuff? 

GOD BLESS PYTHON! 
(and Thomas Aglassinger who wrote this useful [library](https://pypi.org/project/ebcdic/))

Once you have installed the library, just use the `.encode()` and the `.decode()` methods on a string specifying one of the supported codec:

```
* cp290 - Japan (Katakana)
* cp420 - Arabic bilingual
* cp424 - Israel (Hebrew)
* cp833 - Korea Extended (single byte)
* cp838 - Thailand
* cp870 - Eastern Europe (Poland, Hungary, Czech, Slovakia, Slovenia, Croatian, Serbia, Bulgarian); represents Latin-2
* cp1097 - Iran (Farsi)
* cp1140 - Australia, Brazil, Canada, New Zealand, Portugal, South Africa, USA
* cp1141 - Austria, Germany, Switzerland
* cp1142 - Denmark, Norway
* cp1143 - Finland, Sweden
* cp1144 - Italy
* cp1145 - Latin America, Spain
* cp1146 - Great Britain, Ireland, North Ireland
* cp1147 - France
* cp1148 - International
* cp1148ms - International, Microsoft interpretation; similar to cp1148 except that 0x15 is mapped to 0x85 (“next line”) instead if 0x0a (“linefeed”)
* cp1149 - Iceland
* cp037 - Australia, Brazil, Canada, New Zealand, Portugal, South Africa; similar to cp1140 but without Euro sign
* cp273 - Austria, Germany, Switzerland; similar to cp1141 but without Euro sign
* cp277 - Denmark, Norway; similar to cp1142 but without Euro sign
* cp278 - Finland, Sweden; similar to cp1143 but without Euro sign
* cp280 - Italy; similar to cp1141 but without Euro sign
* cp284 - Latin America, Spain; similar to cp1145 but without Euro sign
* cp285 - Great Britain, Ireland, North Ireland; similar to cp1146 but without Euro sign
* cp297 - France; similar to cp1147 but without Euro sign
* cp500 - International; similar to cp1148 but without Euro sign
* cp500ms - International, Microsoft interpretation; identical to codecs.cp500 similar to ebcdic.cp500 except that 0x15 is mapped to 0x85 (“next line”) instead if 0x0a (“linefeed”)
* cp871 - Iceland; similar to cp1149 but without Euro sign
* cp875 - Greece; similar to cp9067 but without Euro sign and a few other characters
* cp1025 - Cyrillic
* cp1047 - Open Systems (MVS C compiler)
* cp1112 - Estonia, Latvia, Lithuania (Baltic)
* cp1122 - Estonia; similar to cp1157 but without Euro sign
* cp1123 - Ukraine; similar to cp1158 but without Euro sign
```

So, in my case, when I needed to encode a string, I had to use this piece of code to get a sequence of encoded EBCDIC bytes:

```python
>>> my_string = "is this fun or useless?"
>>> my_encoded_string = my_string.encode('cp1141')
>>> print(my_encoded_string)
b'\x89\xa2@\xa3\x88\x89\xa2@\x86\xa4\x95@\x96\x99@\xa4\xa2\x85\x93\x85\xa2\xa2o'
```

... and this piece of code when I had something to be decoded:

```python
>>> print(my_encoded_string.decode('cp1141'))
is this fun or useless?
```

Super easy, uh? Keep up the great work, kiddo(s), and happy Pythoning! =)

D.
