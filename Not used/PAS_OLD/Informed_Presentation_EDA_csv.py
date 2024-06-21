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

def montly_PAS_counts(question, csv_path):
    """
    Extracts Q131 and Q133 (about people feeling informed locally and in whole of London respectively) per month from the granular PAS data and puts it into a csv file.
    :param question: Q131 or Q133
    :param csv_path: path to save csv file
    """
    # Extract all grandular PAS data
    df = extract_csv_files('PAS_Data')
    # Extract month and question to consider
    df_informed = df[['MONTH', question]]

    # Format month as mm-YYYY (datetime type)
    df_informed['DATE'] = df_informed['MONTH'].apply(lambda x: pd.to_datetime(x.split('(')[1].replace(')', ''), format='%b %Y').strftime('%m-%Y'))
    print(tabulate(df_informed.head(), headers='keys'))

    # Convert date column to datetime
    df_informed['DATE'] = pd.to_datetime(df_informed['DATE'], format='%m-%Y')

    # Take relevant timeframe (2017 - 2020)
    mask = (df_informed['DATE'] > '2016-12-31') & (df_informed['DATE'] <= '2019-12-31')
    df_informed = df_informed.loc[mask]
    print(tabulate(df_informed.head(), headers='keys'))

    # Convert date column back to month-year again
    df_informed['DATE'] = df_informed['DATE'].dt.strftime('%Y-%m')

    # Pivot the data to get trust scores in columns and their counts for each date in rows
    df_pivot = df_informed.groupby(['DATE', question]).size().reset_index(name='Count')
    df_pivot = df_pivot.pivot(index='DATE', columns=question, values='Count').fillna(0)

    print(tabulate(df_pivot, headers='keys'))

    # Save dataframe to csv file
    df_pivot.to_csv(csv_path, encoding='utf')


# Q131 (Informed local)
# Q133 (Informed London)
montly_PAS_counts('Q131', 'Informed_data/informed_locally_Q131_month.csv')
montly_PAS_counts('Q133', 'Informed_data/informed_London_Q133_month.csv')

