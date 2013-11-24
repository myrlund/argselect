argselect
=========

A simple implementation of `argmax` and `argmin` in Python.

It differs from most other built-in implementations in that it returns all arguments yielding a max/min result.

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

argmin(cube, [-1, 2, -3])
# => [-3]

argmax(cube, [-1, 2, -3])
# => [2]
```
