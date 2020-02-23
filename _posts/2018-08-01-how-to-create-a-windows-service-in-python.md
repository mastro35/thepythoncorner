---
title: How to create a Windows Service in Python
date: 2018-08-01T19:36:01+02:00
author: Davide Mastromatteo
excerpt: Can we create a Python Windows service that starts at boot and can be controlled like any other standard Windows service? Yes, we can.
header:
  teaser: https://imgs.xkcd.com/comics/backslashes.png
categories:
  - Dev
tags:
  - Background
  - Background Task
  - Python
  - Services
  - Windows
redirect_from:
  /2018/08/how-to-create-a-windows-service-in-python
---
<!-- wp:paragraph -->
<p>Hi guys, today’s post is just for the ones of you that work with the “OS of the misoriented slashes”: Microsoft Windows.&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Have you ever had the need of writing a Python script that could run in background as a Windows Service? In this post, you will learn how to do it in less than 10 minutes, no jokes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I will skip all the introduction about Windows Services, how convenient they could be, how much could be appreciated the fact that they can be run in background even when the user is logged off etc… I mean, if you can code in Python and you use Windows I bet you already know what a Windows Service is, don’t you?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, first of all, let’s start by installing the Python for Windows extensions:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">c:test&gt; pip install pywin32</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Once you have done it, let’s write this base class, your Windows service will be a subclass of this base class.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python","lineNumbers":true} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:true,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">'''
SMWinservice
by Davide Mastromatteo

Base class to create winservice in Python
-----------------------------------------

Instructions:

1. Just create a new class that inherits from this base class
2. Define into the new class the variables
   _svc_name_ = &quot;nameOfWinservice&quot;
   _svc_display_name_ = &quot;name of the Winservice that will be displayed in scm&quot;
   _svc_description_ = &quot;description of the Winservice that will be displayed in scm&quot;
3. Override the three main methods:
    def start(self) : if you need to do something at the service initialization.
                      A good idea is to put here the inizialization of the running condition
    def stop(self)  : if you need to do something just before the service is stopped.
                      A good idea is to put here the invalidation of the running condition
    def main(self)  : your actual run loop. Just create a loop based on your running condition
4. Define the entry point of your module calling the method &quot;parse_command_line&quot; of the new class
5. Enjoy
'''

import socket

import win32serviceutil

import servicemanager
import win32event
import win32service


class SMWinservice(win32serviceutil.ServiceFramework):
    '''Base class to create winservice in Python'''

    _svc_name_ = 'pythonService'
    _svc_display_name_ = 'Python Service'
    _svc_description_ = 'Python Service Description'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Constructor of the winservice
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        '''
        Override to add logic before the start
        eg. running condition
        '''
        pass

    def stop(self):
        '''
        Override to add logic before the stop
        eg. invalidating running condition
        '''
        pass

    def main(self):
        '''
        Main class to be ovverridden to add logic
        '''
        pass

# entry point of the module: copy and paste into the new module
# ensuring you are calling the &quot;parse_command_line&quot; of the new created class
if __name__ == '__main__':
    SMWinservice.parse_command_line()
</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Let's examine the class we have just introduced a little.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>def SvcDoRun(self)</em></strong>: it’s the method that will be called when the service is requested to start.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>def SvcStop(self)</em></strong>: it’s the method that will be called when the service is requested to stop.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>def start(self):</em> </strong>it’s a method that you will be asked to override if you need to do something when the service is starting (before started)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>def stop(self)</em></strong>: it’s the method that you will be asked to override if you need to do something when the service is stopping (before stopped)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>def main(self)</em></strong>: it’s the method that will contain the logic of your script, usually in a loop that keeps it alive until the service is stopped.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>def parse_command_line(cls)</em></strong>: it’s the method that handles the command line interface that you can use to install and update your windows service</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Can you see how easy it is with pywin32 to interface with the system to create a Windows Service? The last mention is for the following variables:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">svc_name = &quot;PythonCornerExample&quot;
svc_display_name = &quot;Python Corner’s Winservice Example&quot;
svc_description = &quot;That’s a great winservice! :)&quot;</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>These are just three variables that contain the name of the service, the “friendly name” that will be used by Windows to display the name on the mmc console and a short description of your service.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As always, enough talk, let’s code something useful!</p>
<!-- /wp:paragraph -->

<!-- wp:separator {"className":"is-style-dots"} -->
<hr class="wp-block-separator is-style-dots"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>Let’s pretend that we want to create a Winservice that, when started, creates a random file on our C: drive every 5 seconds.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What? Do you think it is stupid? Well, install it on your boss PC, set the destination folder as its user’s desktop and you will change your mind.&nbsp;:)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>However, how can you achieve this result? Super easy.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Subclass the SMWinservice class we have just met.</li><li>On the new class, override the three variables <em>_svc_name_</em>, <em>_svc_display_name_</em> and <em>_svc_description_</em>.</li><li>Override the “<strong><em>start</em></strong>” method to set the running condition. Setting a boolean variable will be enough for that.</li><li>Override the “<strong><em>stop</em></strong>” method to invalidate the running condition when the service is requested to be stopped.</li><li>Override the “<strong><em>main</em></strong>” method to add the logic of creating a random file every 5 seconds</li><li>Add the call at the “<strong><em>parse_command_line</em></strong>” function to handle the command line interface.</li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The result should be something like this: </p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python","lineNumbers":true} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:true,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import time
import random
from pathlib import Path
from SMWinservice import SMWinservice

class PythonCornerExample(SMWinservice):
    _svc_name_ = &quot;PythonCornerExample&quot;
    _svc_display_name_ = &quot;Python Corner's Winservice Example&quot;
    _svc_description_ = &quot;That's a great winservice! :)&quot;

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:{x}.txt').touch()
            time.sleep(5)

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>That’s it! Now it’s time to install our newly created winservice. Just open a command prompt, navigate to your script directory and install the service with the command:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">C:test&gt; python PythonCornerExample.py install
Installing service PythonCornerExample
Service installed</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>In the future, if you want to change the code of your service, just modify it and reinstall the service with</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">C:test&gt; python PythonCornerExample.py update
Changing service configuration
Service updated</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Now, open the “Services” msc snap in</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">C:test&gt; mmc Services.msc</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>locate your new <em><em>PythonCornerExample</em></em> winservice, and right click and choose properties. Here you can start your service and configure it at your will.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now try to start your service and go to see your C: folder contents.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Can you see all these files being created to your C: folder? Yeah, that’s working!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But now it’s time to stop it! :) You can do it from the previous windows or just by using the command line</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">C:test&gt; net stop PythonCornerExample 
Il servizio Python Corner’s Winservice Example sta per essere arrestato.. 
Servizio Python Corner’s Winservice Example arrestato.</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:heading -->
<h2>If something goes&nbsp;wrong…</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>There are a couple of known problems that can happen writing Windows Services in Python. If you have successfully installed the service but starting it you get an error, follow this iter to troubleshoot your service:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Check if Python is in your PATH variable. It MUST be there. To check this, just open a command prompt and try starting the python interpreter by typing “python”. If it starts, you are ok.</li><li>Be sure to have the file <strong>C:Program FilesPython36Libsite-packageswin32pywintypes36.dll</strong> (please note that “36” is the version of your Python installation). If you don’t have this file, take it from <strong>C:Program FilesPython36Libsite-packagespywin32_system32pywintypes36.dll</strong> and copy it into <strong>C:Program FilesPython36Libsite-packageswin32</strong></li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If you still have problems, try executing your Python script in debug mode. To try this with our previous example, open a terminal, navigate to the directory where the script resides and type</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">c:test&gt; python PythonCornerExample.py debug</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:separator {"className":"is-style-dots"} -->
<hr class="wp-block-separator is-style-dots"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>Ok, that’s all for today, this was just a brief introduction to developing Windows Services with Python. Try it by yourself and&nbsp;… happy coding!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>D.</p>
<!-- /wp:paragraph -->