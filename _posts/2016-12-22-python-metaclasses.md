---
title: Python Metaclasses
date: 2016-12-22T12:31:01+01:00
author: Davide Mastromatteo
excerpt: |
  “Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don’t". That's what Tim Peters once said. But aren't you curious to know something about them? :)
header:
  teaser: https://imgs.xkcd.com/comics/code_quality.png
categories:
  - Dev
tags:
  - Abstract Base Classes
  - Featured
  - Metaclasses
  - Programming
  - Python
redirect_from:
  /2016/12/python-metaclasses
---
<!-- wp:paragraph -->
<p>Working with Python means working with objects because, in Python, <strong>everything</strong> is an object. So, for example:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; type(1)
&lt;class 'int'&gt;
&gt;&gt;&gt; type('x')
&lt;class 'str'&gt;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>As you can see, even basic types like integer and strings are objects, in particular, they are respectively instances of <em>int</em> and <em>str</em> classes. So, since everything is an object and given that an <em>object</em> is an instance of a <em>class</em>… what is a class?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let’s check it:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; type(int)
&lt;class 'type'&gt;
&gt;&gt;&gt; type(str)
&lt;class 'type'&gt;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>It turns out that classes are an object too, specifically they are instances of the “type” class, or better, they are instances of the “type” <em>metaclass</em>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A metaclass is <em>the class of a class</em> and the use of metaclasses could be convenient for some specific tasks like logging, profiling and more.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, let’s start demonstrating that a class is just an instance of a metaclass. We’ve said that <em>type</em> is the base metaclass and instantiating this metaclass we can create some class so… let’s try it:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">&gt;&gt;&gt; my_class = type(&quot;Foo&quot;, (), {&quot;bar&quot;: 1})
&gt;&gt;&gt; print(my_class)
&lt;class '__main__.Foo'&gt;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Here you can see that we have created a class named “Foo” just instantiating the metaclass <em>type</em>. The parameters we have passed are:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>The class name (Foo)</li><li>A tuple with the class superclasses (in this example we are creating a class without specifying any superclass)</li><li>A dictionary of attributes for the class (in this example we are creating the attribute “bar” with an int value of 1)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If everything is clear so far, we can try to create and use a custom metaclass. To define a custom metaclass it’s enough to subclass the type class.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Look at this example:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">class Logging_Meta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        print(str.format(&quot;Allocating memory space for class {0} &quot;, cls))
        return super().__new__(cls, name, bases, attrs, **kwargs)

    def __init__(self, name, bases, attrs, **kwargs):
        print(str.format(&quot;Initializing object {0}&quot;, self))
        return super().__init__(name, bases, attrs)

class foo(metaclass=Logging_Meta):
    pass

foo_instance = foo()
print(foo_instance)
print(type(foo))</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>on my PC, this code returns:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"shell","mime":"text/x-sh"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;shell&quot;,&quot;mime&quot;:&quot;text/x-sh&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">Allocating memory space for class &lt;class '__main__.Logging_Meta'&gt;
Initializing object &lt;class '__main__.foo'&gt;
&lt;__main__.foo object at 0x000000B54ACC0B00&gt;
&lt;class '__main__.Logging_Meta'&gt;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In this example we have defined a metaclass called <em>Logging_Meta</em> and using the magic methods <em>__new__</em> and <em>__init__</em> we have redefined the behavior of the class when the object is created and initialized. Then, we’ve declared a foo class specifying which is the metaclass to use for this class and as you can see, our class behavior is changed according to the <em>Logging_Meta</em> metaclass implementation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>A concrete use-case: Abstract Base classes&nbsp;(ABC’s)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A concrete use of metaclasses is the <em>abc</em> module. The <em>abc</em> module is a module of the standard library that provides the infrastructure for defining an abstract base class. Using abc you can check that a derived class that inherits from an abstract base class implements all the abstract methods of the superclass <strong>when the class is instantiated</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">from abc import ABCMeta, abstractmethod

class my_base_class(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

class my_derived_class(my_base_class):
    pass

a_class = my_derived_class()</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>If you try this example, you will see that the last line (the one that tries to instantiate the derived class) will raise<br>
the following exception:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">TypeError: Can't instantiate abstract class my_derived_class with abstract methods foo</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>That’s because <em>my_derived_class</em> does not implement the method foo as requested from the abstract base class.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It’s worth to be said that if you subclass a base class that uses a specific metaclass, your new object will use the metaclass as well. In fact, since Python 3.4 the module abc now provide also the ABC class that is just a generic class that uses the ABCMeta metaclasses. This means that the last example can be rewritten as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">from abc import ABC

class my_base_class(ABC):
    @abstractmethod
    def foo(self):
        pass

class my_derived_class(my_base_class):
    pass

a_class = my_derived_class()</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>This was just a brief introduction to metaclasses in Python. It’s more or less what <em>I</em> think should be known about this topic because it could lead to a better understanding of some internals of Python.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But let’s be clear: this is not something that every single Python user needs to know in order to start working in Python. As the "Python Guru" Tim Peters once said:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><em>“Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don’t (the people who actually need them know with certainty that they need them, and don’t need an explanation about why).” — Tim Peters</em></p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Enjoy!</p>
<!-- /wp:paragraph -->