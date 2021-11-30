import os
import pandas as pd

csv_list = os.listdir("./data")  # returns list

df_list = []
df_map = {}

for file in csv_list:
    print(file)
    if "csv" in file:
        df_map[file.split(".")[0]] = pd.read_csv("./data/" + file)
    else:
        df_map[file.split(".")[0]] = pd.read_excel("./data/" + file)
    
# for every word (csv) in the list, read_csv if it has.csv extension else use read_excel
# df_list = [pd.read_csv("./data/" + csv) if "csv" in csv else pd.read_excel("./data/" + csv) for csv in csv_list]

nrows, ncols = df_map['titanic'].shape

print("There are %d rows, and %d columns in the Titanic DataFrame" % (nrows, ncols))
print(df_map['titanic'].dtypes)  # Gives data types
'NB - the date/time object hasnt returned as datetime due to ambiguity. Python automatically will assign object'

print(df_map['titanic'].columns)

df_map['titanic'].sort_values(by=['age', 'ticket'], ascending=[True, False])
print(df_map['titanic'].head())

'Selecting a single column - Returns a Series'
print(df_map['titanic'].fare)  # Equivalent to the preferred method below
print(df_map['titanic']['fare'])

'Selecting multiple columns - 2D list'
print(df_map['titanic'][['age', 'sex', 'name', 'survived']])

'Selecting on Data Type'
print(df_map['titanic'].select_dtypes(include=["object"]))  # Could use param 'exclude' the same way, with int64 or float64 or np.number

'Filtering'
print(df_map['titanic'][0:4])  # Selects first 5, like head

'Creating a Mask - Returns a Single Column of True/Falso'
mask = df_map['titanic']['sex'] == 'female'
print(mask)

'''Filtering on Condition'''
print(df_map['titanic'][mask])  # Could use mask as input
print(df_map['titanic'][df_map['titanic']['sex'] == 'female'])  # or reiterate with conditions directly 

'''Filtering on Multiple Conditions - Use & or |'''
print(df_map['titanic'][(df_map['titanic']['sex'] == 'female') & (df_map['titanic']['age'] > 30) & df_map['titanic']['fare'] > 0.8 ])

'''Filter Shortcuts / Syntax'''
print(df_map['titanic'][df_map['titanic']['boat'].isin(["2", "C", "15"])])  # Where boat field is in the list provided
print(df_map['titanic'][df_map['titanic']['age'].between(0, 12)])  # Where age field between two values provided
print(df_map['titanic'][~(df_map['titanic']['sex'] == 'female')])  # ~ can be used to invert mask (similar to !=), must wrap in ()

print(df_map['titanic'].query('fare > 50 & sex == "male"'))  # Searches the contents as shown
print(df_map['titanic'].filter(like='1', axis=0))  # Filters based on the index value, not the contents

'''Deriving New Columns'''

df_map['titanic']['new_column'] = 1  # Create new col with constant value
df_map['titanic']['family_size'] = df_map['titanic']['sibsp'] + df_map['titanic']['parch'] + 1  # Add parents and sibling rows together to get fam size
df_map['titanic']['under_18_bool'] = df_map['titanic']['age'] < 18  # Create boolean col (missing ages will evaluate to false)
df_map['titanic']['under_18_bin'] = df_map['titanic']['under_18_bool'].astype("int64")  # Convert from bool to binary

# One of the issues is that missing/NaN ages will evaluate to not under 18
# These values should be replaced as None to avoid assumign they are over 18
# We can use loc for this 

df_map['titanic'].loc[df_map['titanic']['age'].isnull(), 'under_18_bool'] = None  # Where age = NaN, make under_18_bool None
print(df_map['titanic'][df_map['titanic']['age'].isnull()].head())

'''Mapping Columns using Dictionary'''

df_map['titanic']['port'] = df_map['titanic']["embarked"].map({"S": "Southampton", "C":"Cherboug", "Q":"Queenstown"})

'''Deleting Columns'''
del df_map['titanic']['new_column']  # Use del keyword
df_map['titanic'].drop(columns=['under_18_bin', "port"], inplace=True)  # Or use drop() method
print(df_map['titanic'].columns)

'''Left, Right, Inner and Outer Joins'''
print(df_map['joining_data1'])
print(df_map['joining_data2'])

left_merge = pd.merge(left=df_map['joining_data1'],
                      right=df_map['joining_data2'],
                      how='outer',  # Keep LHS values if no match on RHS
                      on='name',  # Common field
                      indicator=True)  # Indicate if not a full match
print(left_merge)

'''Union (or concatenation)'''

union_joined = pd.concat(objs=[df_map['joining_data1'], df_map['union_data']], ignore_index=True)
print(union_joined)

