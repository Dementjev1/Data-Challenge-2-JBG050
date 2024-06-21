import pandas as pd
from tabulate import tabulate

path = 'Data/twitter_data_clean.csv'       # Path to data

# Load the csv file to a Dataframe
df_twitter_clean = pd.read_csv(path, quotechar='"', sep=',')

# Group by every borough per year and calculate the derived variables
derived_df = df_twitter_clean.groupby(['Borough', 'year', 'Post Type']).agg(
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

# Reset index to make borough, year and post type seperate columns
derived_df = derived_df.reset_index()

# # Format year column as datetime object
# derived_df['year'] = pd.to_datetime(derived_df['year'], format='%Y')

# Make column names lowercase
derived_df.columns = map(str.lower, derived_df.columns)

derived_df = derived_df.rename(columns={'post type': 'post_type'})

# Display dataframe
print(tabulate(derived_df, headers='keys'))

# Save dataframe to csv file
derived_df.to_csv('Data/twitter_data_derived_post_type.csv', encoding='utf', index=False)