---
title: Lambdas and functions in Python
date: 2017-12-13T19:06:00+01:00
author: Davide Mastromatteo
excerpt: "How lambdas can improve your code's readability and maintainability"
header:
  teaser: https://imgs.xkcd.com/comics/code_quality_2.png
categories:
  - Dev
tags:
  - Featured
  - First Class Objects
  - Lambda
  - Python
redirect_from:
  /2017/12/lambdas-and-functions-in-python
---
<!-- wp:paragraph -->
<p><a href="https://www.thepythoncorner.com/2018/05/the-art-of-avoiding-nested-code.html" target="_blank" rel="noopener noreferrer">In my last post</a>, I discussed some ways to avoid nested code in Python and discussing the ”<em>filter</em>” and ”<em>map</em>” functions I mentioned the <strong><em>lambda functions</em></strong>.<br>After that article, some reader asked me to write a little more about this topic, so&nbsp;… here I am.&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s start with a mantra. If you want to know what something is, in Python, just use your REPL.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, start the Python REPL and define a lambda:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">Python 3.6.2 |Anaconda custom (64-bit)| (default, Sep 19 2017, 08:03:39) [MSC v.1900 64 bit (AMD64)] on win32
Type “help”, “copyright”, “credits” or “license” for more information.

&gt;&gt;&gt; my_lambda = lambda x: x+1</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now, try to ask Python what is “my_lambda”</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; print(my_lambda)
&lt;function &lt;lambda&gt; at 0x0000021D14663E18&gt;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>It turns out that a "lambda" is… just a function!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Basically, a lambda is just an anonymous function that can be used “inline” whenever your code expects to find a function. In Python, in fact, functions are first-class objects and that basically means that they can be used like any other objects. They can be passed to other functions, they can be assigned to a name, they can be returned from a function and so on.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, in our first example, we just defined a function that takes an argument (x), sums the value 1 to the input argument, and returns the result of this operation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What’s the name of the function?<br>It has no name actually, and so I had to assign this anonymous function to the name “my_lambda” to be able to use it in my code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now I can hear some of you saying:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Why bother with this stuff?<br>Why not just use a standard named function?<br>Couldn’t I write something like this?</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; def my_sum_function(x):
… return x+1
…
&gt;&gt;&gt; print (my_sum_function)
&lt;function my_sum_function at 0x0000021D14D83E18&gt;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Yes, you could actually… and I will tell you something more: you can pass this function as well to other functions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In our example, if we use:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; print(list(map(my_lambda, range(10)))) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>we get the same results of writing:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; print(list(map(my_sum_function, range(10))))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>So, why bother with lambda functions?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well… it’s just a matter of style and readability, because as we will keep saying: readability counts (<a rel="noopener noreferrer" href="https://www.python.org/dev/peps/pep-0020/" target="_blank">“The Zen Of Python”, rule #7</a>).</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:heading {"level":3} -->
<h3>The case of the RPN Calculator</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let’s pretend that one of your customers asked you to create a program to simulate a “Reverse Polish Notation calculator” that they will install on all their employees’ computers. You accept this work and get the specs for the program:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The program should be able to do all the basic operations (divide, sum, subtract, multiply), to find the square root of a number and to power to 2 a number. Obviously, you should be able to clear all the stack of the calculator or just to drop the last inserted number.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p> <strong>RPN Calculator for newbies</strong></p><p><br> If you already know what is a RPN calculator, skip this part.<br> If you do not know what is the Reverse Polish Notation, but you are curious, just <a rel="noreferrer noopener" href="https://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">check this out</a>.<br> If you do not know anything about the Reverse Polish Notation and you want just a brief explanation to keep reading this article… go ahead.<br> The Reverse Polish Notation was very relevant in 70’s and 80’s as Hewlett-Packard used it in their scientific calculators and I personally love this notation.<br> Basically in a RPN calculator you have a “stack” where you put the operands with a LIFO (last in, first out) logic.<br> Then, when you press the button to compute an operation, the calculator takes out from the stack all the operands that the operation ask for, compute the operation and put the result back to the stack.<br> So, let’s do an example. You want the result of the operation 5 x 6. In a standard calc you would act this way:<br> - press 5<br>- press *<br>- press 6<br>- press =<br> and on the display you get the result : 30.<br> In a RPN calculator, you act this way:<br> - press 5<br>- press ENTER (and the number 5 is put on the stack)<br>- press 6<br>- press ENTER (and the number 6 is put on the stack)<br>- press *<br> Now, before pressing the ‘*’ symbol your stack was like this:<br> —<br>5<br>6<br>—<br> after pressing the ‘*’ symbol, you find on the stack just the result: 30. That’s because the calculator knows that for a multiplication you need two operands, so it has “popped” the first value (6 — remember, it’s a stack, it’s LIFO), then it has “popped” the second value (5), it has executed the operation and put back the result (30) on the stack.<br> RPN calculators are great since they do not need expressions to be parethesized and there’s more: they’re cool! :) </p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Now, you accepted the job and you have to start working, but since the deadline of the project is very tight, you decide to ask Max, your IT artist, of writing a GUI for the calculator and Peter, your new intern, of creating the “engine” of this calculator software.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s focus on Peter’s work.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Peter’s work</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>After a while, Peter comes proudly to you asserting he has finished coding the calculator engine.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And that’s what he has done so far:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python","lineNumbers":true} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:true,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;&quot;&quot;
Engine class of the RPN Calculator
&quot;&quot;&quot;

import math

class rpn_engine:
    def __init__(self):
        &quot;&quot;&quot; Constructor &quot;&quot;&quot;
        self.stack = []

    def push(self, number):
        &quot;&quot;&quot; push a value to the internal stack &quot;&quot;&quot;
        self.stack.append(number)

    def pop(self):
        &quot;&quot;&quot; pop a value from the stack &quot;&quot;&quot;
        try:
            return self.stack.pop()
        except IndexError:
            pass # do not notify any error if the stack is empty...

    def sum_two_numbers(self):
        op2 = self.stack.pop()
        op1 = self.stack.pop()
        self.push(op1 + op2)

    def subtract_two_numbers(self):
        op2 = self.stack.pop()
        op1 = self.stack.pop()
        self.push(op1 - op2)

    def multiply_two_numbers(self):
        op2 = self.stack.pop()
        op1 = self.stack.pop()
        self.push(op1 * op2)

    def divide_two_numbers(self):
        op2 = self.stack.pop()
        op1 = self.stack.pop()
        self.push(op1 / op2)

    def pow2_a_number(self):
        op1 = self.stack.pop()
        self.push(op1 * op1)

    def sqrt_a_number(self):
        op1 = self.stack.pop()
        self.push(math.sqrt(op1))


    def compute(self, operation):
        &quot;&quot;&quot; compute an operation &quot;&quot;&quot;

        if operation == '+':
            self.sum_two_numbers()

        if operation == '-':
            self.subtract_two_numbers()

        if operation == '*':
            self.multiply_two_numbers()

        if operation == '/':
            self.divide_two_numbers()

        if operation == '^2':
            self.pow2_a_number()

        if operation == 'SQRT':
            self.sqrt_a_number()

        if operation == 'C':
            self.stack.pop()

        if operation == 'AC':
            self.stack.clear()
</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In a moment he understands that you’re looking at him shocked and states: “<em>my code runs fine</em>”.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now, let’s clarify one thing: Peter’s right. His code runs (so does a burning bus… [cit]). Nevertheless, his code sucks. That’s it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So let’s have a look at how we can improve this “stuff”.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>The first problem here is the code duplication. There’s a principle of software engineering that is called “DRY”. It stands for “Don’t Repeat Yourself”.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Peter has duplicated a lot of code because for every single function he has to get the operands, compute the operation and put the result back to the stack. Wouldn’t it be great if we could have a function that does exactly this job, computing the operation we request? How can we achieve this?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well, it’s really simple actually, because as we said earlier… functions are first-class objects in Python! So, Peter’s code can be simplified a lot.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s have a look at the functions we have to provide.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>All the standard operations (divide, sum, add and multiply) needs two operands to be computed. The “sqrt” and the “pow2” functions need just one operand to be computed. The “C” (to drop the last item in the stack) and “AC” (to clear the stack) functions, don’t need any operand to be computed.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, let’s rewrite Peter’s code this way:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python","lineNumbers":true} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:true,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;&quot;&quot;
Engine class of the RPN Calculator
&quot;&quot;&quot;

import math

class rpn_engine:
    def __init__(self):
        &quot;&quot;&quot; Constructor &quot;&quot;&quot;
        self.stack = []

    def push(self, number):
        &quot;&quot;&quot; push a value to the internal stack &quot;&quot;&quot;
        self.stack.append(number)

    def pop(self):
        &quot;&quot;&quot; pop a value from the stack &quot;&quot;&quot;
        try:
            return self.stack.pop()
        except IndexError:
            pass # do not notify any error if the stack is empty...

    def sum_two_numbers(self, op1, op2):
        return op1 + op2

    def subtract_two_numbers(self, op1, op2):
        return op1 - op2

    def multiply_two_numbers(self, op1, op2):
        return op1 * op2

    def divide_two_numbers(self, op1, op2):
        return op1 / op2

    def pow2_a_number(self, op1):
        return op1 * op1

    def sqrt_a_number(self, op1):
        return math.sqrt(op1)


    def compute(self, operation):
        &quot;&quot;&quot; compute an operation &quot;&quot;&quot;

        if operation == '+':
            self.compute_operation_with_two_operands(self.sum_two_numbers)

        if operation == '-':
            self.compute_operation_with_two_operands(self.subtract_two_numbers)

        if operation == '*':
            self.compute_operation_with_two_operands(self.multiply_two_numbers)

        if operation == '/':
            self.compute_operation_with_two_operands(self.divide_two_numbers)

        if operation == '^2':
            self.compute_operation_with_one_operand(self.pow2_a_number)

        if operation == 'SQRT':
            self.compute_operation_with_one_operand(self.sqrt_a_number)

        if operation == 'C':
            self.stack.pop()

        if operation == 'AC':
            self.stack.clear()

    def compute_operation_with_two_operands(self, operation):
        &quot;&quot;&quot; exec operations with two operands &quot;&quot;&quot;
        try:
            if len(self.stack) &lt; 2:
                raise BaseException(&quot;Not enough operands on the stack&quot;)

            op2 = self.stack.pop()
            op1 = self.stack.pop()
            result = operation(op1, op2)
            self.push(result)
        except BaseException as error:
            print(error)

    def compute_operation_with_one_operand(self, operation):
        &quot;&quot;&quot; exec operations with one operand &quot;&quot;&quot;
        try:
            op1 = self.stack.pop()
            result = operation(op1)
            self.push(result)
        except BaseException as error:
            print(error)
            </pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Isn’t it better? The duplicated code is far less than before and looks at the functions, all they do is to compute the operation and return the results. They are no longer in charge of getting operands and pushing the result to the stack, the readability of the code is definitely improved!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now, looking at the code, the first thing I really hate is all the “ifs” in the compute function. Perhaps replacing them with a “switch” function… if only the switch function would exist in Python!&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But we can do something better. Why don’t we create a <em>catalog</em> of the available functions and then we just use this catalog to decide which function to use?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Why don’t we use a <em>dictionary</em> for that?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s try to modify our code again:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python","lineNumbers":true} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:true,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;&quot;&quot;
Engine class of the RPN Calculator
&quot;&quot;&quot;

import math

class rpn_engine:
    def __init__(self):
        &quot;&quot;&quot; Constructor &quot;&quot;&quot;
        self.stack = []
        self.catalog = self.get_functions_catalog()

    def get_functions_catalog(self):
        return {&quot;+&quot;: self.sum_two_numbers, 
                &quot;-&quot;: self.subtract_two_numbers, 
                &quot;*&quot;: self.multiply_two_numbers,
                &quot;/&quot;: self.divide_two_numbers,
                &quot;^2&quot;: self.pow2_a_number,
                &quot;SQRT&quot;: self.sqrt_a_number,
                &quot;C&quot;: self.stack.pop,
                &quot;AC&quot;: self.stack.clear}

    def push(self, number):
        &quot;&quot;&quot; push a value to the internal stack &quot;&quot;&quot;
        self.stack.append(number)

    def pop(self):
        &quot;&quot;&quot; pop a value from the stack &quot;&quot;&quot;
        try:
            return self.stack.pop()
        except IndexError:
            pass # do not notify any error if the stack is empty...

    def sum_two_numbers(self, op1, op2):
        return op1 + op2

    def subtract_two_numbers(self, op1, op2):
        return op1 - op2

    def multiply_two_numbers(self, op1, op2):
        return op1 * op2

    def divide_two_numbers(self, op1, op2):
        return op1 / op2

    def pow2_a_number(self, op1):
        return op1 * op1

    def sqrt_a_number(self, op1):
        return math.sqrt(op1)


    def compute(self, operation):
        &quot;&quot;&quot; compute an operation &quot;&quot;&quot;

        if operation in ['+', '-', '*', '/']:
            self.compute_operation_with_two_operands(self.catalog[operation])

        if operation in ['^2', 'SQRT']:
            self.compute_operation_with_one_operand(self.catalog[operation])

        if operation in ['C', 'AC']:
            self.compute_operation_with_no_operands(self.catalog[operation])

    def compute_operation_with_two_operands(self, operation):
        &quot;&quot;&quot; exec operations with two operands &quot;&quot;&quot;
        try:
            if len(self.stack) &lt; 2:
                raise BaseException(&quot;Not enough operands on the stack&quot;)

            op2 = self.stack.pop()
            op1 = self.stack.pop()
            result = operation(op1, op2)
            self.push(result)
        except BaseException as error:
            print(error)

    def compute_operation_with_one_operand(self, operation):
        &quot;&quot;&quot; exec operations with one operand &quot;&quot;&quot;
        try:
            op1 = self.stack.pop()
            result = operation(op1)
            self.push(result)
        except BaseException as error:
            print(error)

    def compute_operation_with_no_operands(self, operation):
        &quot;&quot;&quot; exec operations with no operands &quot;&quot;&quot;
        try:
            operation()
        except BaseException as error:
            print(error)
</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Wow, almost all our “<em>if(s)</em>” are gone! And now we have a catalog of functions that we can expand as we want. So for example, if we need to implement a factorial function, we will just add the function to the catalog and implement a custom method in the code. That’s really good!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Even if&nbsp;…</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It would be great to act only on the catalog, wouldn’t it?<br>But wait… shouldn’t we talk about lambdas in this article?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here’s where lambdas can be useful! We don’t need a standard defined function for a simple calc, we need just an inline lambda for that!</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python","lineNumbers":true} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:true,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;&quot;&quot;
Engine class of the RPN Calculator
&quot;&quot;&quot;

import math

class rpn_engine:
    def __init__(self):
        &quot;&quot;&quot; Constructor &quot;&quot;&quot;
        self.stack = []
        self.catalog = self.get_functions_catalog()

    def get_functions_catalog(self):
        return {&quot;+&quot;: lambda x, y: x + y,
                &quot;-&quot;: lambda x, y: x - y,
                &quot;*&quot;: lambda x, y: x * y,
                &quot;/&quot;: lambda x, y: x / y,
                &quot;^2&quot;: lambda x: x * x,
                &quot;SQRT&quot;: lambda x: math.sqrt(x),
                &quot;C&quot;: self.stack.pop,
                &quot;AC&quot;: self.stack.clear}

    def push(self, number):
        &quot;&quot;&quot; push a value to the internal stack &quot;&quot;&quot;
        self.stack.append(number)

    def pop(self):
        &quot;&quot;&quot; pop a value from the stack &quot;&quot;&quot;
        try:
            return self.stack.pop()
        except IndexError:
            pass # do not notify any error if the stack is empty...

    def compute(self, operation):
        &quot;&quot;&quot; compute an operation &quot;&quot;&quot;

        if operation in ['+', '-', '*', '/']:
            self.compute_operation_with_two_operands(self.catalog[operation])

        if operation in ['^2', 'SQRT']:
            self.compute_operation_with_one_operand(self.catalog[operation])

        if operation in ['C', 'AC']:
            self.compute_operation_with_no_operands(self.catalog[operation])

    def compute_operation_with_two_operands(self, operation):
        &quot;&quot;&quot; exec operations with two operands &quot;&quot;&quot;
        try:
            if len(self.stack) &lt; 2:
                raise BaseException(&quot;Not enough operands on the stack&quot;)

            op2 = self.stack.pop()
            op1 = self.stack.pop()
            result = operation(op1, op2)
            self.push(result)
        except BaseException as error:
            print(error)

    def compute_operation_with_one_operand(self, operation):
        &quot;&quot;&quot; exec operations with one operand &quot;&quot;&quot;
        try:
            op1 = self.stack.pop()
            result = operation(op1)
            self.push(result)
        except BaseException as error:
            print(error)

    def compute_operation_with_no_operands(self, operation):
        &quot;&quot;&quot; exec operations with no operands &quot;&quot;&quot;
        try:
            operation()
        except BaseException as error:
            print(error)
</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>So, our code could be:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Wow, this code rocks now!&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Even if…</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s pretend that we have to add the factorial function, could we just modify the catalog?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Unfortunately no.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There’s another place we have to modify… we have to modify also the compute function because we need to specify that the factorial function is a “one operand function”.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That’s bad, we do know that it is a one operand function, it’s obvious since we need to call the math.factorial(x) function passing just the x argument. If only there were a way to determine how many arguments a function needs at runtime…</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There is actually. In the “inspect” module, there’s a “signature” function that can help us inspect the signature of our method at runtime. So, let’s start the REPL and do a quick test:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; a = lambda x, y: x + y
&gt;&gt;&gt; from inspect import signature
&gt;&gt;&gt; my_signature = signature(a)
&gt;&gt;&gt; print(my_signature)
(x, y)
&gt;&gt;&gt; print (my_signature.parameters)
OrderedDict([(‘x’, &lt;Parameter “x”&gt;), (‘y’, &lt;Parameter “y”&gt;)])
&gt;&gt;&gt; print (len(my_signature.parameters))
2</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Yes, amazing. We could determine at runtime how many operands our function needs!</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python","lineNumbers":true} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:true,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;&quot;&quot;
Engine class of the RPN Calculator
&quot;&quot;&quot;

import math
from inspect import signature

class rpn_engine:
    def __init__(self):
        &quot;&quot;&quot; Constructor &quot;&quot;&quot;
        self.stack = []
        self.catalog = self.get_functions_catalog()

    def get_functions_catalog(self):
        &quot;&quot;&quot; Returns the catalog of all the functions supported by the calculator &quot;&quot;&quot;
        return {&quot;+&quot;: lambda x, y: x + y,
                &quot;-&quot;: lambda x, y: x - y,
                &quot;*&quot;: lambda x, y: x * y,
                &quot;/&quot;: lambda x, y: x / y,
                &quot;^2&quot;: lambda x: x * x,
                &quot;SQRT&quot;: lambda x: math.sqrt(x),
                &quot;C&quot;: lambda: self.stack.pop(),
                &quot;AC&quot;: lambda: self.stack.clear()}

    def push(self, number):
        &quot;&quot;&quot; push a value to the internal stack &quot;&quot;&quot;
        self.stack.append(number)

    def pop(self):
        &quot;&quot;&quot; pop a value from the stack &quot;&quot;&quot;
        try:
            return self.stack.pop()
        except IndexError:
            pass # do not notify any error if the stack is empty...

    def compute(self, operation):
        &quot;&quot;&quot; compute an operation &quot;&quot;&quot;

        function_requested = self.catalog[operation]
        number_of_operands = 0
        function_signature = signature(function_requested)
        number_of_operands = len(function_signature.parameters)

        if number_of_operands == 2:
            self.compute_operation_with_two_operands(self.catalog[operation])

        if number_of_operands == 1:
            self.compute_operation_with_one_operand(self.catalog[operation])

        if number_of_operands == 0:
            self.compute_operation_with_no_operands(self.catalog[operation])

    def compute_operation_with_two_operands(self, operation):
        &quot;&quot;&quot; exec operations with two operands &quot;&quot;&quot;
        try:
            if len(self.stack) &lt; 2:
                raise BaseException(&quot;Not enough operands on the stack&quot;)

            op2 = self.stack.pop()
            op1 = self.stack.pop()
            result = operation(op1, op2)
            self.push(result)
        except BaseException as error:
            print(error)

    def compute_operation_with_one_operand(self, operation):
        &quot;&quot;&quot; exec operations with one operand &quot;&quot;&quot;
        try:
            op1 = self.stack.pop()
            result = operation(op1)
            self.push(result)
        except BaseException as error:
            print(error)

    def compute_operation_with_no_operands(self, operation):
        &quot;&quot;&quot; exec operations with no operands &quot;&quot;&quot;
        try:
            operation()
        except BaseException as error:
            print(error)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Let’s try it now:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As someone said, “<a href="https://it.wikiquote.org/wiki/Neil_Armstrong" target="_blank" rel="noopener noreferrer">That’s one small step for [a] man, one giant leap for mankind</a>.”&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Note that in this last code we have modified the zero operands functions in the catalog from</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;C&quot;: self.stack.pop,
&quot;AC&quot;: self.stack.clear</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>to</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;C&quot;: lambda: self.stack.pop(),
&quot;AC&quot;: lambda: self.stack.clear()}</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Why that?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well, the problem is that in the <em>compute </em>function we are trying to determine the number of parameters from the signature of the method. The problem is that for built-in methods written in C, we can’t do that.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s try it by yourself, start a REPL&nbsp;:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; from inpect import signature
&gt;&gt;&gt; a = []
&gt;&gt;&gt; my_sig = signature(a.clear)
Traceback (most recent call last):
 File “&lt;stdin&gt;”, line 1, in &lt;module&gt;
 File “C:UsersMASTROMATTEOAppDataLocalContinuumanaconda3libinspect.py”, line 3033, in signature
 return Signature.from_callable(obj, follow_wrapped=follow_wrapped)
 File “C:UsersMASTROMATTEOAppDataLocalContinuumanaconda3libinspect.py”, line 2783, in from_callable
 follow_wrapper_chains=follow_wrapped)
 File “C:UsersMASTROMATTEOAppDataLocalContinuumanaconda3libinspect.py”, line 2262, in _signature_from_callable
 skip_bound_arg=skip_bound_arg)
 File “C:UsersMASTROMATTEOAppDataLocalContinuumanaconda3libinspect.py”, line 2087, in _signature_from_builtin
 raise ValueError(“no signature found for builtin {!r}”.format(func))
ValueError: no signature found for builtin &lt;built-in method clear of list object at 0x000001ED6EB18F88&gt;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>as you can see we can’t get the signature of a built-in method.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our possibilities to solve this problem were:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Handle this special case in our code, trapping the exception raised when we tried to get the signature for the self.stack.pop() function and the self.stack.clear() function </li><li> Encapsulate the built-in functions in void lambdas, so as to have the signature functions extract the signature from our void lambda function and not from the built-in function contained. </li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>And we have obviously chosen the second possibility since it is the most “Pythonic” we had.&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That’s all folks. Today’s article has explored some aspect of functions and lambdas in Python and I hope you got the message I wanted to send.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>think twice, code&nbsp;once.</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Sometimes developers are lazy and don’t think too much at what can mean maintain bad code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s have a look at the first Peter’s code of the article and try to figure out what could have meant to add the factorial function then. We should have created another function, duplicated more code, and modified the "compute" function, right? With our last code we just need to add a single line to our catalog:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&quot;!&quot;: lambda x: math.factorial(x),</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Try to think at what could have meant to add another feature to the program for logging all the calculations requested and the given results. We had been supposed to modify a dozen functions of our code to add the feature right? And we would have had to modify as well all the new functions that we will have inserted from now on. Now we can add the feature just in the three methods that really compute the requested calculation depending on the number of the operands requested.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Wait, three methods? Wouldn’t it be possible to have just a method that works regardless of the number of operands that are requested by the function?&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Happy coding!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>D.</p>
<!-- /wp:paragraph -->