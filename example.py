from argselect import argmin, argmax

def cube(n):
    return n ** 3

argmin(cube, [-1, 2, -3])
# => [-3]

argmax(cube, [-1, 2, -3])
# => [2]
