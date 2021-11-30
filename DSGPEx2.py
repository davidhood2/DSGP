'''
Created on 10 Nov 2021

@author: David
'''
import random
Ex12 = [3 * 3, (10 - 3) ** 3, 97623 / 9 ]

for i in range(len(Ex12)):
    # prompt = ("Press a key for answer %i" % i)
    # input(prompt)
    print("Answer %i):\t %i" % (i, Ex12[i])) 

del Ex12

height = 1.6
age = 27
name = "David"
my_bool = True

print("Height:\t Value:\t %f\tType:\t%s " % (height, type(height)))
print("Age:\t Value:\t %f\tType:\t%s " % (age, type(age)))
print("Name:\t Value:\t %s\tType:\t%s " % (name, type(name)))
print("my_bool:\t Value:\t %s\tType:\t%s " % (my_bool, type(my_bool)))

print("\nTrue or False Truth Table\n")

matA = matB = [True, False]

add = lambda X, Y: (X + Y, "+")
sub = lambda X, Y: (X - Y, "-")
mul = lambda X, Y: (X * Y, "*")
div = lambda X, Y: (None if Y == 0 else X, "/")

operations = [add, sub, mul, div]

for op in operations:
    for A in matA:
        for B in matB:
            (res, nary) = op(A, B)
            print("%s %s %s = %s" % (A, nary, B, bool(res)))

hobbies = ["cricket, climbing, walking"]
pets = ("cat", "dog", "hamster")

example_dict = {"name": "Stacy", "buyers": ["Elaine, David"], "prop_num": 57 }
cheese_list = ['cheddar', 'gorgonzola', 'brie', 'camembert', 'red leceister', 'wensleydale', 'gruyere', 'halloumi', 'emmental']

print(cheese_list[0:3], cheese_list[-2])
print(example_dict['buyers'])

cheese_list.sort()

cheese_list.extend(['Double Gloucester', 'Parmesan', 'Stilton'])
cheese_list.pop(-1)

print(cheese_list)
print(dir(cheese_list))

import pandas as pd

cheese_series = pd.Series(cheese_list)
cost_series = pd.Series([random.randint(1, 100) / 100 for cheese in cheese_list])
