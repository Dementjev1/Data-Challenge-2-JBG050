import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

def extract_csv_files(directory):
    """
    Extracts all csv files in a certain directory into one DataFrame.
    :param directory: Target directory
    :return: DataFrame with data from all csvs in the directory
    """
    files = os.listdir(directory)
    csv_files = [f for f in files if f.endswith('.csv')]
    dataframes = []

    for csv_file in csv_files:
        df = pd.read_csv(os.path.join(directory, csv_file))
        dataframes.append(df)

    # Concatenate all dataframes
    final_df = pd.concat(dataframes, ignore_index=True)
    return final_df


Question = 'Q131'
# Q131 (Informed local)
# Q133 (Informed London)

# Extract all grandular PAS data
df = extract_csv_files('PAS_Data')
# Extract month and trust scores
df_informed = df[['MONTH', 'Q131', 'Q133']]

# Format month as mm-YYYY (datetime type)
df_informed['DATE'] = df_informed['MONTH'].apply(lambda x: pd.to_datetime(x.split('(')[1].replace(')', ''), format='%b %Y').strftime('%m-%Y'))
print(tabulate(df_informed.head(), headers='keys'))

# Map score text as integers
score_mapping = {'Very well informed': 1, 'Fairly well informed': 2, 'Not at all informed': 3}
df_informed[Question] = df_informed[Question].map(score_mapping)

# Convert date column to datetime
df_informed['DATE'] = pd.to_datetime(df_informed['DATE'], format='%m-%Y')

# Take relevant timeframe (2017 - 2020)
mask = (df_informed['DATE'] > '2016-12-31') & (df_informed['DATE'] <= '2019-12-31')
df_informed = df_informed.loc[mask]
print(tabulate(df_informed.head(), headers='keys'))

# Pivot the data to get trust scores in columns and their counts for each date in rows
df_pivot = df_informed.groupby(['DATE', Question]).size().reset_index(name='Count')
df_pivot = df_pivot.pivot(index='DATE', columns=Question, values='Count').fillna(0)
print(tabulate(df_pivot, headers='keys'))

# Specify a diverging colormap
cmap = plt.cm.get_cmap('coolwarm', 3)

# Plot absolute counts of trust levels
plt.figure(figsize=(10,6))
for i, column in enumerate(df_pivot.columns):
    plt.plot(df_pivot.index, df_pivot[column], marker='', linewidth=2, label=column, color=cmap(i))
plt.title('People feeling informed about police locally')
plt.xlabel('Month')
plt.ylabel('Count')
plt.legend(title='Scores', title_fontsize='13', loc='upper right')
plt.savefig('Figures/Informed police local Line Absolute')


# Plot percentages of total levels of trust
df_pivot = df_pivot.divide(df_pivot.sum(axis=1), axis=0)
plt.figure(figsize=(10,6))
for i, column in enumerate(df_pivot.columns):
    plt.plot(df_pivot.index, df_pivot[column], marker='', linewidth=2, label=column, color=cmap(i))
plt.title('People feeling informed about police locally')
plt.xlabel('Month')
plt.ylabel('Percentage')
plt.legend(title='Scores', title_fontsize='13', loc='upper left')
plt.savefig('Figures/Informed police local Line Percentage')