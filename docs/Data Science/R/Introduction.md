#<p align="center"> Statistics for Psychologists with R: An Introduction </p>
**<p align="center"> Dominique Makowski </p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-open-brightgreen.svg) |
|---------------|---|
| Length | ≈ 45min |


This course was crafted by psychologists, neuropsychologists and neuroscientists for psychologists, neuropsychologists and neuroscientists.
As such, it is a straightforward introduction to R with a special focus on how to get some actual results with it.
It is not a programming course on R, nor a course on statistics *per se*.

Note that there are other more complete tutorials teaching R for psychological research (such as [this one](http://personality-project.org/r/) or [my favourite one](https://drive.google.com/file/d/0B4udF24Yxab0S1hnZlBBTmgzM3M/view
)).

### Contact

For remarks, complaints, suggestions or anything else, please create an [issue](https://github.com/neuropsychology/Courses/issues).


### Outline

Add the end of this course, you will:

- [x] Know a bit of the philosophy and history behind R
- [x] Use R for simple operations
- [x] Read your data file with R
- [x] Explore your data
- [x] Subset your data
- [x] Run a correlation analysis
- [x] Run a t-test
- [x] Draw some basic plots
- [x] Run an analysis of variance (ANOVA)
- [x] Run a multiple linear regression
- [x] Install and use packages


And, most importantly...

- [x] You won't be afraid of R or statistics anymore :muscle:

## About <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Rlogo.png/64px-Rlogo.png" height="40">

### Personal Experience

I spent all my bachelor years with a mixed feeling toward statistics. Although I understood their importance for psychological science, I was just completely lost when following the classes. 
I spent like three years learning theoretical stuff about the history of t-testing and, again, even if I realise its importance *now*, it just wasn't the right moment to teach that to students. 
Then, shortly after, we learn how to get some results with Statistica, by clicking here and there, and looking for the highlighted text that indicates that you're [lucky enough to have a significant effect](https://www.youtube.com/watch?v=5OL1RqHrZQ8). 
I applied the methods and passed the exams, with no interest or understanding of statistics whatsoever. 

All that until my master thesis, about neuroaesthetics, where I gathered data from children and adults and I became eager to discover the results. 
Somehow, I knew what I wanted to do: check the link between those two variables, check if there's a difference in that variable between my group ages etc. But to do it with a software like Statistica was a pain in the *bottom*, to say it nicely. 
I somehow managed to do it, and the year after that, I discovered R. 

Interested by the possibility of automating statistical reports, creating pdfs with figures, results and all, being able to re-run an analysis from the start as many times as I wanted, I started to learn. 
Beside the unlimited resources available from the Internet, I was alone and nobody in my lab' was using it at that time. The learning curve was steep, indeed, I was now lacking the theoretical notions that were taught to me years ago. 
I eventually managed to get through, and it's been now a couple of years since I use R on a daily basis...
Long story short, I do now love statistics.

And that is, thanks to R.

*Disclaimer: I am not a statistican nor a programmer, just an interested user.* 

### The Myth

- R is complicated
- It is hard to do simple things
- You need to know programming and coding
- You need to be an statistics expert

### Why R

- [x] 100% Free
- [x] Open-source 
- [x] Cross-platform Compatibility (Windows, MacOS, Linux...)
- [x] Huge support and community 
- [x] Gold standard across science
- [x] Reproducible research
- [x] Cutting-edge statistics and methods
- [x] Powerful data visualisation
- [x] Data safe

### Think different

R will require from you to think differently. Especially if you're used to software like STATISTICA, SPSS or SAS. 
But it's for the best. 

- It will require and develop a deep knowledge of your data
- Think in terms of "objects": everything in R is an object; a dataframe, a function, a result, a statistical model etc. An object is basically just a container of information.

The syntax in R is quite consistent. 
You apply a function on an object. 
This function returns something that you can store in another object.
```R
  object2 <- function(object1)
```


## Installation

You'll need two things: the language (R) and an editor (RStudio) with which you will communicate with R.

- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Rlogo.png/64px-Rlogo.png" height="22">

Download and install R for [MacOS](https://cran.r-project.org/bin/macosx/), [Windows](https://cran.r-project.org/bin/windows/) or [Linux](https://cran.r-project.org/bin/linux/).

- <img src="https://www.rstudio.com/wp-content/uploads/2014/03/blue-250.png" height="22">

Click on [this link](https://www.rstudio.com/products/rstudio/download3/) and then on the Download green button of RStudio Desktop (Free Licence). Then, choose your platform (Windows, MacOS or Linux).


## Let's go!

### First steps

#### Initialisation

Create a folder where you will store your project (the data, scripts, plots...). 
Usually you would place your data in this folder. 
For this training, we will use the "personality" dataset available within the neuropsychology package. 
So right click on [this link](https://raw.githubusercontent.com/neuropsychology/neuropsychology.R/master/data/personality.csv) and select "save the link under" to download the dataset, which ends with .csv. 
This format (.csv for comma separated values) is a standard light format used in statistics. 
You can open those files with almost any software (including Excel, Statistica, etc.)

1. Once you have a folder (that you can name "Rcourse" for example), and the file personality.csv in it,
2. Open RStudio. Click on `file -> new file -> R script`. Then click on `save as`, navigate to your project directory and save it there, with the personality.csv file.
3. So now we have a project directory with, in it, a data file and the statistic script.

However, we still have to tell R that this is the project directory we will be working in, and that when we say "read the file personality.csv", R will find it there.

So, each time you open RStudio, don't forget to do the following: 

- **click on Session -> Set Working Directory -> To Source File location**.

What does it mean? 
That the working directory (where R will look for files and save things if asked to) is to be where the script (the source file) is.

#### RStudio

Let's take a look at what we have now. A classic RStudio window is organized in 4 different panels:

- **Script**: nothing more than a text editor where we will write and save our code. 
- **Console**: here lives the language R, where we can communicate with it.
- **Environment**: a panel that will display the different variables, dataframes (which are all "objects") that we will create.
- **Plots and Help**: a panel that will display the plots or the help for functions.
 
You want to communicate with R? 
Type `3+5` into the console and press ENTER. 
See the result? It's magical. 
But from now on, we want to save the code we will create, so we won't type it directly in the console but in the script panel, that we can run and re-run every time we want.


### Our First Object: `df`

`df` is a convention name for **dataframe**, which is the classic format of statistical data. 
Is is organised into *variables*, the columns, that are named, and *observations*, the rows, that often are, in psychological science, participants.

We want to read the csv and to store it in an object that we will call `df`. In the script panel, write the following:

```R
df <- read.csv("personality.csv")
```
**NOTE: use `read.csv(...)` for non-European files and `read.csv2(...)` for some European files (French or German for example): the difference lies in the format, the former use a dot separation for decimals (`3.12`) and the latter use a comma (`3,12`)**

Then, execute this line of code by clicking on it and pressing CTRL + ENTER.

*So, what happened here?*

When you executed that line, it pasted it from the script into the console. 
Then, it applied the function `read.csv()` on the name "personality.csv" (it knows it is a name thanks to the quotes). 
It looked for a file of that name in the *working directory*, defined above, which is our project directory, found the file, read it, and returned a dataframe that we stored into an object called df (we could have called it differently, it doesn't matter).

If you look into the environment panel, you'll see that a line just appeared that says "df    1327 obs. of 20 variables".
Indeed, the personality dataset consists of 1327 participants (rows/observations) and 20 variables (columns/variables). 

**NOTE: R is case-sensitive, meaning that it matters whether it is upper or lowercase. If you type rEad.csv or "persoNality.csv", it won't work. This is the cause of many errors when beginning**

But we would like to *actually* see it, right? 
See what variables there are etc. 
We can do it like that:

- Click on the small table-like button on the right of "df    1327 obs. of 20 variables". It will open a new tab where we can visualize the dataframe.

|Sex |      Age| Salary| Study_Level|Mood_Disorder |      BMI|Meditation |Sport |Music | Extraversion| Empathy.Agreeableness| Conscientiousness| Instability.Neuroticism| Openness_to_Experience.Intellect| Honesty.Humility| Disinhibition| Detachment| Psychoticism| Negative_Affect| Antagonism|
|:---|--------:|------:|-----------:|:-------------|--------:|:----------|:-----|:-----|------------:|---------------------:|-----------------:|-----------------------:|--------------------------------:|----------------:|-------------:|----------:|------------:|---------------:|----------:|
|F   | 25.03818|      2|           6|Absence       | 22.64738|No         |No    |No    |         4.75|                  3.50|              2.25|                    4.75|                             3.75|             1.00|           5.8|        2.8|          4.0|             6.2|        4.6|
|M   | 25.87324|      3|           6|Absence       | 21.91381|No         |Yes   |Yes   |         3.25|                  3.50|              2.25|                    2.00|                             4.00|             4.75|           2.0|        2.2|          1.4|             2.4|        2.6|
|F   | 22.19897|      0|           5|Absence       | 23.05175|Yes        |Yes   |No    |         5.50|                  6.50|              3.75|                    3.25|                             6.00|             7.00|           3.2|        1.0|          2.6|             2.2|        1.4|
|F   | 27.25862|      2|           6|Absence       | 18.61150|No         |No    |No    |         5.00|                  4.75|              0.75|                    3.50|                             5.25|             7.00|           4.8|        0.2|          0.2|             1.6|        2.8|
|F   | 49.02227|      3|           6|Absence       | 21.23057|No         |Yes   |Yes   |         2.75|                  6.25|              2.25|                    2.00|                             4.50|             7.00|           1.0|        2.4|          2.6|             2.0|        2.0|

- We can also ask for a summary. To do it, add the following line in your script and execute it (CTRL + ENTER):
```R
summary(df)
```

It will print, in the console, a summary of all the variables (note that there are better summary-like functions available from different packages, such as `describe()` from the `psych` package, but let's stick with the base functions for now).


### Accessing Variables

So, we have one object, called `"df"`, that is a dataframe, that itself contains 1327 rows and 20 *named* variables. 
We can access each variable using the `$` sign, which roughly means "in". For example, execute the following line:
```R
df$Age
```
It will print, in the console, the variable "Age" that is stored *in* the object df. 
Again, we can use the function we used above, `summary()`, but this unique variable. Run the following line:

```R
summary(df$Age)
```


We can also ask specifically for the mean or the standard deviation (SD):

```R
mean(df$Age)
sd(df$Age)
```

### Variable Type

Now try applying the `mean()` function on the Sex variable "`mean(df$Sex)`". 
What happened? R throws an error message. 
Indeed, Sex is not a **numeric variable**, but a **factor**. 
And the mean of a factor does not make much sense.

It should also throw an error if we apply the function `mean()` on the Study_Level variable, which is a factor with 7 levels (coded from 0 to 7, 0 corresponding to primary school and 7 corresponding to a doctorate degree). 

As you can see, R sees no problem and returns us a mean. Why? 
Because it thinks that it is a numeric variable (In its defence, we must admit that it looks very much like it, with all the levels being numeric). 
Same goes for the Salary variable.

**So before doing any analysis, make sure to check the type of your variables and convert them when necessary**.

We can convert a variable by using the `as.factor()` command (and `as.numeric()` in the reverse case). 
If we simply run `as.factor(df$Study_Level)`, it will print the variable. 
However, if you do, again, a summary of this variable, you'll see that R keeps considering it as a numeric variable. 
Why? Because we must **replace** the variable from the dataframe by the transformed one.

So, the right way to go is to run the following:
```R
df$Study_Level <- as.factor(df$Study_Level)
df$Salary <- as.factor(df$Salary)
```

Once our variables are correctly stored with the right type, let's jump to the next section.

## Let's do some proper statistics

### Individual Correlations

Correlations are one of the most popular statistical procedure in psychological science. 
To run a correlation test between the Age of the participant and the Negative Affect personality trait (the tendency to experience negative emotions such as sadness, anger, fear or anxiety), simply run the following:

```R
cor.test(df$Age, Negative_Affect)
```

Nice, you've run your first statistical test! :smile:

**Once you'll be used to it, doing statistics with R will be way quicker than with any other software.**


The output is the following:

```
	Pearson's product-moment correlation

data:  df$Age and df$Negative_Affect
t = -7.3625, df = 1300, p-value = 3.193e-13
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 -0.2516608 -0.1473437
sample estimates:
       cor 
-0.2000692 
```

It gives you all the important info: the estimated coefficient r (-0.057...), the *p* value, the 95% CI and the degrees of freedom.

It reveals that the correlation between Age and Negative Affect is significantly negative and moderate, meaning that the tendency to experience negative emotions diminishes when Age increases.

### t-tests

When comparing two groups, another popular procedure is the t-test.
Let's compare the men and the women on the Negative Affect variable by running the following:

```R
t.test(df$Negative_Affect ~ df$Sex)
```

Wait, what is that `~` sign? It basically means "by". "I want the statistics on Negative Affect by Sex".

Let's take a look at the output:

```
	Welch Two Sample t-test

data:  df$Negative_Affect by df$Sex
t = 7.152, df = 430.61, p-value = 3.697e-12
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 0.4974571 0.8744882
sample estimates:
mean in group F mean in group M 
       3.475024        2.789051  
```

Ok, so in general, women appear to have a higher level of negative affect. But wait, it says we did a Welsh t-test! Usually, people don't do a Welsh test but assumes that the two samples are of equal variance... Let's take a look at the documentation of the variable by running the following:

```R
?t.test()
```

This will show the documentation for the function. 
Indeed, in R, **almost every function is documented**.

In the documentation of this function, under the *Arguments* section, we find the following:

```
a logical variable indicating whether to treat the two variances as being equal. If TRUE then the pooled variance is used to estimate the variance otherwise the Welch (or Satterthwaite) approximation to the degrees of freedom is used.
```

It corresponds to the `var.equal` argument. In the Usage section, it is indicated that the default value for this argument is `FALSE`.
We can change it with the following:

```R
t.test(df$Negative_Affect ~ df$Sex, var.equal=TRUE)
```
Due to the large sample, the result did not differ that much. The output shows that the level of negative affect is still significantly higher in women than in men.

in R, all functions have arguments. You can display the documentation by typing `?yourfunction()` to have more info about the arguments and their defaults.


### Ugly box plots

Instead of t-testing the differences between the two groups, we can also plot it with the function... `plot()`. Let's run the following:

```R
plot(df$Negative_Affect ~ df$Sex)
```

For a course on plotting, see [this](https://github.com/neuropsychology/Courses/blob/master/Statistics/R/English/Plotting%20with%20ggplot2.md) tutorial.


### Subsetting

We have to be careful. Our results about the Sex difference on Negative Affect could be biased by another variable, namely the presence of a mood disorder.
Indeed, as their prevalence is higher in women, it could bias the results by boosting the level of Negative Affect in women.

How to remove all the people that reported suffering from a mood disorder?
First let's see how this variable is organised.

```R
summary(df$Mood_Disorder)
```

**NOTE: if you don't remember the exact name of a variable, you can list all your variables by executing the command `names(df)`.**

It is a factor with two levels, "Presence" and "Absence". We want to keep only the subset of people that have `Mood_Disorder` equal to "Absence". We do it with the following:

```R
df <- subset(df, Mood_Disorder=="Absence")
```
Ok, so what it means is that we want a subset of "df" (our dataframe), in which the variable Mood_Disorder equals to "Absence". 
Why two equals sign? Because, to put it simply, it is not a statement that says "this equals this", but rather an evaluation ("when this equals to that, then it is true"). 
Other operators are ">", "<", "<=", ">=" and "!=" (for "not equal").

So now we have a dataframe with only the people that did not report suffering from a mood disorder. 
But wait... *we've overwrite our data!* 
Indeed, we replaced the original object df with the new subset.

**No worries, R is completely data safe. It never works directly on the data file. Unless you explicitly ask him to save something, it will never modify the external files.**
So we can simply run the code again, from the beginning, whenever we want, to reload the original dataframe and do all these steps over again.


## Let's finish with some more complex stuff

It is a lie. In R, many complex algorithms and statistical procedures are as simply to run as a correlation. Your job is then to know if you applied the right method, and to correctly interpret the output.

### ANOVAs & post-hocs

The third widely used procedure is the Analysis Of Variance (aov), which we will use to see if there is an interaction between the Sex and the presence of Mood Disorder.
Therefore, we want to avoid the line of our script where we do the subsetting. 
However, we don't need to remove it, we can simply *comment* it by adding a "#" at the beginning of the line (or by pressing CTRL + SHIFT + C). 

**A useful feature is that we can keep lines of code, or some comments about each line, to remember what we did, that will not be ran when the code is executed.**

After having commented that subsetting line, rerun your script from the beginning (by clicking on the run button or by selecting all the script and pressing CTRL + ENTER). It should do, again, all the things we did, without the subsetting, resulting in a dataframe of 1327 observations.


Then, we will do a analysis of variance with the `aov()` function, and place the results in an object that we can call... "results".

```R
results <- aov(df$Negative_Affect ~ df$Sex * df$Mood_Disorder)
```

This formula means that we want to explain/predict the Negative Affect (our *outcome variable*) with Sex, Mood Disorder **and** the interaction between the two predictors. If you don't want to include the interaction, replace the **" * "** by a **" + "**.

For more clarity, we can pass the dataframe `df` as an argument, thus specifying it only once, as follows:

```R
results <- aov(Negative_Affect ~ Sex * Mood_Disorder, data=df)
```
If we run this line, nothing happens, but a second object, called results, is created in the environment panel. We can visualize this result with the `summary()` function.
```R
summary(results)
```

This will return the analysis of variance table.

```
                    Df Sum Sq Mean Sq F value   Pr(>F)    
Sex                  1  102.3  102.31  52.595 6.95e-13 ***
Mood_Disorder        1  116.4  116.40  59.839 2.03e-14 ***
Sex:Mood_Disorder    1    3.8    3.76   1.931    0.165    
Residuals         1323 2573.6    1.95                     
---
Signif. codes:  0 *** 0.001 ** 0.01 * 0.05 . 0.1   1
```

The two predictors have a significant effect on the outcome variable, but their interaction is not significant. To take a look at the multiple comparisons (posthocs analysis), use the `TukeyHSD()` function:

```R
TukeyHSD(results)
```

### Linear Modeling

In fact, the correlation, the t-tests and the ANOVA we did are all a part of the same framework: linear modelling. 
Correlation is fitting a linear model with two (scaled and centred) numeric variables. 
A t-test is a linear model with a numeric variable as the outcome variable and one factor with two levels as the predictor, and an ANOVA/MANOVA focuses on the effect of categorical predictors (factors).

**Fitting linear models is a general procedure that withholds all the information, and that could replace the use of t-tests, ANOVAs and correlations, if only we psychologists were used to read its output.**

Fitting a linear model is the same as running an ANOVA. Let's do it and store its output in an object we call "fit" (also a conventional name for a model we fitted), and inspect the results with the `summary()` function.

```R
fit <- lm(Negative_Affect ~ Sex * Mood_Disorder, data=df)
summary(fit)
```

That generates a lot of information, which I will not explain in details in the present course (see the [not available yet] course on hierarchical mixed-effects models).


### Linear Models vs. ANOVAs, t-tests and correlations

Not convinced by the fact that a linear model is the general framework all of these other procedures work on?
Let's do an analysis of variance on the linear model fitted above and compare it with the analysis of variance table obtained with the `aov()` function.

```R
anova(fit)
```

Yes, it's pretty much the same. To put it simply, the `aov()` function works as a wrapper function that does an ANOVA on a linear model). 

Now fit a linear model with Sex as the only predictor and compare it with the result of a t-test:
```R
fit <- lm(Negative_Affect ~ Sex, data=df)
summary(fit)
t.test(Negative_Affect~Sex, data=df, var.equal=TRUE)
```
As you can see, the p value is the same. 
Even more interesting, if you subtract the two means (the men's mean from the women's mean) displayed in the t-test output, it will give you... the value of the &#946; (the "beta", the slope), displayed under "Estimate" in the linear model output. 
But still, if you're really rigid and tenacious, you might argue that the `t.test()` function gives us the confidence interval for the estimate that the `lm()` does not provide...

```R
confint(fit)
```
There you go :wink:


As for the correlation, it will be the occasion to introduce another useful function, `scale()`, that scales and/or center your variable (or your whole dataframe). Let's say we want to add in our dataframe two variables, the Z score of the Age, and the Z score of the Negative Affect. How do we do that?

We can add variables on the fly simply by specifying a value for them. For example, if you run the line below, it will create a new variable called Z_Age, filled with ones.

```R
df$Z_Age <- 1
```

But we want to fill it with the actual Z score of the Age:


```R
df$Z_Age <- scale(df$Age)
df$Z_Negative_Affect <- scale(df$Negative_Affect)
```

As we can see, our dataframe df is now made of 22 variables (instead of 20 as in the beginning). Now, let's fit a linear model of the two new variables and compare it with the correlation of the same two original variables (not scaled).

```R
fit2 <- lm(Z_Negative_Affect ~ Z_Age, data=df)
summary(fit2)

cor.test(df$Negative_Affect, df$Age)
```

As you can see, the p value and the beta are almost identical (altough not exactly, due to some minimal imprecisions caused by the intermediate `scale()` function). Again, you can retrieve the confidence interval with the `confint()` function.

**As a conclusion, linear and nonlinear modelling is a powerful, consistent and general framework.**



### Packages

We will finish this course by what makes the wealth of languages such as R, Python, Matlab or Julia:
The existence of thousands of packages (or modules) that extent their possibilities.

In R, there are three ways of installing a package. For the majority of packages, you can do:

- Click on Tools -> Install Packages...
- Directly use the `install.packages()` function. For example, we can download the "devtools" package by running the following command:

```R
  install.packages("neuropsychology")
```

First, every time you start an R session, you need to *load* a package in order to use it:

```R
  library("neuropsychology")
```
The `neuropsychology` package contains the function `cortable()` that returns a correlation matrix with significance stars as well as a plot.

```R
  cortable(df)
```

<p align="legt"><img src="https://github.com/neuropsychology/neuropsychology.R/blob/master/tests/testthat/cortable_plot.png" width="700"></p>

## That's it!

:clap::clap::clap::clap:

We hope you're not afraid to do your statistics with R anymore and that you are eager to discover more about this language. 
Believe us, it's worth it.

**Thank you !!!**
