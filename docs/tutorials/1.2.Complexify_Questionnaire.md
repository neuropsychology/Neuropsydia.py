#<p align="center">Creating Experiments with Python and Neuropsydia</p>
##<p align="center">Part 1.2: Complexify this Questionnaire</p>
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
