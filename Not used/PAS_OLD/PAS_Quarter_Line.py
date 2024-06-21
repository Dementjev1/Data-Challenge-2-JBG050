import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from tabulate import tabulate

# Extract data
df = pd.read_csv('PAS_Data_Quarter/PAS_quarter.csv')
print(tabulate(df, headers='keys'))

# Format the Quarter column to dates
df['Quarter'] = pd.to_datetime(df['Quarter'], format='%d-%m-%Y')  # Convert 'Quarter' to datetime
df = df.sort_values('Quarter')  # Sort the values

# New column with Quarter dates as numeric values
df['QuarterNumeric'] = mdates.date2num(df['Quarter'])

# Line plot
plt.figure(figsize=(10, 6))
plt.plot(df['Quarter'], df['Trust'], marker='o')
plt.plot(df['Quarter'], df['Confidence'], marker='o')
plt.plot(df['Quarter'], df['Treat_Fair'], marker='o')

# Add vertical/annotation lines for Corona Lockdown announcements
dates = ['2020-3-31', '2020-10-31', '2021-01-06']
for date in dates:
    plt.axvline(pd.to_datetime(date), color='r', linestyle='--')

# Add vertical lines for event indicators, as time ranges
events_date_ranges = [('2017-10-16', '2017-10-16'), ('2020-06-1', '2020-07-31'), ('2021-03-7', '2021-03-20'),
               ('2021-09-26', '2021-10-02'), ('2021-10-1', '2021-11-30'), ('2022-01-02', '2022-01-08'),
               ('2022-03-13', '2022-03-19'), ('2022-05-01', '2022-05-31'), ('2023-01-15', '2023-02-11'),
               ('2023-03-01', '2023-03-31')]
for start_date, end_date in events_date_ranges:
    start_date_numeric = mdates.date2num(pd.to_datetime(start_date))
    end_date_numeric = mdates.date2num(pd.to_datetime(end_date))
    plt.axvspan(xmin=start_date_numeric, xmax=end_date_numeric, ymin=0, ymax=1, color='r', alpha=0.3)

# Line plot labels & Title
plt.xlabel('Time (Quarter)')
plt.ylabel('Trust')
plt.title('Trust over quarters (Rolling 12) with event timeline indicators')
plt.legend(['Trust', 'Confidence', 'Treat fairly'])
# plt.grid(True)
plt.savefig('Figures/Trust per quarter with event timeline')
