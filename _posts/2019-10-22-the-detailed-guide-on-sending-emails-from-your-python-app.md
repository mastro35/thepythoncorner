---
title: The Detailed Guide on Sending Emails from your Python App
date: 2019-10-22T00:00:45+02:00
author: Andrew Zapisotskyi
excerpt: "A special article from Andrew Zapisotskyi of [mailtrap](https://mailtrap.io) about sending emails from your Python App"
header:
  teaser: https://imgs.xkcd.com/comics/mail.png
categories:
  - Dev
tags:
  - Featured
  - mail
  - Programming
  - Python
redirect_from:
  /2019/10/the-detailed-guide-on-sending-emails-from-your-python-app
---
<!-- wp:paragraph -->
<p>Hey there! Now you are reading a quick but detailed guide on adding the essential functionality to your web app built with Python: email sending. From this post, you will learn about the capabilities of the native Python modules for email sending and then &nbsp;get the practical steps for creating a message with images and attachments. With plenty of code examples, you will be able to craft and send your own emails using an SMTP server.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Before we start</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Just a brief theory and a couple of notes before we move to coding. In Python, there is an&nbsp;<em>email</em> package designed for handling email messages. We will explain how to use its main modules and components. It’s simple but comprehensive so that you don’t need any additional libraries, at least, for a start.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This guide was created and tested with Python version 3.7.2.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>How to configure email sending</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>First of all, we need to import the necessary modules. The main one for sending emails is&nbsp;<em>smtplib.&nbsp;</em>From the very beginning,&nbsp;<code>help(smtplib)</code><em>&nbsp;</em>is indeed very helpful: it will provide you with the list of all available classes and arguments as well as confirm whether&nbsp;smtplib<em>&nbsp;</em>was properly imported: <span style="color: #000000; font-weight: 400; text-decoration: none; vertical-align: baseline; font-size: 11pt; font-family: Arial; font-style: normal;"></span></p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import smtplib
help(smtplib)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:heading -->
<h2>Define SMTP server</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Before we can move to the first code sample, we should define an SMTP server. We strongly recommend starting by testing options and only when everything is set up and tested, switch to the production server.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>&nbsp;Python provides an&nbsp;<em>smtpd</em>&nbsp;module for testing your emails in the local environment. There is a&nbsp;<em>DebuggingServer&nbsp;</em>feature, for discarding your sent messages and printing them to&nbsp;<em>stdout</em>.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Set your SMTP server to&nbsp;<em>localhost:1025</em>&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">python -m smtpd -n -c DebuggingServer localhost:1025</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>With the local debugging, you can check whether your code&nbsp;works&nbsp;and detect the possible problems. Nevertheless, you won’t be able to preview your email template and verify whether it works as designed with it. For this purpose, we would advise you to use a dedicated testing tool.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Sending emails via Gmail or another external SMTP server</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To send an email via any SMTP server, you have to know the hostname and port as well as get your username and password.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The difference in sending emails via Gmail is that you need to grant access for your applications. You can do it in two ways:&nbsp;<a href="https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://myaccount.google.com/lesssecureapps%26amp;sa%3DD%26amp;ust%3D1571698656469000&amp;sa=D&amp;ust=1571698656550000&amp;usg=AFQjCNG_uhhOg21gT1ctNU7I_Mn-EfK_CQ">allow less secure apps</a>&nbsp;(2-step verification should be disabled) or use the&nbsp;<a href="https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://developers.google.com/gmail/api/quickstart/python%26amp;sa%3DD%26amp;ust%3D1571698656470000&amp;sa=D&amp;ust=1571698656550000&amp;usg=AFQjCNFZqjAT3jVYeXSUlRGTKcay6zW3Ow">OAuth2 authorization protocol</a>. The latter is more secure. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Gmail server credentials are:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"className":"lst-kix_mkcj775z7kun-0 start"} -->
<ul class="lst-kix_mkcj775z7kun-0 start"><li>the server name =<span class="Apple-converted-space">&nbsp;</span><span style="color: #000000; font-weight: 400; text-decoration: none; vertical-align: baseline; font-size: 11pt; font-family: Arial; font-style: italic;">smtp.gmail.com</span></li><li>port =<span class="Apple-converted-space">&nbsp;</span><span style="font-style: italic;">465 for SSL/TLS<span class="Apple-converted-space">&nbsp;</span></span><span style="color: #000000; font-weight: 400; text-decoration: none; vertical-align: baseline; font-size: 11pt; font-family: Arial; font-style: normal;">connection (preferred) or </span> port =<span class="Apple-converted-space">&nbsp;</span><span style="font-style: italic;">587 for STARTTLS<span class="Apple-converted-space">&nbsp;</span></span><span style="color: #000000; font-weight: 400; text-decoration: none; vertical-align: baseline; font-size: 11pt; font-family: Arial; font-style: normal;">connection</span></li><li><span style="color: #000000; font-weight: 400; text-decoration: none; vertical-align: baseline; font-size: 11pt; font-family: Arial; font-style: normal;">username = your Gmail email address</span></li><li><span style="color: #000000; font-weight: 400; text-decoration: none; vertical-align: baseline; font-size: 11pt; font-family: Arial; font-style: normal;">password = your password</span></li></ul>
<!-- /wp:list -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import smtplib, ssl
port = 465  
password = input(&quot;your password&quot;)
context = ssl.create_default_context()
with smtplib.SMTP_SSL(&quot;smtp.gmail.com&quot;, port, context=context) as server:
    server.login(&quot;my@gmail.com&quot;, password)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Alternatively, you can try Yagmail, the dedicated Gmail/SMTP, which simplifies email sending with Gmail:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import yagmail
yag = yagmail.SMTP()
contents = [
    &quot;This is the body, and here is just text http://somedomain/image.png&quot;,
    &quot;You can find an audio file attached.&quot;, '/local/path/to/song.mp3'
]
yag.send('to@someone.com', 'subject', contents)</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Finally, let’s review the whole example. We will use some external SMTP server:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import smtplib
port = 2525
smtp_server = &quot;smtp.yourserver.com&quot;
login = &quot;1a2b3c4d5e6f7g&quot; # paste your login 
password = &quot;1a2b3c4d5e6f7g&quot; # paste your password 
# specify the sender’s and receiver’s email addresses
sender = &quot;my@example.com&quot;
# make sure you are not sending test emails to real email addresses 
receiver = &quot;your@example.com&quot;
# type your message: use two newlines (\n) to separate the subject from the message body and use 'f' to  automatically insert variables in the text
message = f&quot;&quot;&quot;\
Subject: Hi there
To: {receiver}
From: {sender}
This is my first message with Python.&quot;&quot;&quot;
#send your message with credentials specified above
with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, receiver, message)
print('Sent')</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:heading -->
<h2>Sending personalized emails to multiple recipients</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Python lets you send multiple emails with dynamic content with almost no
 extra effort, with the help of loops. Make a database in a&nbsp;<strong>.csv&nbsp;</strong>format and save it to the same folder as your Python script. The most simple example is a table with two columns - &nbsp;name and email address - &nbsp;as follows:&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">#name,email
John Johnson,john@johnson.com
Peter Peterson,peter@peterson.com</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>The file will be opened with the script and its rows will be looped over line by line. In this case, the <em>{name}</em> will be replaced with the value from the “name” column:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import csv, smtplib
port = 2525 
smtp_server = &quot;smtp.yourserver.com&quot;
login = &quot;1a2b3c4d5e6f7g&quot; # paste your login 
password = &quot;1a2b3c4d5e6f7g&quot; # paste your password 
message = &quot;&quot;&quot;Subject: Order confirmation
To: {recipient}
From: {sender}
Hi {name}, thanks for your order! We are processing it now and will contact you soon&quot;&quot;&quot;
sender = &quot;new@example.com&quot;

with smtplib.SMTP(smtp_server, port) as server:
    server.login(login, password)
    with open(&quot;contacts.csv&quot;) as file:
        reader = csv.reader(file)
        next(reader)  # it skips the header row
        for name, email in reader:
            server.sendmail(
              sender,
              email,
              message.format(name=name, recipient=email, sender=sender)
            )
            print(f'Sent to {name}')</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>As a result, you should receive the following response:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;htmlmixed&quot;,&quot;mime&quot;:&quot;text/html&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">Sent to John Johnson
Sent to Peter Peterson</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:heading -->
<h2>Let’s add HTML content</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We have examined how the email sending works. Now it’s time to create email templates containing images and file attachments.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In Python, this can be done with the&nbsp;<em>email.mime</em>&nbsp;module, which handles the MIME message type. Write a text version apart from the HTML one, and then merge them with the MIMEMultipart("alternative") instance.</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
port = 2525 
smtp_server = &quot;smtp.yourserver.com&quot; 
login = &quot;1a2b3c4d5e6f7g&quot; # paste your login 
password = &quot;1a2b3c4d5e6f7g&quot; # paste your password 
sender_email = &quot;sender@example.com&quot; 
receiver_email = &quot;new@example.com&quot; 
message = MIMEMultipart(&quot;alternative&quot;) 
message[&quot;Subject&quot;] = &quot;multipart test&quot; 
message[&quot;From&quot;] = sender_email 
message[&quot;To&quot;] = receiver_email 

# write the plain text part 
text = &quot;&quot;&quot;\ Hi, Check out the new post on our blog blog: How to Send Emails with Python? https://blog.example.com/send-email-python/ Feel free to let us know what content would be useful for you!&quot;&quot;&quot; 

# write the HTML part 
html = &quot;&quot;&quot;\ &lt;html&gt; &lt;body&gt; &lt;p&gt;Hi,&lt;br&gt; Check out the new post on our blog blog: &lt;/p&gt; &lt;p&gt;&lt;a href=&quot;https://blog.example.com/send-email-python/&quot;&gt;How to Send Emails with Python?&lt;/a&gt;&lt;/p&gt; &lt;p&gt; Feel free to &lt;strong&gt;let us&lt;/strong&gt; know what content would be useful for you!&lt;/p&gt; &lt;/body&gt; &lt;/html&gt; &quot;&quot;&quot;

# convert both parts to MIMEText objects and add them to the MIMEMultipart message 
part1 = MIMEText(text, &quot;plain&quot;) 
part2 = MIMEText(html, &quot;html&quot;) 
message.attach(part1)
message.attach(part2) 

# send your email with smtplib.SMTP(&quot;smtp.yourserver.com&quot;, 2525) as server: server.login(login, password) 
server.sendmail( sender_email, receiver_email, message.as_string() ) 
print('Sent')</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:heading -->
<h2>How to attach files in Python</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In Python, email attachments are treated as the MIME objects. But first, you need to encode them with the&nbsp;<em>base64</em>&nbsp;module.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can attach images, text and audio, as well as applications. Each of 
the file types should be defined by the corresponding email class - for 
example,&nbsp;<em>email.mime.image.MIMEImage or email.mime.audio.MIMEAudio.&nbsp;</em>For details, follow&nbsp;<a href="https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://docs.python.org/3/library/email.mime.html%26amp;sa%3DD%26amp;ust%3D1571698656502000&amp;sa=D&amp;ust=1571698656559000&amp;usg=AFQjCNGNIW5oqFcJENkBJKAMes25gJYrKw">this section</a>&nbsp;of the Python documentation.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3><strong>Example of attaching a PDF file:</strong></h3>
<!-- /wp:heading -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}">import smtplib
# import the corresponding modules
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 2525 
smtp_server = &quot;smtp.yourserver.com&quot;
login = &quot;1a2b3c4d5e6f7g&quot; # paste your login 
password = &quot;1a2b3c4d5e6f7g&quot; # paste your password 
subject = &quot;An example of boarding pass&quot;
sender_email = &quot;sender@example.com&quot;
receiver_email = &quot;new@example.com&quot;

message = MIMEMultipart()
message[&quot;From&quot;] = sender_email
message[&quot;To&quot;] = receiver_email
message[&quot;Subject&quot;] = subject

# Add body to email
body = &quot;This is an example of how you can send a boarding pass in attachment with Python&quot;
message.attach(MIMEText(body, &quot;plain&quot;))
filename = &quot;yourBP.pdf&quot;

# Open PDF file in binary mode
# We assume that the file is in the directory where you run your Python script from
with open(filename, &quot;rb&quot;) as attachment:
    # The content type &quot;application/octet-stream&quot; means that a MIME attachment is a binary file
    part = MIMEBase(&quot;application&quot;, &quot;octet-stream&quot;)
    part.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part)

    # Add header 
    part.add_header(
        &quot;Content-Disposition&quot;,
        f&quot;attachment; filename= {filename}&quot;,
    )

    # Add attachment to your message and convert it to string
    message.attach(part)
    text = message.as_string()

    # send your email
    with smtplib.SMTP(&quot;smtp.yourserver.com&quot;, 2525) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, text
        )

    print('Sent')</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>Call the&nbsp;message.attach() method several times for adding several attachments</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Embed an image</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>There are three common ways to include an image in an email message: base64 image (inline embedding), CID attachment (embedded as a MIME object), and linked image.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In the example below we will experiment with inline embedding. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For this purpose, we will use the&nbsp;<em>base64</em>&nbsp;module:</p>
<!-- /wp:paragraph -->

<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre class="CodeMirror cm-s-material" data-setting="{&quot;mode&quot;:&quot;python&quot;,&quot;mime&quot;:&quot;text/x-python&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true}"># import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

port = 2525
smtp_server = &quot;smtp.yourserver.com&quot;
login = &quot;1a2b3c4d5e6f7g&quot; # paste your login 
password = &quot;1a2b3c4d5e6f7g&quot; # paste your password 
sender_email = &quot;sender@example.com&quot;
receiver_email = &quot;new@example.com&quot;
message = MIMEMultipart(&quot;alternative&quot;)
message[&quot;Subject&quot;] = &quot;inline embedding&quot;
message[&quot;From&quot;] = sender_email
message[&quot;To&quot;] = receiver_email

# The image file is in the same directory that you run your Python script from
encoded = base64.b64encode(open(&quot;illustration.jpg&quot;, &quot;rb&quot;).read()).decode()
html = f&quot;&quot;&quot;\
&lt;html&gt;
 &lt;body&gt;
   &lt;img src=&quot;data:image/jpg;base64,{encoded}&quot;&gt;
 &lt;/body&gt;
&lt;/html&gt;
&quot;&quot;&quot;

part = MIMEText(html, &quot;html&quot;)
message.attach(part)

# send your email
with smtplib.SMTP(&quot;smtp.yourserver.com&quot;, 2525) as server:
    server.login(login, password)
    server.sendmail(
       sender_email, receiver_email, message.as_string()
   )
print('Sent')</pre></div>
<!-- /wp:codemirror-blocks/code-block -->

<!-- wp:paragraph -->
<p>That's it!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Useful resources for sending emails with Python</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Python offers a wide set of capabilities for email sending. In this article, we went through the main steps. To go further, you can refer to the&nbsp;<a href="https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://docs.python.org/3/library/email.html%26amp;sa%3DD%26amp;ust%3D1571698656527000&amp;sa=D&amp;ust=1571698656566000&amp;usg=AFQjCNGu8NQ5Hp41gjq2_yncquv114dZMw">Python documentation</a>&nbsp;and also try additional libraries such as Flask Mail or Marrow Mailer.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here you will find a really&nbsp;<a href="https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://awesome-python.com/%26amp;sa%3DD%26amp;ust%3D1571698656527000&amp;sa=D&amp;ust=1571698656567000&amp;usg=AFQjCNE9j1NJsff6cDe5yCH2bzKDrKyNug">awesome list</a>&nbsp;of Python resources sorted by their functionality.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>This article was originally published on Mailtrap’s blog:&nbsp;<a href="https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/%26amp;sa%3DD%26amp;ust%3D1571698656528000&amp;sa=D&amp;ust=1571698656567000&amp;usg=AFQjCNF0Cch_ocBxwHhOWI0AI0TwBrvupg">Sending emails with Python</a></em>.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><span style="color: #222222; font-style: italic;"></span><span style="color: #222222; font-weight: 400; text-decoration: none; vertical-align: baseline; font-size: 11pt; font-family: Arial; font-style: normal;"><span class="Apple-converted-space"></span></span></p>
<!-- /wp:paragraph -->