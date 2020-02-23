---
title: The art of avoiding nested code
date: 2017-12-04T23:34:42+01:00
author: Davide Mastromatteo
excerpt: |
  The fifth statement of Tim Peter's "Zen of Python" is: "Flat is better than nested". So, let's explore some tips to make our code flatter and avoid nested code in Python! :)
header:
  teaser: https://imgs.xkcd.com/comics/flatland.png
categories:
  - Dev
tags:
  - Featured
  - Functools
  - List Comprehension
  - Maps
  - Python
redirect_from:
  /2017/12/the-art-of-avoiding-nested-code
---
<!-- wp:paragraph -->
<p>Today’s article is about nested code and how to avoid it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Why we should try to avoid nested code? Well the answer is inside your heart, and in your Python interpreter…</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Start your REPL and write:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import this</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>you will get the “Zen Of Python” by Tim Peters.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one — and preferably only one — obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let’s do more of those!</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now relax, breath, and read carefully all the statements, three times each.<br>Stop at the fifth statement and start meditating about that.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><em>Flat is better than nested<br>Flat is better than nested<br>Flat is better than nested</em></p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Do you get it?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>FLAT IS BETTER THAN NESTED!!</em></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, let’s start making your program "<em>flatter</em>"! :)</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2>Tip #1 — List Comprehension</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Raise your hand if you have ever written code like this:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">my_input_numbers = [1,2,3,4,5,6,7,8]
my_odd_numbers = []

for number in my_input_numbers:
    if number % 2 != 0:
        my_odd_numbers.append(number)

print(my_odd_numbers)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Come on, don’t be shy! Raise your hand!<br>Ok, are you looking at this article with a hand raised?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>SHAME ON YOU!</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>you probably don’t know anything about “<em>List Comprehension</em>”, do you?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>List comprehension is a (great) way of defining a list in Python, just like you’d do in math. For example, by using list comprehension the previous code could be rewritten like this:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">my_input_numbers = [1,2,3,4,5,6,7,8]
my_odd_numbers = [x for x in my_input_numbers if x%2 != 0]
print (my_odd_numbers)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Pretty cool uh? And it’s definitely flatter!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But list comprehension makes possible to do something more than just filter out even numbers from a list, for example, we can also manipulate the elements of the list:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">my_squared_odd_numbers = [x*x for x in my_input_numbers if x%2 != 0]</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Or again, let’s say that you want to create a list of tuples where you will put<br>all the combinations of the (integer) numbers between 1 and 90 taken 2 at a time (quite common if you play the Italian lottery), how can you do this?</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">ambi = [(x, y) for x in range(1,91) for y in range(x+1,91)]</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Yes, that’s so easy!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>One line of code instead of two-nested-for-loops, that’s it.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2>Tip #2 — Map, Filter and&nbsp;Reduce</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you have liked list comprehension you will probably like also the three functions we’re going to discuss here.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3><strong>The map&nbsp;function</strong></h3>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><code><strong>map</strong></code>(<em>function</em>, <em>iterable</em>, <em>...</em>)</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>The “<em>map</em>” function lets you execute a function on all the items of an iterable and returns an iterator with the result of this operation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, let’s write this one:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">my_numbers = [1,2,3,4,5,6,7,8,9,10]
my_squared_numbers = map(lambda x:x*x, my_numbers)
print(list(my_squared_numbers))</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>and we will have as a result</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Ok, ok, I know that some of you are now thinking “why don’t you use list comprehension to make that?”<br>Yes, it’s true, I could have written something like this</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">my_squared_numbers = [x*x for x in my_numbers]
print(my_squared_numbers)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>but it’s not the same. Look carefully to the two examples again…</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Did you get that?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In the former example, after we used the <em>map </em>function we had to use the “list” class to print out the results. That’s because “<em>map”</em> returns an iterator, not a real list.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you are wondering what are iterators, go and check my <a href="https://medium.com/the-python-corner/iterators-and-generators-in-python-2c3929a144b" target="_blank" rel="noopener noreferrer">previous article about the topic</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>The filter&nbsp;function</h3>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><code><strong>filter</strong></code>(<em>function</em>, <em>iterable</em>)</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>The “<em>filter</em>” function lets you filter out a list for certain values that meets a certain condition. Just like the the “<em>map</em>” function, the filter one return an iterator object with the results.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, for example:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">my_numbers = [1,2,3,4,5,6,7,8,9,10]
my_odd_numbers = filter(lambda x: x%2!=0, my_numbers)
print(list(my_odd_numbers))</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Like before, if you don’t need an iterable or if you do need a list, you can achieve the same result with list comprehension.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>The reduce&nbsp;function</h3>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><code>functools.<strong>reduce</strong></code>(<em>function</em>, <em>iterable</em>[, <em>initializer</em>])</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>The “<em>reduce</em>” is the last function we are going to discuss today. It lets you take an iterable and… reduce it literally to a single element by applying a function of two arguments cumulatively to the items of the iterable input. For example:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import functools
my_numbers = [1,2,3,4,5,6,7,8,9,10]
my_sum = functools.reduce(lambda x,y : x+y, my_numbers)
print(my_sum)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>And the result will be 55!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That’s great, isn’t it?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As you can see we had to import the functools library to use the reduce function because since the release of Python 3 this function is no more a built-in standard function and it’s now part of the functools library.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2>Tip #3 — Ternary conditional operator</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you are used to languages like Swift or C# you have probabilly seen the ternary conditional operator before.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, in Swift you can write something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"swift","mime":"text/x-swift"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;swift&quot;,&quot;mime&quot;:&quot;text/x-swift&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">let x = 5
// let's get x*x only if x is an odd number...
let squared_if_odd = x%2 == 0 ? x : x*x</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>this operator is very handy because it avoids you to write code like this:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mime":"text/x-swift"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/x-swift&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">let x = 5
var squared_if_odd = x

if x%2 != 0 {
    squared_if_odd = x*x
}</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>This handy ternary conditional operator is available also in Python, even if the syntax it a little different from what we could expect:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">x=5
squared_if_odd = x if x%2==0 else x*x</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Really convenient and definitely flat!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That’s all folks, go back to your code and start using these techniques; your code will be far more readable from now on.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>All the best<br>Dave</p>
<!-- /wp:paragraph -->