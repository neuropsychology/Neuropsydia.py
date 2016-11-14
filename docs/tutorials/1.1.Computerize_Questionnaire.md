#<p align="center">Creating Experiments with Python and Neuropsydia</p>
##<p align="center">Part 1.1: Computerize a Questionnaire</p>
**<p align="center">Dominique Makowski</p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-open-brightgreen.svg) |
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

