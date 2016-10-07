# -*- coding: utf-8 -*-
import inspect

class Path:
    def root():
        return(inspect.getfile(Path).split("path.py")[0])
    def logo():
        return(inspect.getfile(Path).split("path.py")[0] + "files\\logo\\")
    def binary():
        return(inspect.getfile(Path).split("path.py")[0] + "files\\binary\\")
    def font():
        return(inspect.getfile(Path).split("path.py")[0] + "files\\font\\")