import os
import pandas as pd

def clean_directory(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # Check if the file does not end with 'metropolitan-street.csv' or 'metropolitan-outcomes.csv'
            if not file.endswith("metropolitan-street.csv") and not file.endswith("metropolitan-outcomes.csv"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {str(e)}")


def list_files(root_path):
    for root, dirs, files in os.walk(root_path):
        print(f"Directory: {root}")
        if files:
            for file in files:
                print(f"  File: {file}")
        else:
            print("  No files found in this directory.")

def list_csv_columns(root_path):
    for root, dirs, files in os.walk(root_path):
        print(f"Directory: {root}")
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                try:
                    df = pd.read_csv(file_path)
                    columns = df.columns.tolist()
                    print(f"  File: {file}, Columns: {columns}")
                except Exception as e:
                    print(f"  Failed to read {file_path}: {str(e)}")
            else:
                print(f"  File: {file} is not a CSV file.")

def display_top_values(file_name):
    # Load the dataset
    df = pd.read_csv(file_name)

    # Initialize a dictionary to store top values for each attribute
    top_values = {}

    # Loop through each column in the dataframe
    for column in df.columns:
        # Get the top 7 most frequent values and their counts
        top_values[column] = df[column].value_counts().head(20)

    return top_values

def merge_files(directory, file_suffix):
    all_files = []
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        count=0
        for file in files:
            # Check if the file ends with the specified suffix
            if file.endswith(file_suffix):
                full_path = os.path.join(root, file)
                df = pd.read_csv(full_path)
                all_files.append(df)
                count+=1
                print(f'Added file {root} number {count}')

    # Concatenate all dataframes if not empty
    if all_files:
        merged_df = pd.concat(all_files, ignore_index=True)
        return merged_df
    else:
        return pd.DataFrame()  # Return an empty dataframe if no files matched


def clean_cols_and_rows(file):
    df = pd.read_csv(file)

    columns_to_remove = ["Reported by", "Falls within", "Context"]
    df.drop(columns=columns_to_remove, inplace=True, errors='ignore')

    df = df[~df['Month'].str.startswith(tuple(["2010", "2011", "2012"]))]

    return df

def clean_cols_and_rows2(file):
    df = pd.read_csv(file)

    columns_to_remove = ["Reported by", "Falls within"]
    df.drop(columns=columns_to_remove, inplace=True, errors='ignore')

    df = df[~df['Month'].str.startswith("2012")]

    return df

street_path = 'data/crime_data/2010-2024/metropolitan-street-data.csv'
outcomes_path = 'data/crime_data/2010-2024/metropolitan-outcomes-data.csv'

clean_street = (clean_cols_and_rows(street_path)).to_csv("metropolitan_street_data.csv", index=False)
clean_outcomes = (clean_cols_and_rows2(outcomes_path)).to_csv("metropolitan_outcomes_data.csv", index=False)

