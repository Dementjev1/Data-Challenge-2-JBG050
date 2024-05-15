import pandas as pd
import matplotlib.pyplot as plt


# Assuming the CSV file is in the same directory as your Python scrip

# Load the CSV file into a DataFrame
df = pd.read_csv(".//granular_PAS//PAS_ward_level_FY_15_17.csv", header = 0)

#dropping empty columns
#df = df.drop(columns=['Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'])

# Now you can use 'df' to work with your data
print(df.head(15))# This will print the first few rows of the DataFrame

#NAn and datatype
print(df.info())

#Explorattory statisctics of the dataframe
print(df.describe())

# Group by 'borough' and 'year', then calculate proportions of each ethnicity
proportions = df.groupby(['FinancialYear', 'BOROUGHNEIGHBOURHOOD'])['NQ147r'].value_counts(normalize=True).rename('proportion').reset_index()

pd.set_option('display.max_columns', None)  # Show all columns

print(proportions)