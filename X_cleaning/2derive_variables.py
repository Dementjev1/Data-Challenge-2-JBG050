import pandas as pd
from tabulate import tabulate

path = 'Data/twitter_data_clean.csv'       # Path to data

# Load the csv file to a Dataframe
df_twitter_clean = pd.read_csv(path, quotechar='"', sep=',')

# Group by every borough per year and calculate the derived variables
derived_df = df_twitter_clean.groupby(['Borough', 'year']).agg(
    {
        'Like': 'sum',  # Sum the 'Like' column
        'Retweet': 'sum',  # Sum the 'Retweet' column
        'Reply': 'sum',  # Sum the 'Reply' column
        'year': 'size',  # Count the number of entries
        'Content': lambda x: x.str.len().mean()  # Calculate the average length of 'text'
    }
)

# Rename columns
derived_df = derived_df.rename(columns={'year': 'entries', 'Content': 'post_length'})

# Group by 'Borough', 'year' and 'Post Type', and count the number of each type of post
post_type_counts = df_twitter_clean.groupby(['Borough', 'year', 'Post Type']).size().reset_index(name='counts')
# Pivot this dataframe to have 'Post Type' values as columns
post_type_counts_pivot = post_type_counts.pivot_table(index=['Borough', 'year'], columns='Post Type', values='counts', fill_value=0).reset_index()
# Join this dataframe with your original dataframe
derived_df = pd.merge(derived_df, post_type_counts_pivot, on=['Borough', 'year'], how='left')

# # Format year column as datetime object
# derived_df['year'] = pd.to_datetime(derived_df['year'], format='%Y')

# Make column names lowercase
derived_df.columns = map(str.lower, derived_df.columns)

# Display dataframe
print(tabulate(derived_df, headers='keys'))

# Save dataframe to csv file
derived_df.to_csv('Data/twitter_data_derived.csv', encoding='utf', index=False)