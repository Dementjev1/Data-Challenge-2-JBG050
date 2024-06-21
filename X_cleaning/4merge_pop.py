import pandas as pd
from tabulate import tabulate

path = 'Data/twitter_data_derived.csv'       # Path to data
path2 = 'Data/housing-density-borough.csv'

# Load the csv files to Dataframes
df_twitter_derived = pd.read_csv(path, quotechar='"', sep=',')
df_population = pd.read_csv(path2, sep=',')

# Get columns of interest from population data
df_population = df_population[['Name', 'Year', 'Population']]
# Rename columns
df_population = df_population.rename(columns={'Name': 'borough', 'Year': 'year'})

# Merge Twitter data and population data
derived_df = pd.merge(df_twitter_derived, df_population, on=['borough', 'year'])
print(tabulate(derived_df, headers='keys'))

# Save dataframe to csv file
derived_df.to_csv('Data/twitter_data_pop.csv', encoding='utf', index=False)
