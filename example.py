from argselect import argmin, argmax

def cube(n):
    return n ** 3

minimized_arg = argmin(cube, [-1, 2, -3])
maximized_arg = argmax(cube, [-1, 2, -3])

print minimized_arg
print maximized_arg
