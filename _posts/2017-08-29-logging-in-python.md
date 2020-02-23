---
title: Logging in Python
date: 2017-08-29T13:02:52+02:00
author: Davide Mastromatteo
excerpt: "Do you always write log routines to make your program be verbose in the production environment? No? Well, you'd better have a look at this article."
header:
  teaser: https://imgs.xkcd.com/comics/git_commit.png
categories:
  - Dev
tags:
  - Featured
  - Logging
  - Python
redirect_from:
  /2017/08/logging-in-python
---
<!-- wp:paragraph -->
<p>One of the most underestimated topics that I’ve seen in my working experience is logs management. A lot of people don’t care at all about logging the execution of their programs and I’ve seen a lot of code released in the production environment that doesn’t log anything. To log seems to be a waste of time to them, especially if the code they’re writing is apparently simple. So, why bother logging the execution of a program if the program can run great with no logs?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Actually, logging the execution of your own program avoids you lots of headaches when something goes wrong in production and make your coding experience easier. Besides, logging a lot of debug information can save you time in writing comments, because your code is just well documented by the use of the logging, so to log is always a good idea in production as it is during the development, and that is true for any language you’re using to code, not just in Python.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But Python is not “any language”, Python is a great language that comes with “batteries included”, isn’t it?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In fact, although in other languages you need to write your own logging facility or to download some third-party libraries that solve this problem for you, in Python it just means to use the built-in logging module.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, what are we waiting for? Let’s start logging in Python!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The first thing that we have to bear in mind is that a log can contain a different kind of messages and each message has its own level of importance. These levels, in Python, are defined in order of verbosity (from the most verbose to the less verbose) as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>DEBUG: Detailed information, typically of interest only when diagnosing problems.</li><li>INFO: Confirmation that things are working as expected.</li><li>WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.</li><li>ERROR: Due to a more serious problem, the software has not been able to perform some function.</li><li>CRITICAL: A serious error, indicating that the program itself may be unable to continue running.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>So, each time we want to write something in our log we have to decide what kind of message we are writing to the log, and hence what level it should have.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The second thing that we have to know is how to configure a logger in Python. It’s really easy actually, we just need three components:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>a logger: the object that our code will use to log</li><li>at least one handler: the object that will handle the writing of our log to the target device</li><li>a formatter: an object that defines the format of our log for the handler</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Ok, too much talk, let’s start coding.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s start by importing the logging module:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import logging</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>then, let’s create the first object: the logger</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">logger=logging.getLogger(__name__)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>as you can see, to create a logger we just have to call the “getLogger” method of our logging module passing to it a name for the logger. Usually, it’s a good idea to use the <strong>name</strong> special variable to specify the name of the logger. Doing this you will have different loggers for different modules by design, and you will be able to configure differently every single logger.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now we have to specify the default log level of our logger. This configuration ensures you that just the log messages with this level or with a less verbose level will be recorded. This enables you to have a super detailed log with all the debug information when you are developing or testing your application and a less verbose log when you deploy your program to the production environment.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}"># define the default level of the logger. 
# We could specify a greater (LESS VERBOSE) level on the single handler 
logger.setLevel(logging.DEBUG)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now we have to create our second object: the formatter. As we said before, the formatter is the object that specifies the format we want for our log. In this example, I’m creating a formatter that will output every single message specifying its timestamp and its log level. There are plenty of variables you can use to configure the format of your log, to have a complete list check the <a href="https://docs.python.org/3/library/logging.html#logrecord-attributes" target="_blank" rel="noopener noreferrer">official documentation</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}"># creating a formatter. 
# to see all the attributes you can use
formatter=logging.Formatter('%(asctime)s | %(levelname)s -&gt; %(message)s')</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now we need to create the handler (or the handlers) that will take care of writing our logs to the target device. Usually I create a file handler to log on a file on the filesystem all the information with an INFO level or greater (it’s a must for the production environment) and a stream handler to log every single information also to the console (it’s quite convenient while I’m coding and prevent me to misuse the “print” function). Note that we can specify a different level for each handler unless it is greater or equal to the main level specified for the logger. Even the format can be different (we could need different information for the console and for the log file for example).</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}"># creating a handler to log on the filesystem
file_handler=logging.FileHandler('mylogfile.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# creating a handler to log on the console
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Ok, we have almost finished now, we just need to put everything together…</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}"># adding handlers to our logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>and that’s it! We have configured our logger. It wasn’t a pain, was it? Now, to log a message we will just need to call the “info”, “warning”, “error”, “debug”, or “critical” method passing the message we want to log as a parameter. For example:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">logger.info('this is a log message...')</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>and we'll get:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">2017-08-29 12:41:42,154 | INFO -&gt; this is a log message...</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now, if we were creating a program to divide two given numbers and log the result, we could have done something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">a=50
b=10

try:
    c=a/b
    logger.info(f&quot;Operation {a}/{b} gave the result {c}&quot;)
except:
    logger.error(f&quot;Error occured during the division of {a} and {b}&quot;)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>And the output would be:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">2017-08-29 12:41:42,204 | INFO -&gt; Operation 50/10 gave the result 5.0</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>It’s worth to be said that to log the exceptions there’s also an “exception” method of the logger that write a message with the “ERROR” level but add to it also some more information from the exception, like the stacktrace and the exception message. So for example, in this example it was far better to write something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">a=50
b=0

try:
    c=a/b
    logger.info(f&quot;Operation {a}/{b} gave the result {c}&quot;)
except:
    logger.error(f&quot;Error occured during the division of {a} and {b}&quot;)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>And the output would be:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">2017-08-29 12:41:42,242 | ERROR -&gt; Error occured during the division of 50 and 0
Traceback (most recent call last):
  File &quot;&lt;ipython-input-10-9b4751150eb5&gt;&quot;, line 5, in &lt;module&gt;
    c=a/b
ZeroDivisionError: division by zero</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>As always, for more information and for advanced topics I encourage you to check the <a href="https://docs.python.org/3/library/logging.html#module-logging" target="_blank" rel="noopener noreferrer">official documentation</a> and the <a href="https://www.python.org/dev/peps/pep-0282/" target="_blank" rel="noopener noreferrer">original PEP</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That’s all folks, happy coding and… happy logging!&nbsp;:)</p>
<!-- /wp:paragraph -->