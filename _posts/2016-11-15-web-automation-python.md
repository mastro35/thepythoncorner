---
layout: post
author: Davide Mastromatteo
title: Web Automation in Python
tags: [web, splinter, selenium, webtest]
excerpt_separator: <!--more-->
---
Automation and web test. The Pythonic way.
<!--more-->

![](https://imgs.xkcd.com/comics/turing_test.png)

A couple of days ago I was in the need of automating simple browsing on the internet.
To be more specific I needed to visit my company website, click on a couple of specific links and then repeat this operation every few minutes. You are probably thinking that there is software that can perform what is called «automation test» but I am just too lazy to surf the web looking for a free program and writing code is really more fun so there was just one thing in my mind...

![](https://cdn-images-1.medium.com/max/800/1*x38OL4Y7YnkXsZLDLihs7Q.jpeg)

For this project, we’ll use [Splinter](https://splinter.readthedocs.io). 

According to the official website

> Splinter is an open source tool for testing web applications using Python. It lets you automate browser actions, such as visiting URLs and interacting with their items.

Splinter is just an abstraction layer on top of [Selenium](http://seleniumhq.org/) and makes easy to write automation tests for web applications. 

So, let’s pretend that we want to automate research on bing.com. 
First of all, we need to install Splinter. 
To do it, open a terminal and do a 

```console
pip install splinter
```

Once Splinter’s been installed we need to choose the browser to use.
By default, the system would use Firefox, but you can choose to use Chrome or IE as well.
Today we’ll use Chrome, so you will need to install both the Chrome browser and the Chrome web driver that you can find [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). 

If you use Windows or Linux the driver is just a standalone executable that you have to put in a directory listed in your PATH environment variable, if you use macOS you can get it through homebrew with:

```console
$ brew install chromedriver
```

Please note that if you prefer to use Firefox you will need to install [Gekodriver](https://github.com/mozilla/geckodriver).

Now, if you have installed both Splinter and a web driver, you can start coding:

```python
from splinter import Browser

with Browser('chrome') as browser:
    # Visit URL
    url = http://www.bing.com
    browser.visit(url)

    # fill the query form with our search term
    browser.fill('sb_form_q', 'mastro35 twitter')

    # find the search button on the page and click it
    button = browser.find_by_id('sb_form_go')
    button.click()
```

Once run, this script will let you achieve three major results:

1. You will see how easy it is to automate a simple search on Bing
2. You will have the access to my Twitter profile in case you want to follow me :)
3. You will have probably doubled the statistic about the daily Bing.com visits :))

However, this is just a small example of what you can do with Splinter.
It also allows you to find elements in page by their CSS, XPath, tag, name, text, id or value and if you want a more accurate control of the page or you need to do something more (like interacting with the old «frameset» tags) it expose also the web driver that allows you to use the Selenium low-level methods.

There’s no need to say that you can obviously get also the HTTP status code of the page you visited (using browser.status_code) and the HTML of the page (using browser.html).

Besides, the Splinter project is super well documented and that’s really important when you have to deal with third-party libraries.

One last thing: if you want to create an automation test that runs without the browser window, you can try [PhantomJS](http://phantomjs.org/).

According to their website

> PhantomJS is a headless WebKit scriptable with a JavaScript API. It has fast and native support for various web standards: DOM handling, CSS selector, JSON, Canvas, and SVG.

PhantomJS is simply amazing and works great with Splinter. 

Enjoy and... happy Pythoning!
D.