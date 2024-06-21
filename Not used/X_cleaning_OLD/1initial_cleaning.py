import pandas as pd
from tabulate import tabulate

path = 'Data/twitter_data.csv'       # Path to data

# Load the csv file to a Dataframe
df_twitter = pd.read_csv(path, quotechar='"', sep=',')

# Remove whitespaces from the Content (text) column
df_twitter['Content'] = df_twitter['Content'].str.replace('\n', ' ')

# Remove unneeded columns
df_twitter = df_twitter.drop(['Unnamed: 0', 'Unnamed: 8', 'Date', 'Video Thumbnail', 'Image', 'month', 'day'], axis=1)

# Replace nan values for Likes, Retweets and Replies to 0
df_twitter['Like'] = df_twitter['Like'].fillna(0)
df_twitter['Retweet'] = df_twitter['Retweet'].fillna(0)
df_twitter['Reply'] = df_twitter['Reply'].fillna(0)

# Make Likes, Retweets and Replies entries numeric
df_twitter['Like'] = pd.to_numeric(df_twitter['Like'], errors='coerce')
df_twitter['Retweet'] = pd.to_numeric(df_twitter['Retweet'], errors='coerce')
df_twitter['Reply'] = pd.to_numeric(df_twitter['Reply'], errors='coerce')

# Rename boroughs to match other datasets (to merge)
df_twitter['Borough'] = df_twitter['Borough'].replace({
    'Barking_and_Dagenham': 'Barking and Dagenham', 'Hammersmith_and_Fulham': 'Hammersmith and Fulham',
    'Kensington_and_Chelsea': 'Kensington and Chelsea', 'Kingston': 'Kingston upon Thames',
    'Levisham': 'Lewisham', 'Richmond': 'Richmond upon Thames', 'Tower_Hamlets': 'Tower Hamlets'
})

# Reorder the columns
df_twitter = df_twitter[['Borough', 'year', 'Like', 'Retweet', 'Reply', 'Post Type', 'Content']]

# Display small part of the dataframe
print(tabulate(df_twitter[1:100], headers='keys'))

# Export dataframe to csv
df_twitter.to_csv('Data/twitter_data_clean.csv', encoding='utf', index=False)