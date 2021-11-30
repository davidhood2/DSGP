'''
Created on 10 Nov 2021

@author: David
'''
import pandas as pd
import random


cheese_list = ['cheddar', 'gorgonzola', 'brie', 'camembert', 'red leceister', 'wensleydale', 'gruyere', 'halloumi', 'emmental']

print(cheese_list[0:3], cheese_list[-2])

# Basic list functions
cheese_list.sort()
cheese_list.extend(['Double Gloucester','Parmesan', 'Stilton'])
cheese_list.pop(-1)

print(cheese_list)
print(dir(cheese_list))



cheese_series = pd.Series(cheese_list) # Convert list of cheeses to Series
cost_series = pd.Series([random.randint(1, 100)/100 for cheese in cheese_list]) #Generate matching lists of costs

'''
2 Dimensional List (1 series per column)
Columns can only have one datatype
Index (rows) start at 0
Columns (headers) also indexed, but can be referred to by header as K-V pair
'''

cheese_costs = pd.DataFrame({"Cheese": cheese_series,
                             "Cost":cost_series})

print(cheese_costs)

print(cheese_costs.sample(n=4, replace=True)) # replace allows row to be sampeld twice

