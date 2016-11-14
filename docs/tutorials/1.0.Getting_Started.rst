<p align="center">Part 1.1: Getting Started</p>
**<p align="center">Dominique Makowski</p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-open-brightgreen.svg) |
|---------------|---|
| Length | ≈ 15min |


This course was crafted by psychologists, neuropsychologists and neuroscientists for psychologists, neuropsychologists and neuroscientists.
As such, it is a straightforward introduction to Neuropsydia for Python with a special focus on how to actually do something with it.
It is not a programming course on Python, nor a course on programming *per se*.

### Contact

For remarks, complaints, suggestions or anything else, please create an [issue](https://github.com/neuropsychology/Courses/issues).

## Installation

- Windows
  - 1. If you don't have any python distribution installed, download [winpython](https://winpython.github.io/) (version 3.5, without `Qt5` at the end). Choose a 32bits or 64bits version (choose 32bits if you're not sure, it works everywhere)
  - 2. Install winpython somewhere (for example your desktop)
  - 3. Within the winpython folder, find and open `WinPython Command Prompt.exe`
  - 4. Paste the following line and press enter: `pip install https://github.com/neuropsychology/Neuropsydia.py/zipball/master`
  - 5. Wait until the end of the download

## Hands on!

**Well, first of all, welcome and thank you for trying the Python version of [neuropsydia for research](https://github.com/neuropsychology/neuropsychology.R). I'm sure you will like it as, while still in developpment, it already has some powerful functions that will help you create your tasks and experiments and much more.**
 
But enough talking! After the [installation](https://github.com/neuropsychology/Neuropsydia.py#installation) of the neuropsydia package, open your python code editor (*e.g.,* [spyder](https://pythonhosted.org/spyder/installation.html), available within the [WinPython](https://winpython.github.io/) bundle).
 
Here, you will write functions that will almost magically come to live once the program is launched. It basically works like a text editor (such as notepad), except that it automatically highlights python functions and cares about indentation.
```
this
    is
        indentation
```
In spyder, one pane is the **CONSOLE**, where Python actually lives. It's its interface with us humans. If you type something in there, it will swallow it, do something with it, and then, maybe, return something. Also, it's great for calculus. For example, try typing `5*2` and hit Enter.
 
*Pretty cool, huh?*
 
**But for now, let's focus on some simple things, such as how to load, start and close neuropsydia.**
 
 
## Import Neuropsydia
 
Neuropsydia for research is a module which, like any other module, must be loaded in order to be used. In Python, we load modules by running:
```python
import themoduleiwanttoload
```
Then, we can use its functions:

```python
themoduleiwanttoload.function1()
themoduleiwanttoload.function2()
```
However, as you can see it, it's pretty anoying to write the full name of the module each time we use one of its function. Fortunately for us, Python allows us to load a module under another name (or `alias`), for example the letter "x".
```python
import themoduleiwanttoload as x
x.function1()
x.function2()
```
*Better*. That's what we are going to do with neuropsydia, loading it under the name "n".
 
**However, unlike many other packages, Neuropsydia CANNOT be loaded without two of its function, start() and close().**
 
 
 
## Start and Close
 
So, when importing `neuropsydia`, what happens is basically that it needs to initialize several things before being ready to use. And those things are initialized with the `start()` function. Moreover, adding the `close()` function at the end will ensure a clean ending.
 
**Therefore, every experiments, after loading the neuropsydia module, will begin by the `start()` function and end with the `close()` function.**
 
Let's try it. Write in the editor the following lines of code:

```python
import neuropsydia as n
 
n.start()
n.close()
``` 
 
 
## Execute your code
 
The rest of your code will go between the `start()` and the `close()` functions. But these 3 lines are a minimal working program, so let's try it.
 
To execute an entire python program, **always open a new python console** (in spyder, go to console, then click on `open a new python console`, then press F5, - or the green arrow).
 
**Do it.**
 
...
 
Tadaaaa, *voilà*, you've created your first neuropsydia-based program :wink:
