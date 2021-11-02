---
title: "How to create a telegram bot with Python in minutes"
date: 2021-01-16T16:00:47+01:00
author: "davide_mastromatteo"
excerpt: "Creating a Telegram bot in Python couldn't be easier. Don't you believe me? Have a look at this article and let's write our first bot in minutes!"
header:
  teaser: https://imgs.xkcd.com/comics/android_girlfriend.png
categories:
  - Dev
tags:
  - telegram bot
  - bot
  - python
aliases:
  - /dev/how-create-telegram-bot-in-Python/
---
![teaser](https://imgs.xkcd.com/comics/android_girlfriend.png)

Creating a telegram bot with Python in minutes may seem like a clickbait title for a post, but trust me, it's possible. If you're going through a boring afternoon or you're locked down due to COVID restriction and you want to do something different, keep reading and let's create our first Python Telegram bot! :)

For this project, all you will have to use is the  [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) package that's basically a wrapper around telegram APIs. Python Telegram Bot is fully compatible with Python 3.6+ and will make developing a Telegram Bot a piece of cake.

So, let's start by installing this package (I strongly recommend to use a virtual environment for this kind of things: if you don't know how to do it, just look at this [old article](https://thepythoncorner.com/dev/using-virtual-environments-python/) or stay tuned, because I'm going to write something about it soon...

$ pip install python-telegram-bot --upgrade

Now that you have installed the package, let's start with creating our first bot. And guess what? You don't need any Python to create a bot, you just need to chat with the Telegram **BotFather** account.

Once you start chatting with the *BotFather* bot, you just need to issue the `/newbot` command and answer the questions of *BotFather* will ask you: the name of your bot (it's the display name) and the username of your bot.

![botfather1](https://mastro35.github.io/thepythoncorner/images/botfather1.png){: .align-center}

![botfather2](https://mastro35.github.io/thepythoncorner/images/botfather2.png){: .align-center}

That's it, your bot is ready! There is a lot of other stuff that you can ask to BotFather (like changing the profile pic of your bot, for example) but for this basic tutorial, we won't need anything else.

Now, you're going to face a tough decision: what will your bot do? The bot we will create with this example will give visitors information about their *biorhythm*. If you don't know what a biorhythm is, [check this page](https://en.wikipedia.org/wiki/Biorhythm_(pseudoscience)) on Wikipedia and you will find out two important things:

1. According to the theory of biorhythms "a person's life is influenced by rhythmic biological cycles that affect his or her ability in various domains, such as mental, physical, and emotional activity".
2. The proposal has been independently tested and, consistently, **no validity** for it has been found. :)

So our bot will be as useful as reading the horoscope... that's cool uh? :)

But don't worry: at the end of the article, you will be able to program any kind of bots, either completely useless like this one or useful ones! :)

Now, let's see how can we program the bot.

The **python-telegram-bot** package consists of a wrapper around Telegram APIs. The Telegram APIs are exposed via the `telegram.Bot` class. However, on top of this class, they have built the `telegram.ext` module, which will make your work a lot easier, allowing you to create a bot in minutes.

The `telegram.ext` module contains a lot of classes, but the most important two are `telegram.ext.Updater` and `telegram.ext.Dispatcher`. The `Updater` class is responsible for fetching new updates from Telegram and passing them to the `Dispatcher` class, which will handle them through a `Handler` class.

So let's start coding!

```python
# mastrobot_example.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# function to handle the /start command
def start(update, context):
    update.message.reply_text('start command received')

# function to handle the /help command
def help(update, context):
    update.message.reply_text('help command received')

# function to handle errors occured in the dispatcher 
def error(update, context):
    update.message.reply_text('an error occured')

# function to handle normal text 
def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'did you said "{text_received}" ?')

def main():
    TOKEN = "insert here your token and don't share it with anyone!"

    # create the updater, that will automatically create also a dispatcher and a queue to 
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
```

This first example is quite trivial. In the main function, we have created the `Updater` class, which has automatically created for us a `Dispatcher` object, available through the `.dispatcher` property of the `Updater` class.

Then, we've added some handlers for:
* the `/start` command (we simply call the callback function `start()` that reply to the user with an informative message) 
* the `/help` command (we simply call the callback function `help()` that reply to the user with an informative message)
* what happens if an error occurs while dispatching messages (we simply call the callback function `error()`)
* what happens if the user writes something that is not a command (we simply call the callback function `text()` that reply to the user with the same text received)

Finally, we have written the callback functions, that use the update object received to send messages to the user.

Let's test this primitive bot.
Start your bot with:

```console
$ python mastrobot_example.py
```

and now, let's start chatting with our new bot:

![bot1](https://mastro35.github.io/thepythoncorner/images/bot1.png){: .align-center}

It works!

Now, we wanted to create a bot to tell the user their daily biorhythm, right? This will be easy, we will use the `/start` command to get the birthday of the user as the chat starts, and then we will create a function to handle a new `/biorhythm` command to answer the user with its personal biorhythm.

Let's start with the first part: knowing the user's birthday.

The first thing to do is to change the function that handles the `/start` command. We will ask the user it's birthday and we will call a function to start the interaction with the user. To make it simple, we will ask the user the year, the month, and the day they were born in.

```python
# function to handle the /start command
def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f"Hi {first_name}, nice to meet you!")
    start_getting_birthday_info(update, context)
```

As you can see, in the `update` parameter you will find also some useful information about the user, like its name. However, since this is just a starting tutorial to whet your appetite, I won't discuss here the thousand of things you will be able to do with this package, if you want to know everything about the *python-telegram-bot* package, just check the [official documentation](https://python-telegram-bot.readthedocs.io/en/stable/).

Now, at the very beginning of our script, we will define a new variable `STATE` that will be used to understand what question the user is answering. Don't worry if you can't get it now, you will get it in a minute.

```python
STATE = None

BIRTH_YEAR = 1
BIRTH_MONTH = 2
BIRTH_DAY = 3
```

Now, we need to implement the function `start_getting:_birthday_info()` we are calling in the `start()` function and that starts... getting birthday info from user :) :

```python
def start_getting_birthday_info(update, context):
    global STATE
    STATE = BIRTH_YEAR
    update.message.reply_text(f"I would need to know your birthday, so tell me what year did you born in...")
```

As you can see, at the beginning we set the variable `STATE` to the value `BIRTH_YEAR` so that we will know, when the user will answer, that it was answering the birth year question. Then, we just send a message to ask for the year of birth.

Now, the user will answer with a normal text, right? So we need to change the `text()` function to wait for its answer:

```python
def text(update, context):
    global STATE

    if STATE == BIRTH_YEAR:
        return received_birth_year(update, context)

    if STATE == BIRTH_MONTH:
        return received_birth_month(update, context)

    if STATE == BIRTH_DAY:
        return received_birth_day(update, context)
```

Here in the `text()` function we just need to understand what's the question the user is answering by using the `STATE` variable we defined before, and call a specific function to handle each answer.

These functions could be written like this:

```python
def received_birth_year(update, context):
    global STATE

    try:
        today = datetime.date.today()
        year = int(update.message.text)
        
        if year > today.year:
            raise ValueError("invalid value")

        context.user_data['birth_year'] = year
        update.message.reply_text(f"ok, now I need to know the month (in numerical form)...")
        STATE = BIRTH_MONTH
    except:
        update.message.reply_text("it's funny but it doesn't seem to be correct...")

def received_birth_month(update, context):
    global STATE

    try:
        today = datetime.date.today()
        month = int(update.message.text)

        if month > 12 or month < 1:
            raise ValueError("invalid value")

        context.user_data['birth_month'] = month
        update.message.reply_text(f"great! And now, the day...")
        STATE = BIRTH_DAY
    except:
        update.message.reply_text("it's funny but it doesn't seem to be correct...")

def received_birth_day(update, context):
    global STATE

    try:
        today = datetime.date.today()
        dd = int(update.message.text)
        yyyy = context.user_data['birth_year']
        mm = context.user_data['birth_month']
        birthday = datetime.date(year=yyyy, month=mm, day=dd)

        if today - birthday < datetime.timedelta(days=0):
            raise ValueError("invalid value")

        context.user_data['birthday'] = birthday
        STATE = None
        update.message.reply_text(f'ok, you born on {birthday}')

    except:
        update.message.reply_text("it's funny but it doesn't seem to be correct...")        
```

As you can see, when we receive the user birth year, we just check if it is a valid value and in this case, we save it to the `context.user_data[]` dictionary, and then we go ahead setting the next value for the `STATE` variable and asking the next question.

When the last question is asked and we received the day of birth, we just create a date variable and store it in the `context.user_data[]` dictionary as well.

If the user enters an invalid value, we just tell them that it's not correct and doesn't change the value of the `STATE` variable, so the user is stuck with that question until it doesn't answer correctly.

Ok, now we just need to handle the `/biorhythm` command and we've finished.

Let's start adding a new command handler into our `main()` function:

```python
    dispatcher.add_handler(CommandHandler("biorhythm", biorhythm))
```

and let's write the function that calculate the biorhythm:

```python
# This function is called when the /biorhythm command is issued
def biorhythm(update, context):
    user_biorhythm = calculate_biorhythm(
        context.user_data['birthday'])

    update.message.reply_text(f"Phisical: {user_biorhythm['phisical']}")
    update.message.reply_text(f"Emotional: {user_biorhythm['emotional']}")
    update.message.reply_text(f"Intellectual: {user_biorhythm['intellectual']}")

def calculate_biorhythm(birthdate):
    today = datetime.date.today()
    delta = today - birthdate
    days = delta.days

    phisical = math.sin(2*math.pi*(days/23))
    emotional = math.sin(2*math.pi*(days/28))
    intellectual = math.sin(2*math.pi*(days/33))

    biorhythm = {}
    biorhythm['phisical'] = int(phisical * 10000)/100
    biorhythm['emotional'] = int(emotional * 10000)/100
    biorhythm['intellectual'] = int(intellectual * 10000)/100

    biorhythm['phisical_critical_day'] = (phisical == 0)
    biorhythm['emotional_critical_day'] = (emotional == 0)
    biorhythm['intellectual_critical_day'] = (intellectual == 0)

    return biorhythm
```

As you can see I have written two different functions, one to handle the command and the other one to calculate the biorhythm to separate the responsibility of these functions.

So, here there's the complete code of our bot:

```python
# mastrobot_example2.py
import datetime
import math
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

STATE = None
BIRTH_YEAR = 1
BIRTH_MONTH = 2
BIRTH_DAY = 3

# function to handle the /start command
def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f"Hi {first_name}, nice to meet you!")
    start_getting_birthday_info(update, context)

def start_getting_birthday_info(update, context):
    global STATE
    STATE = BIRTH_YEAR
    update.message.reply_text(
        f"I would need to know your birthday, so tell me what year did you born in...")

def received_birth_year(update, context):
    global STATE

    try:
        today = datetime.date.today()
        year = int(update.message.text)

        if year > today.year:
            raise ValueError("invalid value")

        context.user_data['birth_year'] = year
        update.message.reply_text(
            f"ok, now I need to know the month (in numerical form)...")
        STATE = BIRTH_MONTH
    except:
        update.message.reply_text(
            "it's funny but it doesn't seem to be correct...")

def received_birth_month(update, context):
    global STATE

    try:
        today = datetime.date.today()
        month = int(update.message.text)

        if month > 12 or month < 1:
            raise ValueError("invalid value")

        context.user_data['birth_month'] = month
        update.message.reply_text(f"great! And now, the day...")
        STATE = BIRTH_DAY
    except:
        update.message.reply_text(
            "it's funny but it doesn't seem to be correct...")

def received_birth_day(update, context):
    global STATE

    try:
        today = datetime.date.today()
        dd = int(update.message.text)
        yyyy = context.user_data['birth_year']
        mm = context.user_data['birth_month']
        birthday = datetime.date(year=yyyy, month=mm, day=dd)

        if today - birthday < datetime.timedelta(days=0):
            raise ValueError("invalid value")

        context.user_data['birthday'] = birthday
        STATE = None
        update.message.reply_text(f'ok, you born on {birthday}')

    except:
        update.message.reply_text(
            "it's funny but it doesn't seem to be correct...")

# function to handle the /help command
def help(update, context):
    update.message.reply_text('help command received')

# function to handle errors occured in the dispatcher
def error(update, context):
    update.message.reply_text('an error occured')

# function to handle normal text
def text(update, context):
    global STATE

    if STATE == BIRTH_YEAR:
        return received_birth_year(update, context)

    if STATE == BIRTH_MONTH:
        return received_birth_month(update, context)

    if STATE == BIRTH_DAY:
        return received_birth_day(update, context)

# This function is called when the /biorhythm command is issued
def biorhythm(update, context):
    print("ok")
    user_biorhythm = calculate_biorhythm(
        context.user_data['birthday'])

    update.message.reply_text(f"Phisical: {user_biorhythm['phisical']}")
    update.message.reply_text(f"Emotional: {user_biorhythm['emotional']}")
    update.message.reply_text(f"Intellectual: {user_biorhythm['intellectual']}")

def calculate_biorhythm(birthdate):
    today = datetime.date.today()
    delta = today - birthdate
    days = delta.days

    phisical = math.sin(2*math.pi*(days/23))
    emotional = math.sin(2*math.pi*(days/28))
    intellectual = math.sin(2*math.pi*(days/33))

    biorhythm = {}
    biorhythm['phisical'] = int(phisical * 10000)/100
    biorhythm['emotional'] = int(emotional * 10000)/100
    biorhythm['intellectual'] = int(intellectual * 10000)/100

    biorhythm['phisical_critical_day'] = (phisical == 0)
    biorhythm['emotional_critical_day'] = (emotional == 0)
    biorhythm['intellectual_critical_day'] = (intellectual == 0)

    return biorhythm

def main():
    TOKEN = "insert here your token and don't share it with anyone!"

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # add an handler for our biorhythm command
    dispatcher.add_handler(CommandHandler("biorhythm", biorhythm))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
```

It's time to test it, right?

![bot2](https://mastro35.github.io/thepythoncorner/images/bot2.png){: .align-center}

Oh my gosh... I hope you won't find too many mistakes in this article, but in that case bear with me, my intellectual cycle today is only at 28%... that's not so good uh?

I will keep the bot alive, so you can try it if you want (the username is @mastro35_mastrobot) but if it doesn't work ... consider that it's running on my raspberry pi and that it could be offline sometimes...

Ok guys, it's enough for today! If you liked this article feel free to click on the **buy me a coffee** button or subscribe to become a member and [support me on a monthly basis](https://www.buymeacoffee.com/dXjDHmt).

Happy coding and... stay safe!
D.
