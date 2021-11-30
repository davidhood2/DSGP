import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv_list = os.listdir("./data")  # returns list

df_map = {}

for file in csv_list:
    if "csv" in file:
        df_map[file.split(".")[0]] = pd.read_csv("./data/" + file)
    else:
        df_map[file.split(".")[0]] = pd.read_excel("./data/" + file)
    
# for every word (csv) in the list, read_csv if it has.csv extension else use read_excel
# df_list = [pd.read_csv("./data/" + csv) if "csv" in csv else pd.read_excel("./data/" + csv) for csv in csv_list]

print(df_map['titanic'].describe())  # Provides some brief stats on the data in the frame

print(df_map['titanic']['fare'].describe())  # Can also be used on a column

print(df_map['titanic'].describe(include=['object']))  # Gets descriptive info for other types (i.e. objects)

min_fare = df_map['titanic']['fare'].min()  # Get first / min and highest / last items sorted
first_name = df_map['titanic']['name'].min()
max_fare = df_map['titanic']['fare'].max()
last_name = df_map['titanic']['name'].max()  # NB: All lower cases come *after* upper cases due to CHAR numbers
print("Lowest Fare: %d\tFirst Name: %s" % (min_fare, first_name))
print("Highest Fare: %d\tLast Name: %s" % (max_fare, last_name))

'''Quantiles'''

print(df_map['titanic']['fare'].quantile(q=0.25))  # Print first 25% quantile
print(df_map['titanic']['fare'].quantile(q=[i / 4 for i in range(0, 5, 1)]))  # Can also give array of quantiles

'''Averages'''

fare_med = df_map['titanic']['fare'].median()  # Get median and modal averages
fare_mode = df_map['titanic']['fare'].mode()  # Also works on non-numeric columns

print("Median fare: %d,\tModal Fare:%d" % (fare_med, fare_mode))

'''Spread'''
fare_std = df_map['titanic']['fare'].std()
fare_var = df_map['titanic']['fare'].var()

print("Std Dev: %d,\t Variance: %d" % (fare_std, fare_var))

'''Counting Values'''
rows = df_map['titanic']['embarked'].shape[0]  # Get number of rows from shape property
valid_counts = df_map['titanic']['embarked'].count()  # Total numebr of valid rows
total_invalid = df_map['titanic'][df_map['titanic']['embarked'].isna()]['embarked'].isna().count()  # isna() generates True/False map

print("Total rows in Frame: %d\nTotal rows counted: %d\nTotal Invalid Rows: %d" % (rows, valid_counts, total_invalid))

print(df_map['titanic']['sex'].value_counts())  # Counts the frequency of unique values

'''Other Summarising Methods'''

ticket_sum = df_map['titanic']['fare'].sum()  # Sums all numerics in col, ignoring Nones/NaNs etc
print("Sum of Ticket Values: %d" % ticket_sum)

print(df_map['titanic']['boat'].unique())  # Prints all unique values in column
print(df_map['titanic']['boat'].nunique())  # Prints number of unique values

'''Creating Size Bands'''

# We can use the pdf.cut method to split (or bin) data into groups, such as age bands
# It will create a 'category' type column in the frame

df_map['titanic']['binned_ages'] = pd.cut(df_map['titanic']['age'], bins=10)  # Creates 10 equally spaced bins between max, min vals
print(df_map['titanic'].sample(5))

# The issue we have here is that the bins are evenly spaced between min/max and 
# and would be better spaced in intervals defined by ourselves

bin_range = np.arange(0, (df_map['titanic']['age'].max() + 1), 10)  # Create range of bings inc. top value

print(bin_range)
df_map['titanic']['binned_ages2'] = pd.cut(df_map['titanic']['age'], bin_range)
print(df_map['titanic'].sample(5))

# We can also label the bins more accurately by providing a list and 
bin_labels = ['0-10', '11,20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']

df_map['titanic']['EqualSpacedBins'] = pd.cut(df_map['titanic']['age'], bin_range, labels=bin_labels)
print(df_map['titanic'].sample(5))

# Using qcut we can devide based on quantiles i.e. the same number in each bin

df_map['titanic']['QCutBins'] = pd.qcut(df_map['titanic']['age'], q=10)  # Divide into 10 equal sized bins

'''
fig, ax = plt.subplots(1, 2)  # Create subplot
str_compare = ['EqualSpacedBins', 'QCutBins'] #Columns to iterate through
for i in range(0, len(str_compare)):
    data = df_map['titanic'][str_compare[i]].value_counts().tolist()  # Convert value counts into list
    labels = df_map['titanic'][str_compare[i]].value_counts().index.astype('string').tolist()  # Convert lbalens into list of strings
    
    ax[i].barh(labels, data)
    ax[i].set_xlabel('Freq')
    ax[i].set_ylabel("Bins")
    ax[i].set_title("Distribution using %s" % str_compare[i])
fig.tight_layout()
plt.show()
'''

'''Aggregation'''

# Grouping data together by a particular variable and producing a summary
print(df_map['titanic']['pclass'].unique())  # Show unique class values (1st/2nd/3rd etc)
# 1. Data is split into 1 dataframe per groupby value ('pclass')
# 2. Aggregation - applied to each dataframe to create a single row for each grouping (mean())
# 3. Combine the frames back into a result (in this case, just the 'fare')
av_ticket_price = df_map['titanic'].groupby(by='pclass')['fare'].mean() 
print(av_ticket_price)

av_price_loc = df_map['titanic'].groupby(by=['embarked', 'pclass'])['fare'].mean()  # Creates subcategories for each value in the array
print(av_price_loc)

