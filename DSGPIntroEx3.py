import os
import pandas as pd
import random

print(os.getcwd())  # Get current dir of process

os.chdir("..")  # Change dir (passed as call to shell?)

'''
Note about Relative / Absolute paths
- Relative, require proc to be in the correct directory, but otherwise work between users
- Abosolute doesnt work when work dirs are shared
- Use fwd slash / where possible, or prefix string with r"..\data\resource.csv" etc to stop \escape charater
'''

schools_data = pd.read_csv(r"DSGP-Intro-2.2/schools_data.csv")  # Use sep argument to indicate delimiter
print(schools_data)
print(schools_data.tail())

police_data = pd.read_excel(r"DSGP-Intro-2.2/police_data.xlsx")  # Use sep argument to indicate delimiter

print(police_data)

cheese_list = ['cheddar', 'gorgonzola', 'brie', 'camembert', 'red leceister', 'wensleydale', 'gruyere', 'halloumi',
                'emmental''Double Gloucester', 'Parmesan', 'Stilton']

cheese_series = pd.Series(cheese_list)  # Convert list of cheeses to Series
cost_series = pd.Series([random.randint(1, 100) / 100 for cheese in cheese_list])  # Generate matching lists of costs
cheese_costs = pd.DataFrame({"Cheese": cheese_series, "Cost":cost_series})

cheese_costs.to_excel("DSGP-Intro-2.2/cheeses.xlsx")
