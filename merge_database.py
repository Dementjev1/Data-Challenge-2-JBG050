import geopandas as gpd

# Load KML files
boroughs = gpd.read_file('data/metropolitan.kml', driver='KML')
police_areas = gpd.read_file('data/metropolitan.kml', driver='KML')

# Check the data
print(boroughs.head())
print(police_areas.head())

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))
boroughs.plot(ax=ax, color='blue', edgecolor='black')
police_areas.plot(ax=ax, color='none', edgecolor='red', linewidth=2)
plt.show()
