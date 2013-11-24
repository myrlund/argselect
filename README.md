argselect
=========

> A simple implementation of `argmax` and `argmin` in Python.

Example run
-----------

    $ python argselect.py 3 2 1 5 -3 -6 6 -1 1
    Using the square function.
    argmax of 1, 2, 3, 5, 6, -6, -3, -1: 6, -6
    argmin of 1, 2, 3, 5, 6, -6, -3, -1: 1, -1

Or it can be called from code:

```python
from argselect import argmin, argmax

def cube(n):
    return n ** 3

minimized_arg = argmin(cube, [-1, 2, -3])
maximized_arg = argmax(cube, [-1, 2, -3])
```
