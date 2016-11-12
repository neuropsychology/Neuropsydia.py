#<p align="center"> Statistics for Psychologists with R: Mixed Modeling </p>
**<p align="center"> Dominique Makowski </p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course

| Course Status | ![](https://img.shields.io/badge/status-dev-brightred.svg) |
|---------------|---|
| Length | ≈ ...min |


This course was crafted by psychologists, neuropsychologists and neuroscientists for psychologists, neuropsychologists and neuroscientists.



## Why We Should All Use the Mixed Modeling Framework

see: 

[Magezi (2015)](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4302710/)


> Despite this preponderance of categorical data, the
> use of statistical analyses that have long been known
> to be questionable for caterogical data analysis (such as analysis of variance,
> ANOVA) is still commonplace in our field.
> While there are powerful modern methods designed
> for caterogical data analysis [...], they are considered too complicated or simply
> unnecessary.
> --[Jaeger (2008), p. 435](http://www.sciencedirect.com/science/article/pii/S0749596X07001398)


> Traditional approaches to random effects modeling
> suffer multiple drawbacks which can be eliminated by
> adopting mixed effect linear models. These drawbacks
> include (a) deficiencies in statistical power related to
> the problems posed by repeated observations, (b) the
> lack of a flexible method of dealing with missing data,
> (c) disparate methods for treating continuous and categorical
> responses, as well as (d) unprincipled methods
> of modeling heteroskedasticity and non-spherical
> error variance (for either participants or items). Methods
> for estimating linear mixed effect models have
> addressed each of these concerns, and offer a better
> approach than univariate ANOVA or ordinary least
> squares regression.
> --[Baayen (2008), p. 391](http://www.sciencedirect.com/science/article/pii/S0749596X07001398)


> These mixed effects models offer many additional advantages
> over both traditional repeated-measures ANOVA and
> quasi-F statistics. These include the ability to handle incomplete
> and unbalanced data, the ability to easily accommodate continuous
> as well as categorical predictors, avoidance of information loss due
> to prior averaging over stimuli or participants, principled unbiased
> handling of incomplete and/or outlying cases...
> --[Judd (2012), p. 391](http://psycnet.apa.org/journals/psp/103/1/54/)



### Terminology

- LM
- LME
- LMX
- Hierarchical
- LMER

## Procedure

> [They]  show that LMEMs generalize best when they include the maximal random effects structure justified by the design.
> [Barr (2013)](http://www.sciencedirect.com/science/article/pii/S0749596X12001180)


## Applications

### For MRI 

- [Friston (2005)](http://www.sciencedirect.com/science/article/pii/S1053811904005877)
- [Chen (2013)](http://www.sciencedirect.com/science/article/pii/S1053811913000943)

> Our core contribution is to provide a quantitative empirical evaluation of the performance of Linear Mixed Effects 
> and competing alternatives popularly used in prior longitudinal structural MRI studies, 
> namely repeated measures ANOVA [...] Our results suggest that the Linear Mixed Effects approach offers 
> superior statistical power in detecting longitudinal group differences.
> --[Bernal-Rusiel (2012)](http://www.sciencedirect.com/science/article/pii/S1053811912010683)


## Examples

post-hocs:
```R
library(lsmeans)
library(lmerTest)
lsmeans::lsmeans(fit, pairwise~Intensity)
plot(lmerTest::lsmeans(fit))

```

