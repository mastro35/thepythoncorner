---
title: "Representing geographic data in Python - feat. Coronavirus"
date: 2020-03-02T00:18:49+01:00
author: Davide Mastromatteo
excerpt: "In this tutorial, you will learn how to represent geographic  data in Python using Jupiter Notebook and folium"
header:
  teaser: https://imgs.xkcd.com/comics/colds.png
categories:
  - Dev
tags:
  - geographic
  - maps
  - jupiter notebook
  - folium
  - kaggle
  - coronavirus
  - python
redirect_from:
  - 
---
![teaser](https://imgs.xkcd.com/comics/colds.png)
As you may know, I live in Italy, a beautiful country made famous by style, fashion, and food. But in the last days, we've become famous also for something a little less cool: the [Coronavirus](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_outbreak).

At the end of February, in fact, we have become overnight the third country with more infections in the world, after China and South Korea. And Milan (the city I live in) is one of the most affected Italian cities.

As this disease started to spread, everyone in town was like obsessed with the [contagious map](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) an interactive map that let you track the disease in the world. 
And I was as well obsessed with this map, not for the contagious, not for the coronavirus, but because I wanted to know... how to create a map like this in Python!

It turns out that it's easier than you think with the right tools. 

The first tool we will need is [Folium](https://python-visualization.github.io/folium/). Folium is a package that makes super easy to get a map like that with the data you want. You just need to create the object and place your data in the map specifying latitude, longitude and the data you need.

For this example, I will use [Jupiter Notebooks](https://jupyter.org/). 
According to the official site:

> The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

It's somehow similar to a playground for Python, which also supports some markdown and other useful stuff. Once you have developed a notebook there are a lot of sites that offer you hosting of your notebooks almost for free. One of the most famous is [Google Colab](https://colab.research.google.com/).

So let's recap: 
* google Colab
* folium
* Jupiter Notebooks
* Python

Am I missing something to create my interactive map?
Oh, sure... data! I need some data to plot.
And when you need data a good place to start is [kaggle](https://www.kaggle.com/). 

Kaggle is a site that allows you to download a lot of datasets for any kind of use. Weather, Virus, Hotel booking ... there's plenty of topics to choose from and there are data for any kind of use. 
Brief research on Kaggle brings me to [this dataset from Vignesh Coumarane](https://www.kaggle.com/vignesh1694/covid19-coronavirus). 
I don't know if the data are accurate or not... but who cares, I don't need precise data, I just need something to create an interactive map, right? 

Now, to use Kaggle data you have to register (for free) to Kaggle and create an API Token. 
From the [official docs of Kaggle](https://www.kaggle.com/docs/api):

> To use the Kaggle’s public API, you must first authenticate using an API token. From the site header, click on your user profile picture, then on "My Account" from the dropdown menu. This will take you to your account settings at https://www.kaggle.com/account. Scroll down to the section of the page labeled API:
> To create a new token, click on the "Create New API Token" button. This will download a fresh authentication token onto your machine.

Is everything clear?
So, let's start!

Let's go to google colab and create a new Jupiter Notebook. 
For the first block we have to import some stuff:

```python
# import some stuff
import folium
import pandas as pd
import os
import json
```

then we have to set up two variables that will keep our Kaggle username and our Kaggle API KEY:

```python
# set kaggle username and API token
USERNAME="YOUR USERNAME GOES HERE"
KEY="YOUR KEY GOES HERE"
```

then we will need to create a JSON file with this information under `~/.kaggle/kaggle.json`

```python
# pack everything into a json file
!mkdir ~/.kaggle
!mkdir /content/.kaggle

token = {"username":USERNAME,"key":KEY} 
with open('/content/.kaggle/kaggle.json', 'w') as file:
    json.dump(token, file)

!cp /content/.kaggle/kaggle.json ~/.kaggle/kaggle.json
```

Ok. We're ready to authenticate against Kaggle now

```python
# let's authenticate on kaggle
api=KaggleApi()
from kaggle.api.kaggle_api_extended import KaggleApi
api.authenticate()
```

Ok, now that we're in, we need to download the dataset. We can still use the api of kaggle for that:

```python
# download the data we need
dataset_name="vignesh1694/covid19-coronavirus"
filename="time_series_19-covid-Confirmed.csv"
api.dataset_download_file(dataset_name, filename)
```

and now that we have downloaded the file, we can read this CSV and plot the data to the map. Let's start by creating a Panda data frame with the data we need:

```python
# create a Panda data frame with the data
df=pd.read_csv(filename)
```

Cool. Now if you examine the dataset you will see that the "Province/State" field is populated just for Chinese regions. Let's create a new "name" field that contains the "Province/State" when indicated and the "Country/Region" field otherwise.

```python
# transform your dataset to coalesce the Province/State and the Country/Region
df['name']=df['Province/State'].mask(pd.isnull, df['Country/Region'])
```

Now the cool stuff. Let's create a map with folium:

```python
# create an empty map
map = folium.Map(zoom_start=1.5,width=1000,height=750,location=[0,0], tiles = 'Stamen Toner')
```

And now start to loop on your data frame to add all the rows with confirmed cases on your map. 
As you can see you just need to create a CircleMarker object specifying the location, the radius of the point and the color:

```python
# loop on your date to populate the map
for row in df.itertuples():
    lat=getattr(row, "Lat")
    long=getattr(row, "Long")
    confirmed=int(row[-2])
    name=getattr(row, "name")
    tooltip = f"{name} - {confirmed}"
    radius = 30 if confirmed/10>30 else confirmed/10

    if confirmed>0:
        folium.vector_layers.CircleMarker(
            location=(lat, long),
            radius=radius,
            tooltip=tooltip,
            color='red',
            fill_color='red'
        ).add_to(map)
```

and now your map is ready to be shown:

```python
# output the map
map
```

Et voilà:

![map](https://mastro35.github.io/thepythoncorner/images/map.png)

Oh my God... 888 cases right now in Italy! ... it's time to go now!

Bye  
D.