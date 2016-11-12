#<p align="center"> Statistics for Psychologists with R: An Introduction </p>
**<p align="center"> Dominique Makowski </p>**

<p align="center"><img src="https://biblineuropsy.files.wordpress.com/2016/08/n.png" width="200"></p>


*<p align="center">This course is supported by the École de Neuropsychologie group.</p>*

---

## About the course


| Course Status | ![](https://img.shields.io/badge/status-dev-brightred.svg) |
|---------------|---|
| Length | ≈ ...min |


This course was crafted by psychologists, neuropsychologists and neuroscientists for psychologists, neuropsychologists and neuroscientists.
As such, it is a straightforward introduction to R with a special focus on how to get some actual results with it.
It is not a programming course on R, nor a course on statistics *per se*.

Note that there are other more complete tutorials teaching R for psychological research (such as [this one](http://personality-project.org/r/) or [my favourite one](https://drive.google.com/file/d/0B4udF24Yxab0S1hnZlBBTmgzM3M/view
)).

### Contact

For remarks, complaints, suggestions or anything else, you can contact the creator of this course via  [Linkedin](https://fr.linkedin.com/in/dominiquemakowski), email (<dom.makowski@gmail.com>) or by creating an issue on this repository.

### The Pipe Operator %>%

### Create Variables
- On the fly

- `mutate()`

### Rename Variables, Levels and Relevel

- `rename()`

- `factor(labels=)` [rename levels]

- `factor(levels=)` [reorder levels]

### Arrange
- `arrange()`
- `spread()`
- `separate()`

### Select and Filter

- `select()`
 - `ends_with()` = Select columns that end with a character string
 - `contains()` = Select columns that contain a character string
 - `matches()` = Select columns that match a regular expression
 - `one_of()` = Select columns names that are from a group of names
 - `num_range(x, i:j)`
- `filter()`
 - `(>, <, >=, <=, !=, %in%)`
 - `(&, |)`
  
### Group by

- `group_by()`
- `summarise()`
 - `n()`

### Reshape

tidyr

- `gather()`
- `separate()`
- `spread(df, levels_to_columns, values)`

### Merge
- `full_join()`
- `bind_rows()`
- `bind_cols()`
