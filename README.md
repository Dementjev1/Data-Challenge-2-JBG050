# Data Challenge 2 - Improving trust and confidence in the MPS

This is the readme file for running the code for group 3 in Data Challenge 2. The project is an exploration and analysis of the social media factors impacting the level of information on MPS by the people of the Metropolitan area of London.

## Requirements

The following Python packages are required to run the code:

- pandas
- numpy
- geopandas
- matplotlib
- statsmodels == 0.14.2.
- seaborn == 0.13.2.

## Data Files
The script requires the following data files:

- data_merged.csv
- df_pas_2017.csv
- df_pas_2018.csv
- df_pas_2019.csv
- df_pas_2020.csv
- housing-density-borough.csv
- LSOA_2011_London_gen_MHW.shp
- LSOA_2011_London_gen_MHW.shx
- PAS_Dashboard_Borough.csv
- PAS_stop_and_search.csv
- twitter_data.csv
- df_regression_pas_twitter_q131_133_NO_POP.csv
- granular_twitter_theme.csv

Make sure to modify the full r"file path" with the file needed in case it says the file is not found

## File Descriptions
### Py files
- 1initialcleaning: Further cleaning (filling NA values, renaming borough, etc.)
- 2derive variables: Aggregating the data
- 3plotderivedata: Plotting aggregated data (EDA, not actually used in presentation)
- 4mergepop: Merging aggregated data with population data
- 5mergePAS: Merging aggregated+population data with PAS data
- linear_regression: Performs the regressions for the findings
- 
### Jupyter Notebooks:
The PAS_Cleaning_Preprocessing_Plotting_TWITTER_Plotting.ipynb notebook contains three sections:

- Public Attitude Survey: Preparation, exploration, cleaning, plotting. This section contains the code which produces the dataset used for the regressions. Users need to specify the path to their files under the variables at the start of the section, and running the cells will produce the desired dataset.
- Twitter Data Plots: Contains code to plot the collected X Data on a map of London while considering borough population density. Specification of a correct path to the data is required and must be specified under the specific variable placed at the start of the section.
- Not Used Code: Contains mainly code used at the initial stages of the project when we thought of using also Crime Data from MOPAC in the analysis. This code has been included for completeness, but none of its parts have been used in the final version or the project.

The Figs presentation.ipynb contains the code used for slides 7 and 8 of the presentation.

