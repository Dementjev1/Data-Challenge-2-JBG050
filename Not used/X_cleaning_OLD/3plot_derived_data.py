import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

path = 'Data/twitter_data_derived.csv'       # Path to data

# Load the csv file to a Dataframe
df_twitter_derived = pd.read_csv(path, quotechar='"', sep=',')

# Display the dataframe
print(tabulate(df_twitter_derived, headers='keys'))

# Get the unique borough
boroughs = df_twitter_derived['borough'].unique()

# Calculate the number of rows and columns needed for subplots
n = len(boroughs)
cols = int(np.ceil(np.sqrt(n)))
rows = int(np.ceil(n / cols))

# Create a figure and a set of subplots
fig, axs = plt.subplots(rows, cols, figsize=(5*cols, 5*rows))

# Create a line chart for each location
for i, borough in enumerate(boroughs):
    # Filter the dataframe for the current location
    borough_df = df_twitter_derived[df_twitter_derived['borough'] == borough]

    # Calculate the position of the subplot
    row = i // cols
    col = i % cols

    # Plot 'entries' over 'year'
    axs[row, col].plot(borough_df['year'], borough_df['entries'], label=borough)

    # Add title and labels
    axs[row, col].set_title('Number of tweets per year for ' + borough)
    axs[row, col].set_xlabel('Year')
    axs[row, col].set_ylabel('Tweets')

# Adjust the layout
plt.tight_layout()

# Save the plots
plt.savefig('Figures/tweets_per_borough.png')