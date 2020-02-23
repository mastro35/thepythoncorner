---
title: Working with Exception in Python
date: 2017-01-10T19:02:01+01:00
author: Davide Mastromatteo
excerpt: "To know how exception works in Python is really important. Exceptions are not just used to control the program's errors but also to manage the program's flow and in this post, we will discuss this specific topic"
header:
  teaser: https://imgs.xkcd.com/comics/compiler_complaint.png
categories:
  - Dev
tags:
  - Error Handling
  - Exception
  - Featured
  - Programming
  - Python
redirect_from:
  /2017/01/working-with-exception-in-python
---
<!-- wp:paragraph -->
<p>According to the <a href="https://docs.python.org/3/tutorial/errors.html" target="_blank" rel="noopener noreferrer">official documentation</a>, an exception is “an error detected during execution not unconditionally fatal”. Let’s start the interpreter and write:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; 5/0
Traceback (most recent call last):
  File &quot;&lt;pyshell#7&gt;&quot;, line 1, in &lt;module&gt;
    5/0
ZeroDivisionError: division by zero</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>As you can see we asked the interpreter to divide the number 5 by 0. Even if our request was syntactically correct when the interpreter tried to compute it, it “raised” the <em>ZeroDivisionError</em> exception to signal us that we asked something impossible. There are a lot of built-in exceptions in the base library to handle a different kind of errors (system errors, value errors, I/O errors, Arithmetic errors etc…) and to know how to handle this kind of errors is very important for every Python developer.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Handling exception</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Handle an exception means to define what to do when a specific exception happens so that the execution can proceed smoothly.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The basic way to handle an exception is by using the <em>try</em> statement. Basically, we need to specify what we want to do, which kind of exceptions we do expect and what to do when one of these exceptions is raised.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To make an example, let’s say we want to open a file to read it and show its content. To accomplish this task we can write this script:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">f = open(&quot;myfile.txt&quot;)

for line in f:
    print(line)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>The problem is: what happens if the file <em>myfile.txt</em> does not exist? Let’s try…</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">Traceback (most recent call last):
  File &quot;exceptions.py&quot;, line 1, in &lt;module&gt;
    f = open(&quot;myfile.txt&quot;)
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Well, we get a <em>FileNotFoundException</em> and the execution stops. So, to handle this exception we could just modify the code as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">try:
    f = open(&quot;myfile.txt&quot;)
    
    for line in f:
        print(line)
    except FileNotFoundError:
        print(&quot;The file does not exist&quot;)
</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In this way, the interpreter tries to do what’s inside the <em>try</em> block and, if a <em>FileNotFoundError</em> exception is raised, instead of writing the exception’s detail on screen and exit, it just continues executing what’s inside the <em>except</em> block. If the file existed, the exception would not be raised and the except block would be skipped.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now, executing the script again, the result would be:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">The file does not exist</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>It’s worth to be noted that we can use more except clauses for a single try block. For example, the code could be modified as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">try:
    f = open(&quot;myfile.txt&quot;)
    for line in f:
        print(line)
except FileNotFoundError:
    print(&quot;The file does not exist&quot;)
except PermissionError:
    print(&quot;You don't have the permission to open the file&quot;)
except Exception:
    print(&quot;Unexpected error occured&quot;)
              </pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In the latest example, we are trapping the exception to handle the case when the file does not exist, the exception to handle the case when the file exists but the user does not have the permission to read from it and any other error that could happen at run time, catching the general <em>Exception&nbsp;</em>exception. This is made possible thanks to the fact that in Python, everything is an object, even the exceptions. This means that almost all the exceptions that can be fired at runtime are actually derived from the <em>Exception</em> exception.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here’s the complete hierarchy as it appears in the <a href="https://docs.python.org/3/library/exceptions.html" target="_blank" rel="noopener noreferrer">official docs</a>:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Finally, you can have the need to execute some code after the try block is executed, whether or not the code in the try block has raised exceptions. In this case, you can add a <em>finally</em> clause. For example:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">try:
    f = open(&quot;myfile.txt&quot;)
    for line in f:
        print(line)
except FileNotFoundError:
    print(&quot;The file does not exist&quot;)
except PermissionError:
    print(&quot;You don't have the permission to open the file&quot;)
except Exception:
    print(&quot;Unexpected error occured&quot;)
finally:
    print(&quot;The execution will now be terminated&quot;)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In this last example, whatever happens, the message “The execution will now be terminated” will be shown before leaving the try/except block.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Raising exception</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Now that we know what an exception is and how to handle exceptions, let’s see how is it possible to raise exceptions by ourselves. Look at this code:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">def get_numeric_value_from_keyboard():
    '''Get a value from keyboard, if the value is not a valid number, raise a &quot;ValueError&quot; exception'''
    input_value = input(&quot;Please, enter an integer: &quot;)
    if not input_value.isdigit():
        raise ValueError(&quot;The value inserted is not a number&quot;)

	return input_value

while True:
    try:
        numeric_value = get_numeric_value_from_keyboard()
        print(&quot;You have inserted the value &quot; + str(numeric_value))
        break
    except ValueError as ex:
        print(ex)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In this example, we have created a function that gets input from the user keyboard. If the input is numeric, it just returns the input to the caller, but if it’s not, it raises a “ValueError” exception. Note that in this example, we’re not just raising a <em>ValueError</em> exception but we are also specifying a custom message for the exception. In the except clause, we grab the exception, assign it to the <em>ex</em> variable and then we use the <em>ex</em> variable to print the message for the user.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Another possibility you have is to re-raise an exception once it gets caught in an except block. For example, try to modify the code as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">    def get_numeric_value_from_keyboard():
    '''Get a value from keyboard, if the value is not a valid number, raise a &quot;ValueError&quot; exception'''
    input_value = input(&quot;Please, enter an integer: &quot;)
    if not input_value.isdigit():
        raise ValueError(&quot;The value inserted is not a number&quot;)

    return input_value

while True:
    try:
        numeric_value = get_numeric_value_from_keyboard()
        print(&quot;You have inserted the value &quot; + str(numeric_value))
        break
    except ValueError as ex:
        print(&quot;Something strange happened...&quot;)
        raise</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now, if you run this code and insert a non-numeric value, the execution will be interrupted and you will get this message:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">Please, enter an integer: asd
Something strange happened...
Traceback (most recent call last):
  File &quot;exceptions.py&quot;, line 12, in &lt;module&gt;
    numeric_value = get_numeric_value_from_keyboard()
  File &quot;exceptions.py&quot;, line 5, in get_numeric_value_from_keyboard
    raise ValueError(&quot;The value inserted is not a number&quot;)
ValueError: The value inserted is not a number</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>As you can see, in the except block we’ve caught the <em>ValueError</em> exception, we’ve done something (we’ve printed the “Something strange happened…” message) and then we’ve re-raised the same exception we previously caught. Obviously, since there were no other code blocks to catch our exception, the program has exited and the exception has been shown to the console.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Define custom exception</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Knowing how to raise an exception is important especially if we want to build our custom exception. We’ve already said that there’s a hierarchy of exceptions, so to create our custom exception we just need to create a new class inheriting from the <em>Exception</em> class.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, let’s say that we are coding the software for an ATM, we could need a special “WithdrawLimitError” exception to be raised when the user asks for a too high sum of money. In this case, we can create our custom exception like this:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">class WithdrawLimitError(Exception):
    pass</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now, we can use it in our code just like any other exception.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>The bottom&nbsp;line</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>There are several programming languages where the developer is asked to use exception just to handle “errors” because the handling of an exception can lead to performance issues. Well, the Python approach is completely different. Python internals relies on exceptions (for example, in a simple "for" loop the StopIteration exception is used to signal that there are no further items to iterate) and is encouraged the use of an exception to indicate failures, even when they are expected on regular basis.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So for example, if you have to open a file don’t check whether it exists or not, just open it and handle the exception if something goes wrong. It makes the code more readable, <em>Pythonic</em>, and easier to be maintained.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Enjoy!</p>
<!-- /wp:paragraph -->