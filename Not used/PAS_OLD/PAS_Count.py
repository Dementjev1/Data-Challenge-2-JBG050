import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

def extract_one_csv_file(directory):
    files = os.listdir(directory)
    csv_files = [f for f in files if f.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:
        df = pd.read_csv(os.path.join(directory, csv_file))
        dataframes[csv_file] = df

    return dataframes

df = extract_one_csv_file('PAS_Data')['PAS_ward_level_FY_20_21.csv']
df_trust = df[['MONTH', 'NQ135BD', 'NQ62D', 'NQ135BDE', 'NQ135BH']]
df_trust['DATE'] = df_trust['MONTH'].apply(lambda x: pd.to_datetime(x.split('(')[1].replace(')', ''), format='%b %Y').strftime('%m-%Y'))
print(tabulate(df_trust, headers='keys'))

# COUNTPLOT
plt.figure(figsize=(10,7))
sns.countplot(x='DATE', hue='NQ135BD', data=df_trust)
plt.title('Count of levels of trust in police per Month | Financial Year 2020-2021')
plt.xlabel('Month')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend(title='Scores', title_fontsize='13', loc='upper right')
plt.savefig('Figures/Trust Police Count FY 20-21')