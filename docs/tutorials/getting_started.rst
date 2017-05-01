1. Getting Started
====================


Contact
---------

For remarks, complaints, suggestions or anything else, please create an `issue <https://github.com/neuropsychology/Neuropsydia.py/issues>`_.


Installation
---------------

Installation steps can be found `here <http://neurokit.readthedocs.io/en/latest/tutorials/Python.html>`_.


Hands on!
----------------

**Well, first of all, welcome and thank you for trying the Python version of Neuropsydia for research. I'm sure you will like it as, while still in developpment, it already has some powerful functions that will help you create your tasks, experiments, and more.**
 
But enough talking! After the installation, open your python code editor (*e.g.,* spyder, available within the `WinPython <https://winpython.github.io/>`_ bundle). Here, you will write functions that will almost magically come to live once the program is launched.

In spyder, one pane is the **CONSOLE**, where Python actually lives. It's its interface with us humans. If you type something in there, it will swallow it, do something with it, and then, maybe, return something. Also, it's great for calculus. For example, try typing `5*2` and hit Enter.
 
*Pretty cool, huh?*
 
**But for now, let's focus on some simple things, such as how to load, start and close neuropsydia.**
 
 
  
Import Neuropsydia
---------------------


Neuropsydia for research is a module which, like any other module, must be loaded in order to be used. In Python, we load modules by running:

.. code:: python

    import themoduleiwanttoload

Then, we can use its functions:

.. code:: python

    themoduleiwanttoload.function1()
    themoduleiwanttoload.function2()


However, as you can see it, it's pretty anoying to write the full name of the module each time we use one of its function. Fortunately for us, Python allows us to load a module under another name (or :code:`alias`), for example the letter "x".

.. code:: python

    import themoduleiwanttoload as x
    x.function1()
    x.function2()

    
*Better*. That's what we are going to do with neuropsydia, loading it under the name "n".
 
**However, unlike many other packages, Neuropsydia CANNOT be loaded without two of its function, :code:`start()` and :code:`close()`.**
 
 
 
Start and Close
---------------------

So, when importing :code:`neuropsydia`, what happens is basically that it needs to initialize several things before being ready to use. And those things are initialized with the :code:`start()` function. Moreover, adding the :code:`close()` function at the end will ensure a clean ending.
 
**Therefore, every experiments, after loading the neuropsydia module, will begin by the :code:`start()` function and end with the :code:`close()` function.**
 
Let's try it. Write in the editor the following lines of code:

.. code:: python

    import neuropsydia as n
     
    n.start()
    n.close()

 
 
Execute your code
------------------

The rest of your code will go between the :code:`start()` and the :code:`close()` functions. But these 3 lines are a minimal working program, so let's try it.
 
To execute an entire python program, **always open a new python console** (in spyder, go to console, then click on :code:`open a new python console`, then press F5, - or the green arrow).
 
**Do it.**
 
...
 
Tadaaaa, *voilà*, you've created your first neuropsydia-based program :)


