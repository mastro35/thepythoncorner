---
title: "Serialization in Python with JSON"
date: 2020-02-20T00:00:49+01:00
author: "davide_mastromatteo"
excerpt: "Did you know that Python is one of the best programming languages to be used if you want to work with JSON?"
header:
  teaser: https://imgs.xkcd.com/comics/wanna_see_the_code.png
categories:
  - Dev
tags:
  - json
  - serialization
  - python
aliases:
  - /2020/02/serialization-in-python-with-json
  - /2020/02/serialization-in-python-with-json/
  - /dev/serialization-python-json/
---
![teaser](https://imgs.xkcd.com/comics/wanna_see_the_code.png)

In 2016 [I wrote a post about serialization in Python](https://www.thepythoncorner.com/2016/12/object-serialization-in-python/) by using the `pickle` Python module.

In this article, we will try to serialize Python objects by using another module: `json`.

According to [Wikipedia](https://en.wikipedia.org/wiki/JSON) "JSON is an open-standard file format or data interchange format that uses human-readable text to transmit data objects consisting of attribute-value pairs and array data types (or any other serializable value)".

But why you should use to use JSON instead of the official `pickle` module? 
Well, it depends on what you have to do... JSON is a safer protocol, it's human-readable and it's a standard adopted by a lot of languages out there (so it's the best choice if you need a language independent platform). `pickle`, on the other side, is faster and allow you to serialize even custom defined objects.

So, there isn't a silver bullet if you want to serialize and deserialize objects, you have to choose which module to use depending on your specific use case.

Now, before starting I need to tell you something: do not expect me to explain what *serialization* means. If you don't know that, start by reading my [previous article](https://www.thepythoncorner.com/2016/12/object-serialization-in-python/) on this topic.

However, if you just need a hint I could also cite the 2016 myself:

> To serialize an object means to transform it in a format that can be stored, to be able to deserialize it later, recreating the original object from the serialized format. To do all these operations we will use the pickle module.

Pretty straightforward, uh?
And now... it's JSON time!

I still remember the first time I met JSON... what a wonderful time! Someone told me that the *JS* part of the JSON word means "JavaScript" and so I had myself and decided to retire in a Buddist temple for the rest of my life.

![alan](https://mastro35.github.io/thepythoncorner/images/alan_meditation.jpg)

Then I had the enlightenment and understood that I had better to decipher the whole acronym... and I found out that JSON stands for **JavaScript Object Notation**.

So the *JavaScript* part is just about the "Object Notation" token?
Why did they decide to use the world *Javascript* on something not related to that *$)%!(£&* little language?
Who knows...

However, I decided to dig a little bit more and this is how a JSON object appears to be:

```JSON
{"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}
```

Yes, it's just like a Python dictionary! Isn't that great?

So how can we serialize a Python object in a JSON format?

Quite easy, you just need to import the `JSON` module and then use the `dumps()` and `loads()` functions:

- `dumps()` takes a Python object and returns a string with the result of the JSON serialization process.
- `loads()` takes a JSON string and returns the corresponding Python object.

Let see an example of how this works:

```python
# json1.py
import json

my_list = ["this","is","a","simple","list",35]
my_json_object = json.dumps(my_list)
print(my_json_object)

my_second_list = json.loads(my_json_object)
print(my_second_list)
```

Really easy, isn't it?

It's also possible to use the `dump()` and `load()` functions to serialize and deserialize objects. In this case, instead of strings, you will directly use files, like this:

```python
# json2.py
import json

my_list = ["this","is","a","simple","list",35]
with open("my_file", "w") as my_file:
    my_json_object = json.dump(my_list, my_file)

with open("my_file", "r") as my_file_read:
    my_second_list = json.load(my_file_read)

print(my_second_list)
```

In this last example, with the first `dump()` method you create a file named `my_file` with the JSON result of the serialization process and with the next `load()` method you read the previously created file and deserialize the JSON to a Python object.

Super easy, isn't it?

Please remember that not every Python object can be serialized in JSON.
This process works just with the following types:

- dict
- list
- str
- int
- float
- True
- False
- None

However, it's possible to serialize and deserialize even custom object with just a little bit of extra magic... do you want to know how? Stay tuned for the next article! ;)

Happy Pythoning 
D.
