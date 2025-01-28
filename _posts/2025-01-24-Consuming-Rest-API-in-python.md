---
title: How to consume REST APIs in Python
date: 2025-01-27T19:52:52+02:00
author: Davide Mastromatteo
excerpt: "REST APIs have become a standard for web application communication. 
In this article, we will explore how to consume REST APIs using Python."
header:
  teaser: https://imgs.xkcd.com/comics/api.png
categories:
  - Dev
tags:
  - API
  - RestAPI
  - Python
---
![teaser](https://imgs.xkcd.com/comics/api.png)


REST APIs have become a standard for web application communication. 
In this article, we will explore how to consume REST APIs using our beloved programming language: Python. 

## What are REST APIs

An API (Application Programming Interface) is a set of rules that allows different software entities to communicate with each other. APIs define the methods and data formats that applications can use to interact with each other.

REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol -- the HTTP. 

REST APIs are widely used because they are simple, scalable, and easy to integrate with and they become very popular because they use standard HTTP methods (GET, POST, PUT, DELETE) and can return data in various formats, such as JSON and XML. They are also stateless, meaning each request from a client contains all the information needed to process the request.

## Calling APIs in Python

Before we start making API calls, let's set up our Python environment. You'll need to install the `requests` library, which makes it easy to send HTTP requests in Python.
(Always keep in mind that it's a good idea to use a [virtual environment for this](https://thepythoncorner.com/posts/2016-11-28-using-virtual-environments-python/)).

```bash
pip install requests
```

Now, we're ready to make a simple call to a public API. 

> *Tip Time: If you don't know where to start looking for public APIs, consider visiting https://publicapis.dev*

In this article, we will call the https://stephen-king-api.onrender.com/api/books API, which returns all the books written by Stephen King in JSON format. If you don't know who Stephen King is... oh, come on!!!

```python
import requests

response = requests.get('https://stephen-king-api.onrender.com/api/books')
print(response.json())
```

Try to run the code and you will get something like this:

```console
"data":[{"id":1,"Year":1974,"Title":"Carrie","handle":"carrie","Publisher":"Doubleday","ISBN":"978-0-385-08695-0","Pages":199,"Notes":[""],"created_at":"2023-11-13T23:48:47.848Z","villains":[{"name":"Tina Blake","url":"https://stephen-king-api.onrender.com/api/villain/4"},{"name":"Cindi","url":"https://stephen-king-api.onrender.com/api/villain/14"},{"name":"Myra Crewes","url":"https://stephen-king-api.onrender.com/api/villain/16"},{"name":"Billy deLois","url":"https://stephen-king-api.onrender.com/api/villain/25"},{"name":"Kenny Garson","url":"https://stephen-king-api.onrender.com/api/villain/38"},{"name":"Mary Lila Grace","url":"https://stephen-king-api.onrender.com/api/villain/44"},{"name":"Christine Hargensen","url":"https://stephen-king-api.onrender.com/api/villain/49"},{"name":"Vic Mooney","url":"https://stephen-king-api.onrender.com/api/villain/75"},{"name":"The Mortimer Snerds","url":"https://stephen-king-api.onrender.com/api/villain/77"},{"name":"Billy Nolan","url":"https://stephen-king-api.onrender.com/api/villain/80"},{"name":"Elenor Richmond","url":"https://stephen-king-api.onrender.com/api/villain/90"},{"name":"Rachel Spies","url":"https://stephen-king-api.onrender.com/api/villain/94"},{"name":"Jackie Talbot","url":"https://stephen-king-api.onrender.com/api/villain/99"},{"name":"Donna and Mary Lila Grace Thibodeau","url":"https://stephen-king-api.onrender.com/api/villain/102"},{"name":"Jessica Upshaw","url":"https://stephen-king-api.onrender.com/api/villain/108"},{"name":"Norma Watson","url":"https://stephen-king-api.onrender.com/api/villain/109"},{"name":"Margaret White","url":"https://stephen-king-api.onrender.com/api/villain/113"}]},{"id":2,"Year":1975,"Title":"Salem's Lot","handle":"salem-s-lot","Publisher":"Doubleday","ISBN":"978-0-385-00751-1","Pages":439,"Notes":["Nominee, World Fantasy Award, 1976[2]"],"created_at":"2023-11-13T23:48:48.098Z","villains":[{"name ....
```
Wow! It seems Stephen hasn't had much spare time lately, has he?

> *Tip Time: When dealing with JSON format, keep in mind that online there are a lot of viewers that allow you to see your JSON nicely formatted and validate, for example: https://jsonformatter.curiousconcept.com/*

Now, if you're wondering why we used the HTTP `GET` method instead of the `POST` one, consider that it's a good practice when you are designing an API to use the methods according to what you want the API to do.
So:

- **GET:** Is used to retrieve data from the server.
- **POST:** Is used to send data to the server.
- **PUT:** Is used to update existing data on the server.
- **DELETE:** Is used to delete data from the server.

## Handling API Responses

When working with APIs, it's important to handle responses correctly.
So, the first thing that you need to do after the call, is to make sure that the server has answered correctly.
You can check this by using the `status_code` property like this:

```python
import requests

response = requests.get('https://stephen-king-api.onrender.com/api/books')

if response.status_code == 200:
    print(response.json())
else:
    print("an error occured")
```

Try to execute this code and you will see that everything works as expected. 
Now try to change the called URL by adding some extra character and you will see that the program will tell you that an error occured, since the call would probably end with an HTTP 404 status code.

> *Tip Time: You can find a list of possible status codes [here](https://openapi.com/blog/status-codes-rest-api) but remember to always check for them also in your API's documentation.*
>
> Common HTTP status code are: 
>- **200 OK:** The request was successful.
>- **201 Created:** The request was successful, and a resource was created.
>- **400 Bad Request:** The request was invalid or cannot be served.
>- **401 Unauthorized:** Authentication is required and has failed or has not yet been provided.
>- **403 Forbidden:** The request is valid, but the server is refusing action.
>- **404 Not Found:** The requested resource could not be found.
>- **500 Internal Server Error:** An error occurred on the server.


When dealing with REST APIs remember that usually they return their results in JSON format and that the response module has a `.json()` method to parse the response out of the box. This method is super convenient and allows you to parse the result with no effort, for example:

```python
import requests

response = requests.get('https://stephen-king-api.onrender.com/api/books')

if response.status_code == 200:
    books = response.json()['data']
    for book in books:
        print(f"{book['Year']} - {book['Title']}")
else:
    print("an errore occured")
```

Try to execute this version of our program and you will get something like this:

```console
1974 - Carrie
1975 - Salem's Lot
1977 - The Shining
1977 - Rage
1978 - The Stand
1979 - The Long Walk
1979 - The Dead Zone
1980 - Firestarter
1981 - Roadwork
1981 - Cujo
1982 - The Running Man
1982 - The Dark Tower: The Gunslinger
1983 - Christine
1983 - Pet Sematary
1983 - Cycle of the Werewolf
1984 - The Talisman
1984 - The Eyes of the Dragon
1984 - Thinner
1986 - It
1987 - The Dark Tower II: The Drawing of the Three
1987 - Misery
1987 - The Tommyknockers
1989 - The Dark Half
1990 - The Stand Uncut
1991 - The Dark Tower III: The Waste Lands
1991 - Needful Things
1992 - Gerald's Game
1992 - Dolores Claiborne
1994 - Insomnia
1995 - Rose Madder
1996 - The Green Mile
1996 - Desperation
1996 - The Regulators
1997 - The Dark Tower IV: Wizard and Glass
1998 - Bag of Bones
1999 - The Girl Who Loved Tom Gordon
2001 - Dreamcatcher
2001 - Black House
2002 - From a Buick 8
2003 - The Dark Tower V: Wolves of the Calla
2004 - The Dark Tower VI: Song of Susannah
2004 - The Dark Tower VII: The Dark Tower
2005 - The Colorado Kid
2006 - Cell
2006 - Lisey's Story
2007 - Blaze
2008 - Duma Key
2009 - Under the Dome
2011 - 11/22/63
2012 - The Dark Tower: The Wind Through the Keyhole
2013 - Joyland
2013 - Doctor Sleep
2014 - Mr. Mercedes
2014 - Revival
2015 - Finders Keepers
2016 - End of Watch
2017 - Gwendy's Button Box
2017 - Sleeping Beauties
2018 - The Outsider
2018 - Elevation
2019 - The Institute
2021 - Later
2021 - Billy Summers
```

## Best Practices for Consuming APIs

When dealing with API calls there are some things that is better to always keep in mind:

- First and foremost: always **use environment variables** to store API keys and other sensitive information. If you don't know how to use environment variables in Python remember that [there's a nice website that can help you with that](https://thepythoncorner.com/posts/2025-01-12-using-environment-variables-in-python/)... ;)
- Keep a look at the **rate limit**. Usually, there's a limit on how much an API can be called in a specific amount of time. Sometimes the API refuses to answer if the limit has been reached, and other times, there could be a cost for each call after the limit is reached. In both cases, **monitoring the usage** of the API is a good idea.
- **Keep a cache of the results you got**. Let's say that you have created a weather app. A user in Rome asks for the forecast and you ask for that to a third-party provider with an API call. If the same user after a few seconds asks again for the same information there is no need to make another API call to the provider, you just need to give back the same result. This is true also for a second user that asks for the same weather forecast a few moments after the first request. Caching your result can both improve the user experience avoiding the waste of resources. We already discussed this topic [in another article](https://thepythoncorner.com/posts/2018-04-26-how-to-make-your-code-faster-by-using-a-cache-in-python/).
- Remeber to **handle errors**. When you call a piece of software on internet, you simply cannot take for granted that the call will always succed. [Python Exception](https://thepythoncorner.com/posts/2017-01-10-working-with-exception-in-python/) are your best friends.
- Set **timeouts** for your requests to avoid hanging indefinitely. User experience is important.
- Always remember to **log your call**. Don't be crazy, [logging in Python](https://thepythoncorner.com/posts/2017-08-29-logging-in-python/) is always very important and become even more important when you have to manage a system that depends on external API calls.

## Working with Authenticated APIs

Many APIs require authentication to access their endpoints. There are several methods of authentication, including API keys, OAuth, and JWT tokens.

API keys are the simplest form of authentication. You usually pass the key as a query parameter or in the request header.

```python
URL = "https://yourservice.com/yourapi"
api_key = 'your_api_key'
headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get(URL, headers=headers)
print(response.json())
```

OAuth is a more secure method of authentication. It involves obtaining an access token and using it to make authenticated requests.

```python
import requests
from requests_oauthlib import OAuth1

URL = "https://yourservice.com/yourapi"

auth = OAuth1('your_client_key', 'your_client_secret', 'your_resource_owner_key', 'your_resource_owner_secret')
response = requests.get(URL, auth=auth)
print(response.json())
```

Another common method of authentication is by using a JWT token, which involves encoding user information into a token. This token is then used to authenticate API requests.

```python
import jwt
import datetime

URL = "https://yourservice.com/yourapi"

# Generate a JWT token
payload = {
    'user_id': 123,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
}
token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')

# Use the token to make an authenticated request
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(URL, headers=headers)
print(response.json())
```

Always refer to the API documentation to know how to authenticate against the specific API.

## Conclusion

Integrating third-party APIs into your Python projects can significantly enhance their functionality and efficiency. By following the steps outlined in this article, you can confidently make API calls and implement best practices to ensure your code is robust and maintainable. Remember to always handle exceptions gracefully, secure your API keys, and respect rate limits to avoid disruptions in service.

With these tools and techniques at your disposal, you're well-equipped to leverage the power of APIs in your future projects. 

Code well!

D.

