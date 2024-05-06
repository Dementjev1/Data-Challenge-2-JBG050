import os
import pandas as pd




street_path = 'data/crime_data/2010-2024/metropolitan-street-data.csv'
outcomes_path = 'data/crime_data/2010-2024/metropolitan-outcomes-data.csv'

street_data = pd.read_csv(street_path)
print(street_data.info(show_counts=True))