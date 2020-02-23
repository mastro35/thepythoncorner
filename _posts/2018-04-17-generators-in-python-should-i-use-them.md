---
title: When To Use Generators in Python
date: 2018-04-17T11:46:00+02:00
author: Davide Mastromatteo
excerpt: "Let's talk about when to use generators in Python"
header:
  teaser: https://imgs.xkcd.com/comics/goto.png
categories:
  - Dev
tags:
  - Featured
  - Generators
  - Python
redirect_from:
  /2018/04/generators-in-python-should-i-use-them
---

<!-- wp:paragraph -->
<p>Following a request of a reader, today we’re going to discuss when to use iterators and generators in Python.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First of all, it’s important to know what iterators and generators are, so if you don’t know exactly what they are, I suggest to have a look at <a href="https://www.thepythoncorner.com/2018/05/iterators-and-generators-in-python.html" target="_blank" rel="noopener noreferrer">my previous article</a> on this topic.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now that everything is clear, we can start analyzing when to use these features.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>Let’s start saying that if you have read my previous article, the use of the iterator protocol should be quite clear: you use iterator protocol when you have a custom object that you want to be “<em>iterable</em>”.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That’s it, so easy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you want to use your custom object in a loop with something like</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">for i in my_object():
    # do something
    pass</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>you just need to adopt the iterator protocol.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But what about generators?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When am I supposed to write a generator instead of a simple function that returns a list of objects?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well, I have to admit that this can be a little bit tricky for a beginner… so let’s try to answer this question pretending to be there to write a function that returns a list of objects and let’s answer the following questions.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Do I need all the items of the returned&nbsp;list?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This is the first question you should ask yourself when writing a function that returns a list of objects. If the answer is “no”, that probably means that a generator would be a better choice because its main feature is the “lazy evaluation”.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With a generator, you generate a result <strong>only when you really need it</strong>, so if you’re not going to use all the items in the list, why bother creating them?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You will save time and resources not creating them and your users will be happier!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To make an example, have a look at this program.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import time
import random

def get_winning_numbers():
    random.seed()
    elements = []
    for i in range (0,10):
        time.sleep(1) # let's simulate some kind of delay
        elements.append(random.randint(1,10))

    return elements

random.seed()
my_number = random.randint(1,10)
print (&quot;my number is &quot; + str(my_number))

for winning_number in get_winning_numbers():
    print(winning_number)
    if my_number == winning_number:
        print (&quot;you win!&quot;)
        break

</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>The function “get_winning_numbers” is a time-consuming function that generates 10 random “winning numbers” (to simulate the “time-consuming function” we have added a delay of a second for every number generated).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The winning numbers are then checked against “my_number”; if my_number is in these 10 numbers, the player wins and the execution ends.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Made in this way, however, you have always to wait at least 10 seconds because all the winning numbers <strong>are all generated before </strong>the check against the player lucky number. That’s a waste of time because if the first of the winning numbers were the player’s number, we’d had generated 9 other winning numbers (using a time-consuming function) that we don’t need and that we will never use.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Using a generator, we can solve this problem pretty easily:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import time
import random

def get_winning_numbers():
    random.seed()
    for i in range(0,10):
        time.sleep(1)  # let's simulate some kind of delay
        yield random.randint(1,10)

random.seed()
my_number = random.randint(1,10)
print (&quot;my number is &quot; + str(my_number))

for winning_number in get_winning_numbers():
    print(winning_number)
    if my_number == winning_number:
        print (&quot;you win!&quot;)
        break

</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>We don’t need to make a big change to our program, we have the same result but the execution is often faster than the old version. In fact, now if the first winning number is equal to the lucky number of the player, we generate just that number, the player wins and the execution ends in just one second.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Do I need to be notified while the results of the list are generated?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If the answer to this question is yes, well, you will probably need a generator.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Think about a function that searches something on your filesystem or any other slow device and returns a list of results. If your function takes 5 seconds to find every single element and there are just 4 elements to be found, you have to wait 20 seconds before getting the results.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import time

def elements():
    elements = []
    for i in range (0,4):
        # simulate a slow search
        time.sleep(5)
        elements.append(i)
    return elements

print(&quot;start&quot;)
print(elements())
print(&quot;end&quot;)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In this case, even if you need all the four elements before going on, your app will seem to be frozen for 20 seconds, and this could be annoying for the user.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Wouldn’t it be better to be notified after every result, even just to have the time to update the user interface, maybe showing the partial results found or even a simple progress bar?</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import time

def elements():
    elements = []
    for i in range (0,4):
        # simulate a slow search
        time.sleep(5)
        yield(i)

print(&quot;start&quot;)
for i in elements():
    # show a &quot;console style&quot; progress bar  :)
    print(&quot;.&quot;, end=&quot;&quot;, flush=True)
print()
print(&quot;end&quot;)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:heading -->
<h2>Is the memory footprint of the function I’m writing relevant?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If the answer is “yes”, it’s probably a good idea to use a generator.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That’s because with a generator you create a result just when you need it and after the result has been created you can start working on it, removing it from the memory when you have finished and before asking for another item.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s say that your function is supposed to return a huge list of big objects, to return a single list you have to create that list and keep it all in memory.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import time

def get_elements():
    elements = []
    for i in range (0,10000):
        elements.append(&quot;x&quot;*10240)
    # return a list of 10.000 items, each of 10KB...
    return elements

characters_count = 0

my_elements=get_elements()
# in this moment, our program has a memory footprint of more than 100MB!!!

for i in my_elements:
    characters_count = characters_count + len(i)

print(characters_count)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>As you see, in this case, we are allocating more than 100MB RAM before actually doing anything… But using a generator…</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">def get_elements():
    for i in range (0,10000):
        yield(&quot;x&quot;*10240)

characters_count = 0

my_elements=get_elements()

for i in my_elements:
    characters_count = characters_count + len(i)

print(characters_count)
</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>we get the same result with just 10KB RAM used at a time.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>Now I can hear you wondering “well, I have to use generators if the function that creates an element is time-consuming, if the memory footprint of that function is relevant or if I don’t need all the elements of the list, but in every other case it’s ok to create a list, right?”… Well, it could be ok… but… even in this case, why not to use a generator? A generator, for me, is always a better choice and consider that if you have a generator, converting it in a list is a trivial operation that can be done by using the “list” keyword like that.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">mylist = list(my_generator())</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>or by using list comprehension syntax</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">mylist = [element for element in my_generator()]</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>To sum up: <strong>ask not</strong> “<em>why should I use a generator?</em>” but ask “<em>why shouldn’t I?</em>”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Happy Coding!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>D.</p>
<!-- /wp:paragraph -->