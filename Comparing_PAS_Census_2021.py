import pandas as pd
import matplotlib.pyplot as plt


# Assuming the CSV file is in the same directory as your Python scrip

# Load the CSV file into a DataFrame
df1 = pd.read_csv(".//granular_PAS//PAS_ward_level_FY_20_21.csv", header = 0)
selected_columns1 = ['Borough', 'ReNQ147']
new_df1 = df1[selected_columns1].copy()
proportions1 = new_df1.groupby(['Borough'])['ReNQ147'].value_counts(normalize=True).rename('proportion_PAS').reset_index()

df2 = pd.read_csv(".//Census_2021//census_2021_ethnicity.csv", header = 0)
selected_columns2 = ['Upper tier local authorities', 'Ethnic group', 'Observation']
new_df2 = df2[selected_columns2].copy()

# Group by 'Borough' and 'Ethnic Group', and sum the 'Observations' for each group
grouped_df2 = new_df2.groupby(['Upper tier local authorities', 'Ethnic group']).sum()

# Reset index to make 'Borough' and 'Ethnic Group' regular columns
grouped_df2.reset_index(inplace=True)

# Calculate total observations per borough
total_per_borough = grouped_df2.groupby('Upper tier local authorities')['Observation'].transform('sum')

# Calculate proportions of each ethnic group per borough
grouped_df2['Proportion_Census'] = grouped_df2['Observation'] / total_per_borough

#print(proportions1)
#print(grouped_df2)

merged_df = pd.merge(proportions1, grouped_df2, left_on=['Borough', 'ReNQ147'], right_on=['Upper tier local authorities', 'Ethnic group'], how='inner')
merged_df = merged_df.drop(columns=['Upper tier local authorities', 'Ethnic group', 'Observation'])

pd.set_option('display.max_columns', None)  # Show all columns
print(merged_df)
# Assuming you have your DataFrame loaded as df

# Save DataFrame to CSV file
merged_df.to_csv('census_PAS_ethnicity.csv', index=False)  # Set index=False if you don't want to save the index
