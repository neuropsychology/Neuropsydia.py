#<p align="center">Part 1.0: Getting Started</p>
**<p align="center">Dominique Makowski</p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-dev-brightred.svg) |
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
 
Tadaaaa, you've created your first neuropsydia-based program :wink:














---

#<p align="center">Part 1.1: Computerize a Questionnaire</p>
**<p align="center">Dominique Makowski</p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-dev-brightred.svg) |
|---------------|---|
| Length | ≈ 15min |


### Contact

For remarks, complaints, suggestions or anything else, please create an [issue](https://github.com/neuropsychology/Courses/issues).

## Intro

Now that you know all about [importing, starting and closing Neuropsydia](https://github.com/neuropsychology/Courses/blob/master/Programing/Python/Neuropsydia/1.0.Getting_Started.md), we can jump to one of its most useful function: computerizing questionnaires.
 
Questionnaires and scales are the most common measure used in psychological science. Unlike reaction times, which recording was quickly left to computers, scales and questionnaires are still mostly used in a paper-pen version.

*Why?* That might be because there is not much experiment editing softwares with which you can do questionnaires and scales easily (apart from the great [psychopy](http://www.psychopy.org/)).
 
But still, there are so much downsides in the use of paper-pen versions: you cannot have truly analog scales, the time consuming preprocessing of data etc. All these justify the use of computerized questionnaires and scales.
 
**And it's so easy to do using neuropsydia!**
 
Basically, `neuropsydia for research` has a function called `scale()` with which you can draw many different scales (including the *unbelievebly* famous LICKERT scale). This function allows you to draw individual scales, with questions and stuff. However, it takes several lines to do it, one for each scale of each question. And, **as we are proper programmers**, we don't like long and redundant code. That's why we will use a wrapper function called `questionnaire()` that will automate the creation of multiple scales and questions.
 
Let's go !

## A Minimmal Questionnaire
```python
import neuropsydia as n  # Load neuropsydia
 
n.start()
# Here goes my experiment code
n.close()
```
 
As you've seen it in the [previous tutorial](https://github.com/neuropsychology/Courses/blob/master/Programing/Python/Neuropsydia/1.0.Getting_Started.md), that's our minimal working program. Now, the actual experiment code will go between the `start()` and the `close()` functions. However, we can declare things before the start. For example, the number of trials, the length of the trials, etc. It is simpler to have all your variables easily available to tweeking at the beginning of a script than lost in the middle of the code.
 
**In this case, we will declare the questions.** And for that, we will use a python object called a `dictionary` (we will talk about python objects in the "basics of python" part). In fact, a nested dictionary, which might be a bit tricky to describe just now if you are a *python noob* :wink:. So let's just say that the function `questionnaire()` needs questions presented in the following structure:

```python
questions_dictionary = {
    "Item": {
        1: "Is Neuropsydia great?",
        2: "Is Neuropsydia not great?",
        3: "Is Python great?",
        4: "Is Python not great?"
 }
}
```
So here we have four questions associated with a key (the question number). On that object, we can use the `questionnaire()` function, to which we will feed that dictionnary.
 
**FULL CODE:**

```python
import neuropsydia as n  # Load neuropsydia
 
questions_dictionary = {
    "Item": {
        1: "Is Neuropsydia great?",
        2: "Is Neuropsydia not great?",
        3: "Is Python great?",
        4: "Is Python not great?"
 }
}
 
n.start()
n.questionnaire(questions_dictionary)
n.close()
```

Ok, try to run it!

<p align="center">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-questionaire_1.gif" height="700" alt="questinnaire computerize neuropsydia">
</a>
</p>











---

#<p align="center">Part 1.2: Complexify this Questionnaire</p>
**<p align="center">Dominique Makowski</p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-dev-brightred.svg) |
|---------------|---|
| Length | ≈ 15min |


### Contact

For remarks, complaints, suggestions or anything else, please create an [issue](https://github.com/neuropsychology/Courses/issues).


## Intro

This course is the direct following of the previous one on [how to create a more complex questionnaire using neuropsydia](https://github.com/neuropsychology/Courses/blob/master/Programing/Python/Neuropsydia/1.2.Complexify_Questionnaire.md). In this tutorial, we will see how to ask, store and include data about the participants, such as ID, age, gender. **This can be used in any experiments or tasks you create using neuropsydia**.

## Current Code Structure

So, currently, the structure of your questionnaire is the following:
1. defining main questions dictionary
    - defining the items
    - defining the reverse items
    - defining the dimensions
2. Run part
    - start neuropsydia
    - start questionnaire
    - close neuropsydia



```python
questions_dictionary = {

    "Item": {
        1: "Is Neuropsydia great?",
        2: "Is Neuropsydia not great?",
        3: "Is Python great?",
        4: "Is Python not great?"
    },
    "Reverse": {
        1: False,
        2: True,
        3: False,
        4: True
    },
    "Dimension": {
        1: "Neuropsydia",
        2: "Neuropsydia",
        3: "Python",
        4: "Python"
    }

}

n.start()
n.questionnaire(questions_dictionary,  # The questions
                anchors=["Not at all", "Absolutely"],  # The edges of the scale
                results_save=True,  # Should it save the data?
                results_type="csv2",  # Change the separator for ";" instead of "," (for France)
                dimensions_mean=True,  # Compute the mean by dimension?
                analog=False,  # Lickert-like
                edges=[0, 7],  # Values underneath
                style="blue",  # The cursor's colour
                randomize=True,  # Randomize the question's order
                instructions_text="Here are the instructions")  # Add instructions at the beginning
n.close()
```

<p align="center">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-questionaire_2.gif" height="700" alt="questinnaire computerize neuropsydia">
</a>
</p>








---

#<p align="center">Part 1.3: Include Info about the Participant</p>
**<p align="center">Dominique Makowski</p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-dev-brightred.svg) |
|---------------|---|
| Length | ≈ 15min |


### Contact

For remarks, complaints, suggestions or anything else, please create an [issue](https://github.com/neuropsychology/Courses/issues).


This course is the direct following of the previous one on [how to create a more complex questionnaire using neuropsydia](https://github.com/neuropsychology/Courses/blob/master/Programing/Python/Neuropsydia/1.2.Complexify_Questionnaire.md). In this tutorial, we will see how to ask, store and include data about the participants, such as ID, age or gender. **This can be used in any experiments or tasks you create using neuropsydia**.

## Current Code Structure

So, currently, the structure of your questionnaire is the following:
```
1. defining main questions dictionary
    1.1 defining the items
    1.2 defining the reverse items
    1.3 defining the dimensions
    
2. Run part
    2.1 start neuropsydia
    2.2 start questionnaire
    2.3 close neuropsydia
```
So, where should we include the part where we will ask for infos?

UNFINISHED.


```python
import neuropsydia as n

questions_dictionary = {

    "Item": {
        1: "Is Neuropsydia great?",
        2: "Is Neuropsydia not great?",
        3: "Is Python great?",
        4: "Is Python not great?"
    },
    "Reverse": {
        1: False,
        2: True,
        3: False,
        4: True
    },
    "Dimension": {
        1: "Neuropsydia",
        2: "Neuropsydia",
        3: "Python",
        4: "Python"
    }

}

n.start()
n.questionnaire(questions_dictionary,  # The questions
                anchors=["Not at all", "Absolutely"],  # The edges of the scale
                results_save=True,  # Should it save the data?
                results_type="csv2",  # Change the separator for ";" instead of "," (for France)
                dimensions_mean=True,  # Compute the mean by dimension?
                analog=False,  # Lickert-like
                edges=[0, 7],  # Values underneath
                style="blue",  # The cursor's colour
                randomize=True)  # Randomize the question's order
n.close()

```

<p align="center">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-questionaire_2.gif" height="700" alt="questinnaire computerize neuropsydia">
</a>
</p>
