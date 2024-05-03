import pandas as pd
import matplotlib.pyplot as plt


# Assuming the CSV file is in the same directory as your Python scrip

# Load the CSV file into a DataFrame
df = pd.read_csv("C:/Users/20225009/Documents/Data Challenge 2/Code/Datasets/pas_dataset_boroughs.csv", header = 0)

#dropping empty columns
df = df.drop(columns=['Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'])

# Now you can use 'df' to work with your data
print(df.head(15))# This will print the first few rows of the DataFrame

#NAn and datatype
print(df.info())

#Explorattory statisctics of the dataframe
print(df.describe())

#checking statistics on borough level
grouped_by_borough_df = df.groupby('Borough')

#Display count of rows in each group
print("Count of rows in each borough group:")
print(grouped_by_borough_df.size())

# Display basic statistics for each group
print("\nBasic statistics for each borough group:")
print(grouped_by_borough_df.describe())

#how trust changes in the boroughs over time
filtered_df_local = df[df['Measure'] == '"Good Job" local']
filtered_df_local.set_index('Date', inplace=True)
filtered_df_local.groupby('Borough')['Proportion'].plot(legend=True)
plt.title("Good Job done locally over the years")
plt.show()
plt.savefig("boroughs_local_change")