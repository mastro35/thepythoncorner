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
  - /2019/10/the-detailed-guide-on-sending-emails-from-your-python-app
  - /2019/10/the-detailed-guide-on-sending-emails-from-your-python-app/
  - /dev/the-detailed-guide-on-sending-emails-from-your-python-app/
  - /posts/2019-10-22-the-detailed-guide-on-sending-emails-from-your-python-app/
---
![teaser](https://imgs.xkcd.com/comics/mail.png)

Hey there! Now you are reading a quick but detailed guide on adding the essential functionality to your web app built with Python: email sending. From this post, you will learn about the capabilities of the native Python modules for email sending and then  get the practical steps for creating a message with images and attachments. With plenty of code examples, you will be able to craft and send your own emails using an SMTP server.

## Before we start

Just a brief theory and a couple of notes before we move to coding. In Python, there is an *email* package designed for handling email messages. We will explain how to use its main modules and components. It's simple but comprehensive so that you don't need any additional libraries, at least, for a start.

This guide was created and tested with Python version 3.7.2.

## How to configure email sending

First of all, we need to import the necessary modules. The main one for sending emails is *smtplib*. From the very beginning, `help(smtplib)` is indeed very helpful: it will provide you with the list of all available classes and arguments as well as confirm whether *smtplib* was properly imported:

```python
import smtplib
help(smtplib)
```

## Define SMTP server

Before we can move to the first code sample, we should define an SMTP server. We strongly recommend starting by testing options and only when everything is set up and tested, switch to the production server.

Python provides an *smtpd* module for testing your emails in the local environment. There is a *DebuggingServer *feature, for discarding your sent messages and printing them to *stdout*. 

Set your SMTP server to *localhost:1025* 

```console
python -m smtpd -n -c DebuggingServer localhost:1025
```

With the local debugging, you can check whether your code works and detect the possible problems. Nevertheless, you won't be able to preview your email template and verify whether it works as designed with it. For this purpose, we would advise you to use a dedicated testing tool.

## Sending emails via Gmail or another external SMTP server

To send an email via any SMTP server, you have to know the hostname and port as well as get your username and password.

The difference in sending emails via Gmail is that you need to grant access for your applications. You can do it in two ways: [allowing less secure apps](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://myaccount.google.com/lesssecureapps%26amp;sa%3DD%26amp;ust%3D1571698656469000&amp;sa=D&amp;ust=1571698656550000&amp;usg=AFQjCNG_uhhOg21gT1ctNU7I_Mn-EfK_CQ) (2-step verification should be disabled) or using the [OAuth2 authorization protocol](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://developers.google.com/gmail/api/quickstart/python%26amp;sa%3DD%26amp;ust%3D1571698656470000&amp;sa=D&amp;ust=1571698656550000&amp;usg=AFQjCNFZqjAT3jVYeXSUlRGTKcay6zW3Ow).
The latter is more secure.

The Gmail server credentials are:

- the server name = **smtp.gmail.com**
- port = **465** for SSL/TLS (preferred) or **587** for STARTTLS connection
- username = **your Gmail email address**
- password = **your password**

```python
import smtplib, ssl
port = 465  
password = input("your password")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
```

Alternatively, you can try Yagmail, the dedicated Gmail/SMTP, which simplifies email sending with Gmail:

```python
import yagmail
yag = yagmail.SMTP()
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('to@someone.com', 'subject', contents)
```

Finally, let's review the whole example. We will use some external SMTP server:

```python
import smtplib
port = 2525
smtp_server = "smtp.yourserver.com"
login = "1a2b3c4d5e6f7g" # paste your login 
password = "1a2b3c4d5e6f7g" # paste your password 
# specify the sender's and receiver's email addresses
sender = "my@example.com"
# make sure you are not sending test emails to real email addresses 
receiver = "your@example.com"
# type your message: use two newlines (\n) to separate the subject from the message body and use 'f' to  automatically insert variables in the text
message = f"""\
Subject: Hi there
To: {receiver}
From: {sender}
This is my first message with Python."""
#send your message with credentials specified above
with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, receiver, message)
print('Sent')
```

## Sending personalized emails to multiple recipients

Python lets you send multiple emails with dynamic content with almost no
 extra effort, with the help of loops. Make a database in a **.csv **format and save it to the same folder as your Python script. The most simple example is a table with two columns -  name and email address -  as follows: 

```console
#name,email
John Johnson,john@johnson.com
Peter Peterson,peter@peterson.com
```

The file will be opened with the script and its rows will be looped over line by line. In this case, the *{name}* will be replaced with the value from the "name" column:

```python
import csv, smtplib
port = 2525 
smtp_server = "smtp.yourserver.com"
login = "1a2b3c4d5e6f7g" # paste your login 
password = "1a2b3c4d5e6f7g" # paste your password 
message = """Subject: Order confirmation
To: {recipient}
From: {sender}
Hi {name}, thanks for your order! We are processing it now and will contact you soon"""
sender = "new@example.com"

with smtplib.SMTP(smtp_server, port) as server:
    server.login(login, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # it skips the header row
        for name, email in reader:
            server.sendmail(
              sender,
              email,
              message.format(name=name, recipient=email, sender=sender)
            )
            print(f'Sent to {name}')
```

As a result, you should receive the following response:

```console
Sent to John Johnson
Sent to Peter Peterson
```

## Let's add HTML content

We have examined how the email sending works. Now it's time to create email templates containing images and file attachments.

In Python, this can be done with the *email.mime* module, which handles the MIME message type. Write a text version apart from the HTML one, and then merge them with the MIMEMultipart("alternative") instance.

```python
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
port = 2525 
smtp_server = "smtp.yourserver.com" 
login = "1a2b3c4d5e6f7g" # paste your login 
password = "1a2b3c4d5e6f7g" # paste your password 
sender_email = "sender@example.com" 
receiver_email = "new@example.com" 
message = MIMEMultipart("alternative") 
message["Subject"] = "multipart test" 
message["From"] = sender_email 
message["To"] = receiver_email 

# write the plain text part 
text = """\ Hi, Check out the new post on our blog blog: How to Send Emails with Python? https://blog.example.com/send-email-python/ Feel free to let us know what content would be useful for you!""" 

# write the HTML part 
html = """\ <html> <body> <p>Hi,\n Check out the new post on our blog blog: </p> <p><a href="https://blog.example.com/send-email-python/">How to Send Emails with Python?</p> <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p> </body> </html> """

# convert both parts to MIMEText objects and add them to the MIMEMultipart message 
part1 = MIMEText(text, "plain") 
part2 = MIMEText(html, "html") 
message.attach(part1)
message.attach(part2) 

# send your email with smtplib.SMTP("smtp.yourserver.com", 2525) as server: server.login(login, password) 
server.sendmail( sender_email, receiver_email, message.as_string() ) 
print('Sent')
```

## How to attach files in Python

In Python, email attachments are treated as the MIME objects. But first, you need to encode them with the *base64* module.

You can attach images, text and audio, as well as applications. Each of 
the file types should be defined by the corresponding email class - for 
example, *email.mime.image.MIMEImage or email.mime.audio.MIMEAudio. *For details, follow [this section of the Python documentation](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://docs.python.org/3/library/email.mime.html%26amp;sa%3DD%26amp;ust%3D1571698656502000&amp;sa=D&amp;ust=1571698656559000&amp;usg=AFQjCNGNIW5oqFcJENkBJKAMes25gJYrKw).

## **Example of attaching a PDF file:**

```python
import smtplib
# import the corresponding modules
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 2525 
smtp_server = "smtp.yourserver.com"
login = "1a2b3c4d5e6f7g" # paste your login 
password = "1a2b3c4d5e6f7g" # paste your password 
subject = "An example of boarding pass"
sender_email = "sender@example.com"
receiver_email = "new@example.com"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
body = "This is an example of how you can send a boarding pass in attachment with Python"
message.attach(MIMEText(body, "plain"))
filename = "yourBP.pdf"

# Open PDF file in binary mode
# We assume that the file is in the directory where you run your Python script from
with open(filename, "rb") as attachment:
    # The content type "application/octet-stream" means that a MIME attachment is a binary file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part)

    # Add header 
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to your message and convert it to string
    message.attach(part)
    text = message.as_string()

    # send your email
    with smtplib.SMTP("smtp.yourserver.com", 2525) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, text
        )

    print('Sent')
```

Call the message.attach() method several times for adding several attachments

## Embed an image

There are three common ways to include an image in an email message: base64 image (inline embedding), CID attachment (embedded as a MIME object), and linked image. 

In the example below we will experiment with inline embedding. 

For this purpose, we will use the *base64* module:

```python
# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

port = 2525
smtp_server = "smtp.yourserver.com"
login = "1a2b3c4d5e6f7g" # paste your login 
password = "1a2b3c4d5e6f7g" # paste your password 
sender_email = "sender@example.com"
receiver_email = "new@example.com"
message = MIMEMultipart("alternative")
message["Subject"] = "inline embedding"
message["From"] = sender_email
message["To"] = receiver_email

# The image file is in the same directory that you run your Python script from
encoded = base64.b64encode(open("illustration.jpg", "rb").read()).decode()
html = f"""\
<html>
 <body>
   <img src="data:image/jpg;base64,{encoded}">
 </body>
</html>
"""

part = MIMEText(html, "html")
message.attach(part)

# send your email
with smtplib.SMTP("smtp.yourserver.com", 2525) as server:
    server.login(login, password)
    server.sendmail(
       sender_email, receiver_email, message.as_string()
   )
print('Sent')
```

That's it!

## Useful resources for sending emails with Python

Python offers a wide set of capabilities for email sending. In this article, we went through the main steps. To go further, you can refer to the [Python documentation](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://docs.python.org/3/library/email.html%26amp;sa%3DD%26amp;ust%3D1571698656527000&amp;sa=D&amp;ust=1571698656566000&amp;usg=AFQjCNGu8NQ5Hp41gjq2_yncquv114dZMw) and also try additional libraries such as Flask Mail or Marrow Mailer.

Here you will find a really [awesome list of Python resources](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://awesome-python.com/%26amp;sa%3DD%26amp;ust%3D1571698656527000&amp;sa=D&amp;ust=1571698656567000&amp;usg=AFQjCNE9j1NJsff6cDe5yCH2bzKDrKyNug) sorted by their functionality. 

*This article was originally published on Mailtrap's blog: [Sending emails with Python](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/%26amp;sa%3DD%26amp;ust%3D1571698656528000&amp;sa=D&amp;ust=1571698656567000&amp;usg=AFQjCNF0Cch_ocBxwHhOWI0AI0TwBrvupg)*.
