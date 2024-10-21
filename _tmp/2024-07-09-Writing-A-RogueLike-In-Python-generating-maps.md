---
title: "Writing a Roguelike in Python: chapter 1 - generating Maps"
date: 2024-07-09T01:35:00+01:00 
author: Davide Mastromatteo
excerpt: "Writing a Roguelike with Python. This is the first chapter of a series that I hope I will be able to finish... sooner or later... Let's start generating maps!"
header:
    teaser: https://imgs.xkcd.com/comics/game_ais.png
categories:
    - Dev
tags:
    - python
    - videogames
    - rogue
    - roguelike
---

![Game AIs](https://imgs.xkcd.com/comics/game_ais.png)

I think it was 1996. I was more or less 18 years old and one of my best friends, Paolo, came to me holding a floppy disk in his hand (yes, we’re that old...)

P - "Azer" (don’t bother to understand that, consider it as a greeting... :) )
D - "hey, what’s up?"
P - "I brought you the best game ever!"
D - "... where it is?"
P - "Here, in this floppy disk"
D - "What? How can a modern game fit in that stuff?"
P - "I've said that's the best game ever... I haven't said it's a *modern* game... however, in 1980 they used to write games that could fit in 1.44MB”
D - "1980? Are you serious?"
P - "Trust me! It’s the best ever!"

I took the floppy, a simple black floppy with a red lettering that read "ROGUE"...

## Roguelike for dummies

Raise your hands if you don't know what a roguelike is.
Now if you have your hands up, please leave this site now!
No no, I'm just kidding... :) I'll gave you a brief explanation about that.
They're turn based games that usually consist in a character that has to descend into a multi layer dungeon to accomplish a mission and then has to come back up exiting the dungeon.
Obviously the dangeon is full of enemies that want to kill you... and if they kill you, you loose and have to start again with a new try. You have just one try, just one life.
Levels are generated randomly and this is the most fun part becasue almost every game you'll play will be completely different from every game you played, in an infinite loop of fun.

Nowadays roguelike games have some graphic, usually something simple, but in the old days you just have console graphic, so your hero was a simple "@" character, a Vampire was a simple "V" character and so on...
Actually, the best graphic of the world, the one you can create with your imagination.

## The project plan

Ok, let's be clear: I don't know anything about how to write a good roguelike and a good idea would be looking online for resources and other stuff on how to create a good roguelike but... 
hey, there's more fun in trying to do that than in studying how to do that, right?

Let's start.

What would I need? 


