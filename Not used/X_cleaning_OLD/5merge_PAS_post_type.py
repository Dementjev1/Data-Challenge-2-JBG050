import pandas as pd
from tabulate import tabulate

path = 'Data/twitter_data_pop_post_type.csv'       # Path to data
path2 = 'Data/df_pas_2017.csv'
path3 = 'Data/df_pas_2018.csv'
path4 = 'Data/df_pas_2019.csv'
path5 = 'Data/df_pas_2020.csv'

# Load the csv files to Dataframes
df_twitter_pop = pd.read_csv(path, quotechar='"', sep=',')
df_PAS_2017 = pd.read_csv(path2, sep=';')
df_PAS_2018 = pd.read_csv(path3, sep=';')
df_PAS_2019 = pd.read_csv(path4, sep=';')
df_PAS_2020 = pd.read_csv(path5, sep=';')

# Get columns of interest from PAS data
df_PAS_2017 = df_PAS_2017[['year', 'gender', 'race', 'borough', 'mean_Q131', 'mean_Q133', 'count',
                           'total_surveys_borough', 'Q131_Q133_avg', 'proportion_subgroup']]
df_PAS_2018 = df_PAS_2018[['year', 'gender', 'race', 'borough', 'mean_Q131', 'mean_Q133', 'count',
                           'total_surveys_borough', 'Q131_Q133_avg', 'proportion_subgroup']]
df_PAS_2019 = df_PAS_2019[['year', 'gender', 'race', 'borough', 'mean_Q131', 'mean_Q133', 'count',
                           'total_surveys_borough', 'Q131_Q133_avg', 'proportion_subgroup']]
df_PAS_2020 = df_PAS_2020[['year', 'gender', 'race', 'borough', 'mean_Q131', 'mean_Q133', 'count',
                           'total_surveys_borough', 'Q131_Q133_avg', 'proportion_subgroup']]

# Append PAS data from all years to one Dataframe
df_PAS = pd.concat([df_PAS_2017, df_PAS_2018, df_PAS_2019, df_PAS_2020], ignore_index=True)

# Merge Twitter data and PAS data
derived_df = pd.merge(df_twitter_pop, df_PAS, on=['borough', 'year'])

# Name columns
derived_df = derived_df.rename(columns={'entries': 'count_Twitter', 'Population': 'population', 'count': 'count_PAS'})

# Order columns
derived_df = derived_df[['borough', 'year', 'population', 'gender', 'race', 'post_type', 'like', 'retweet', 'reply',
                         'post_length', 'count_Twitter', 'mean_Q131', 'mean_Q133', 'Q131_Q133_avg','count_PAS',
                         'total_surveys_borough', 'proportion_subgroup']]

print(tabulate(derived_df, headers='keys'))

# Save dataframe to csv file
derived_df.to_csv('Data/data_merged_post_type.csv', encoding='utf', index=False)
