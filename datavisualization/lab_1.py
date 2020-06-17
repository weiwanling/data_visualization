# -*- coding: utf-8 -*-
# In[0]
import pandas as pd
import matplotlib.pyplot as plt
df_can=pd.read_excel('.\dataset\Canada.xlsx',sheet_name='Canada by Citizenship',skiprows=range(20),skipfooter=2)
years = list(map(str, range(1980, 2014)))
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can['Total'] = df_can.sum(axis=1)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.set_index('Country', inplace=True)
df_can.columns = list(map(str, df_can.columns))
# In[1]
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.index = haiti.index.map(int)
#haiti.index=list(map(int,haiti.index)) 
haiti.plot(kind='line')
plt.title('imigrants from Hatti')
plt.xlabel('Years')
plt.ylabel('number of imigrants')
plt.text(2000,6000,'2010 Earthuake')
plt.show()
# In[2]
df_CI = df_can.loc[['India', 'China'], years]
df_CI = df_CI.transpose()
df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# In[3]
### type your answer here
# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose() 

df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size

print(df_top5)

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()