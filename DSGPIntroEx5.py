import os
import pandas as pd

csv_list = os.listdir("./data")  # returns list

df_map = {}

for file in csv_list:
    print(file)
    if "csv" in file:
        df_map[file.split(".")[0]] = pd.read_csv("./data/" + file)
    else:
        df_map[file.split(".")[0]] = pd.read_excel("./data/" + file)
    
# for every word (csv) in the list, read_csv if it has.csv extension else use read_excel
# df_list = [pd.read_csv("./data/" + csv) if "csv" in csv else pd.read_excel("./data/" + csv) for csv in csv_list]

animals_reference = df_map['animals']  # Creates a call-by-reference tag
animals_copy = df_map['animals'].copy()  # Creates a new variable

# The following generates a copy warning because DataFrame[DataFrame[field]] returns a copy
# And does not edit the original dataframe
df_map['animals'][df_map['animals']['AnimalGroupParent'] == 'Bull']['AnimalGroupParent'] = "cow"  # Changes value of copy only 

print(df_map['animals'][(df_map['animals']['AnimalGroupParent'] == 'Bull') | (df_map['animals']['AnimalGroupParent'] == "Cow")])  # Returns cow or bull

'''Updating Data Frame values'''

# Loc takes lookup arg, then arg to update
df_map['animals'].loc[df_map['animals']['AnimalGroupParent'] == "Bull", "AnimalGroupParent"] = "Cow"  # Uses function loc to edit original
df_map['animals'].loc[df_map['animals']['AnimalGroupParent'] == 'Lamb', "AnimalGroupParent"] = "Sheep"
# print(df_map['animals'][['AnimalClass', 'AnimalGroupParent']])

'''Str Comparison Methods in DataFrames'''

print(df_map['pun_animals']['animal_type'].unique())  # Shows seperate 'cat' and "cat" categories

df_map['pun_animals']['animal_type'] = df_map['pun_animals']['animal_type'].str.lower()  # Convert all animal types to lower case
print(df_map['pun_animals']['animal_type'].unique())  # Shows seperate 'cat' and "cat" categories

'''Finding incorrect values in DataFrame Types'''
print(df_map['pun_animals'].dtypes)  # Age should be a number
print(df_map['pun_animals'][df_map['pun_animals']['age'].str.isalpha()])  # Shows only rows where age has letters in it

df_map['pun_animals'].loc[df_map['pun_animals']["age"] == "One", "age"] = "1"  # Use Loc to change to numeric
df_map['pun_animals']['age'] = pd.to_numeric(df_map['pun_animals']['age'])  # Now convert the datatype
print(df_map['pun_animals'].dtypes)  # And check

print(df_map['pun_animals'][~df_map['pun_animals']['weight_kg'].str.isdigit()])
df_map['pun_animals'].loc[df_map['pun_animals']['weight_kg'] == '113kg', 'weight_kg'] = "113"
df_map['pun_animals']['weight_kg'] = pd.to_numeric(df_map['pun_animals']['weight_kg'], downcast="float")
# df_map['pun_animals']['weight_kg'] = df_map['pun_animals']['weight_kg'].astype('float64') # Also works 
print(df_map['pun_animals'].dtypes)

'''Changing Columns Names'''

print(df_map['pun_animals'].columns)
df_map['pun_animals'].rename(columns={'name':'pet_name'}, inplace=True)  # Rename a column
df_map['pun_animals'].columns = df_map['pun_animals'].columns.str.replace(" ", "_")
df_map['pun_animals'].columns = df_map['pun_animals'].columns.str.lower()
print(df_map['pun_animals'].sample(1))

'''Handling missing values'''

print(df_map['pun_animals'][['pet_name', 'steps_per_day']])  # Prints a col showing NaN, and erroneous '.'
df_map['pun_animals'].loc[df_map['pun_animals']['steps_per_day'] == '.', 'steps_per_day'] = None  # Convert in place to None
df_map['pun_animals']['steps_per_day'] = pd.to_numeric(df_map['pun_animals']['steps_per_day'])
print(df_map['pun_animals']['steps_per_day'].dtypes)

pun_animals_cleaned = df_map['pun_animals'].copy()

mean_steps = round(df_map['pun_animals']['steps_per_day'].mean(), ndigits=0)  # Get the column mean and round to 0

pun_animals_cleaned['steps_per_day'].fillna(value=mean_steps, inplace=True)  # Replace all NA values with mean steps
print(pun_animals_cleaned[['steps_per_day', 'pet_name']])

pun_animals_dropped = df_map['pun_animals'].copy()
pun_animals_dropped.dropna(axis=0, how='any', inplace=True) # Drop all rows with any NA value
print(pun_animals_dropped[['pet_name','steps_per_day']]) #
pun_animals_dropped.reset_index(drop=True, inplace=True) #Reset the row index

