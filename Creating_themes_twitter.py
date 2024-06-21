#importing necessary libraries
import pandas as pd
from collections import Counter
import re


#In this part we load the aggregated dataframe from the granular PAS and combined basic Twitter metrics data (according to Giacomo's work)

aggregated_pas_twitter_df = pd.read_csv(r"C:\Users\20225009\Documents\Data Challenge 2\Code\Data-Challenge-2-JBG050\df_regression_pas_twitter_q131_133_NO_POP.csv", sep=";")

#Loading the granular twitter dataset

granular_twitter = pd.read_csv(r"C:\Users\20225009\Documents\Data Challenge 2\Code\Data-Challenge-2-JBG050\granular_twitter.csv")

#Selecting relevant columns for the sentiment analysis

granular_twitter = granular_twitter[['year', 'borough', 'Content', 'Post Type', 'Like', 'Retweet', 'Reply']]

#dummy encoding for the posty types
# Identify the unique values in the column
category_column = 'Post Type'
unique_values = granular_twitter[category_column].unique()

# Create dummy variables for each unique value
for value in unique_values:
    dummy_column_name = f'{category_column}_{value}'
    granular_twitter[dummy_column_name] = granular_twitter[category_column].apply(lambda x: 1 if x == value else 0)

print(granular_twitter)
#Ananlysis to determine the most frequently used words

# Combine all content into one large string
all_content = ' '.join(granular_twitter['Content'].astype(str).tolist())

# Preprocess the text: lowercasing, removing punctuation, etc.
all_content = all_content.lower()  # Convert to lowercase
all_content = re.sub(r'[^a-zA-Z\s]', '', all_content)  # Remove punctuation

# Tokenize the text
words = all_content.split()

# Count the frequency of each word
word_counts = Counter(words)

# Get the most common words
most_common_words = word_counts.most_common(200)  # Change the number to get more or fewer words

# We create the Theme Columns according to the most frequent words

# Dictionary of themes and associated most frequent words
themes = {
    'Police force': ['officers', 'police', 'team'],
    'Contact / Interact': ['call', 'help', 'thank', 'thanks', 'information', 'support', 'contact'],
    'London': ['london', 'public'], 'Project Servator': ['projectservator'], 'Local': ['area', 'local', 'community', 'borough'],
    'Missing person': ['missing'], 'Crime': ['safe', 'crime', 'knife', 'stolen', 'offences', 'incident'],
    'Arrest / Results': ['arrested', 'found', 'report', 'arrest', 'court'],'Traffic': ['road', 'vehicle', 'stop', 'car'],
    'Drugs': ['drugs']
}

# Function to check the presence of words in the content
def check_presence(content, words):
    normalized_content = content.lower()  # Normalize the content to lowercase
    return int(any(word in normalized_content for word in words))

# Create new columns for each theme
for theme, words in themes.items():
    granular_twitter[theme] = granular_twitter['Content'].apply(lambda x: check_presence(str(x).lower(), words))

# Aggregate the dataframe per year per borough for the regression
# Drop the 'Content' column
granular_twitter = granular_twitter.drop(columns=['Content'])
grouped_twitter_df = granular_twitter.groupby(['borough', 'year'], as_index=False).sum()


# Merging the aggregated twitter with the other metrics

merged_df = pd.merge(grouped_twitter_df, aggregated_pas_twitter_df, on=['borough', 'year'])

# Display the merged dataframe
length = len(merged_df)
print(length)