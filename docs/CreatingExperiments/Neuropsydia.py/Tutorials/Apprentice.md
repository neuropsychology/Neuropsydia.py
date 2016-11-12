#<p align="center">Creating Experiments with Python and Neuropsydia</p>
##<p align="center">Part 2.1: Structuring your Code</p>
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



## General Principles

There are actually many ways to do it. Each person has its coding style. Here, and throughout all tutorials, we will strive to write a clear, neat, organized, structured, and reproducible code. Basically, we won't write 1000 linear lines of procedure, we will rather create several **blocks** of code which we will then assemble. 

A code lacking structure is called *spaguettti* code. When beginning with programming, you usually end up writing this kind of code anyway. Later on, you learn to structure it.

And remember, **a clear code is a clear thought**: you can then make adjustment and correct bugs much more easily.

To take an abstract example, imagine an experiment when we present images in two conditions, "negative" and "positive", and ask the participants to rate each image on a scale of Fear, Anger and Joy. You experiment code might look like this:
```python
condition="negative"
image("negative1.png")
ask("Fear?")
ask("Anger?")
ask("Joy?")

condition="positive"
image("positive1.png")
ask("Fear?")
ask("Anger?")
ask("Joy?")

condition="negative"
image("negative2.png")
ask("Fear?")
ask("Anger?")
ask("Joy?")

condition="positive"
image("positive2.png")
ask("Fear?")
ask("Anger?")
ask("Joy?")

...
```

If you have like 100 trials, your code will start becomming quite indigest. What can we do to make it more neat? First, we see that the three `ask()` functions are very redundant. a first step would be to regroup in a unique function that we will define at the beginning and call `evaluation`. 
```python
def evaluation():
    ask("Fear?")
    ask("Anger?")
    ask("Joy?")
```
The rest of the code would then look like this:
```python
condition="negative"
image("negative1.png")
evaluation()

condition="positive"
image("positive1.png")
evaluation()

condition="negative"
image("negative2.png")
evaluation()

condition="positive"
image("positive2.png")
evaluation()

...
```
