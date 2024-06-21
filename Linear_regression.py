'''In this file we run a regression on the parameters retrieved from the Twitter channels of the boroughs to assess
their impact on trust and informing ability.'''
#importing necessary libraries
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan



#We load the previously aggregated data
data = pd.read_csv(r"C:\Users\20225009\Documents\Data Challenge 2\Code\regression datasets\granular_twitter_theme.csv")
data = data.apply(pd.to_numeric, errors='coerce')
data = data.fillna(0)


print(data)



#we choose the independent and dependent variables
#Andor's variables: 'avg_like', 'avg_reply', 'avg_retweet', 'post_length', 'post_type_image', 'post_type_text', 'post_type_video', 'Police force', 'Contact / Interact', 'London', 'Project Servator', 'Local', 'Missing person', 'Crime', 'Arrest / Results', 'Traffic', 'Drugs'
#Nikita's variables: 'robbery',	'assault', 'theft', 'homicide', 'shooting', 'vandalism', 'arson', 'domestic', 'violence', 'knife', 'weapon', 'drug', '101', 'vehicle', 'stolen', 'wanted', 'charged'
     # 'alert', 'warning', 'advisory', 'notice', 'lockdown', 'evacuation', 'safetytips', 'help', 'assist', 'callcontact', 'hotline'
     # 'thank you', 'appreciation', 'help', 'support', 'community', 'event', 'protest'
independent_variables = ['Police force', 'Contact / Interact', 'London', 'Project Servator', 'Local', 'Missing person', 'Crime', 'Arrest / Results', 'Traffic', 'Drugs']
dependent_variable = ['Retweet']

# First, we explore correlations between the different variables by scatter plots

sns.pairplot(data[independent_variables])
plt.suptitle("Scatter Plot Matrix of reply_count, like_count, and retweet_count", y=1.02)
plt.show();


#We run the regression
# Define the dependent variable (y) and the independent variables (X)
X = data[independent_variables]
y = data[dependent_variable]

# Add a constant to the independent variable matrix (for the intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())

#Check OLS Assumptions
#A1 is assumed, A2) iid sample by performing Durbin-Watson test (between 0-4, 2 is no autocorrelation)

dw = durbin_watson(model.resid)
print('Durbin-Watson statistic:', dw)

#A3 no perfect multicollinearity by calculating VIF for each independent variable
'''
vif_data = data
vif_data['Variable'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)
'''
#A4 by Breusch-Pagan test
bp_test = het_breuschpagan(model.resid, model.model.exog)
labels_bp = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
print('Breusch-Pagan test results:', dict(zip(labels_bp, bp_test)))

