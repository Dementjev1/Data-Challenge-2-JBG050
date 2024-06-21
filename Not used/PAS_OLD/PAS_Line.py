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


Question = 'NQ135BH'
# NQ135BD (Trust in Police)
# NQ62D (Police have same sense of right and wrong
# NQ135BDE (Trust in Media Companies
# NQ135BD (Police in local area are held accountable


# Extract all grandular PAS data
df = extract_csv_files('PAS_Data')
# Extract month and trust scores
df_trust = df[['MONTH', 'NQ135BD', 'NQ62D', 'NQ135BDE', 'NQ135BH']]

# Format month as mm-YYYY (datetime type)
df_trust['DATE'] = df_trust['MONTH'].apply(lambda x: pd.to_datetime(x.split('(')[1].replace(')', ''), format='%b %Y').strftime('%m-%Y'))
print(tabulate(df_trust, headers='keys'))

# Map score text as integers
score_mapping = {'Strongly disagree': 1, 'Tend to disagree': 2, 'Neither agree nor disagree': 3, 'Tend to agree': 4, 'Strongly agree': 5}
df_trust[Question] = df_trust[Question].map(score_mapping)

# Convert date column to datetime
df_trust['DATE'] = pd.to_datetime(df_trust['DATE'], format='%m-%Y')

# Pivot the data to get trust scores in columns and their counts for each date in rows
df_pivot = df_trust.groupby(['DATE', Question]).size().reset_index(name='Count')
df_pivot = df_pivot.pivot(index='DATE', columns=Question, values='Count').fillna(0)

# Specify a diverging colormap
cmap = plt.cm.get_cmap('coolwarm', 5)

# Plot absolute counts of trust levels
plt.figure(figsize=(10,6))
for i, column in enumerate(df_pivot.columns):
    plt.plot(df_pivot.index, df_pivot[column], marker='', linewidth=2, label=column, color=cmap(i))
plt.title('Police is held accountable absolute count')
plt.xlabel('Month')
plt.ylabel('Count')
plt.legend(title='Scores', title_fontsize='13', loc='upper right')
plt.savefig('Figures/Accountability police Line Absolute 2015-2021')


# Plot percentages of total levels of trust
df_pivot = df_pivot.divide(df_pivot.sum(axis=1), axis=0)
plt.figure(figsize=(10,6))
for i, column in enumerate(df_pivot.columns):
    plt.plot(df_pivot.index, df_pivot[column], marker='', linewidth=2, label=column, color=cmap(i))

# Annotations
annotations = {'10-2017': 'Cost Cutting', '06-2020': 'BH & NS', '03-2021': 'SE'}
for date, text in annotations.items():
    annotation_date = pd.to_datetime(date)
    plt.annotate(text, (annotation_date, df_pivot.loc[annotation_date].max()), textcoords="offset points",
                 xytext=(0,10), ha='center', fontsize=8, color='black')
    plt.axvline(x=annotation_date, color='grey', linestyle='--')  # Draw a vertical line at the annotation dates

plt.title('Police accountability percentage of total')
plt.xlabel('Month')
plt.ylabel('Percentage')
plt.legend(title='Scores', title_fontsize='13', loc='upper left')
plt.savefig('Figures/Accountability police Line Percentage 2015-2021')