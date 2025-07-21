# Databricks notebook source
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# COMMAND ----------

path = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv' 
online_rt = pd.read_csv(path, encoding = 'latin1') 
online_rt.head()


# COMMAND ----------

# group by the Country
countries = online_rt.groupby('Country').sum()
# sort the value and get the first 10 after UK
countries = countries.sort_values(by = 'Quantity',ascending = False) [1:11]
# create the plot
countries['Quantity'].plot(kind='bar')
colors = plt.cm.tab10.colors 
countries['Quantity'].plot(kind='bar', color=colors)
plt.xlabel('Countries')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.title('10 Countries with most orders')
plt.show()



# COMMAND ----------

online_rt = online_rt[online_rt.Quantity > 0] 
online_rt.head()

# COMMAND ----------

customers = online_rt.groupby(['CustomerID','Country']).sum()
# there is an outlier with negative price 
customers = customers[customers.UnitPrice > 0]
# get the value of the index and put in the column Country 
customers['Country'] = customers.index.get_level_values(1)
# top three countries
top_countries =  ['Netherlands', 'EIRE', 'Germany']
# filter the dataframe to just select ones in the top_countries
customers = customers[customers['Country'].isin(top_countries)]
#################
# Graph Section #
#################
# creates the FaceGrid
g = sns.FacetGrid(customers, col="Country")
# map over a make a scatterplot
g.map(plt.scatter, "Quantity", "UnitPrice", alpha=1)
# adds legend
g.add_legend()


# COMMAND ----------

customers = online_rt.groupby(['CustomerID','Country']).sum().head()
customers

# COMMAND ----------

customers.UnitPrice.dtype 

# COMMAND ----------

display(online_rt[online_rt.CustomerID == 12347.0].sort_values(by='UnitPrice', ascending = False).head()) 
display(online_rt[online_rt.CustomerID == 12346.0].sort_values(by='UnitPrice', ascending = False).head())


# COMMAND ----------

sales_volume = online_rt.groupby('Country').Quantity.sum().sort_values(ascending=False)
top3 = sales_volume.index[1:4]
#We are excluding UK 
top3


# COMMAND ----------

online_rt['Revenue'] = online_rt.Quantity * online_rt.UnitPrice 
online_rt.head()

# COMMAND ----------

grouped = online_rt[online_rt.Country.isin(top3)].groupby(['CustomerID','Country'])
plottable = grouped['Quantity','Revenue'].agg('sum') 
plottable['AvgPrice'] = plottable.Revenue / plottable.Quantity
# get the value of the index and put in the column Country
plottable['Country'] = plottable.index.get_level_values(1) 
plottable.head()


# COMMAND ----------

g = sns.FacetGrid(plottable, col="Country")
# map over a make a scatterplot
g.map(plt.scatter, "Quantity", "AvgPrice", alpha=1)
# adds legend
g.add_legend()


# COMMAND ----------

grouped = online_rt.groupby(['CustomerID'])
plottable = grouped['Quantity','Revenue'].agg('sum')
plottable['AvgPrice'] = plottable.Revenue / plottable.Quantity
# map over a make a scatterplot
plt.scatter(plottable.Quantity, plottable.AvgPrice) 
plt.plot()


# COMMAND ----------

grouped = online_rt.groupby(['CustomerID','Country']) 
plottable = grouped.agg({'Quantity': 'sum','Revenue': 'sum'})
plottable['AvgPrice'] = plottable.Revenue / plottable.Quantity
# map over a make a scatterplot
plt.scatter(plottable.Quantity, plottable.AvgPrice)
#Zooming in. (I'm starting the axes from a negative value so that
#the dots can be plotted in the graph completely.) 
plt.xlim(-40,2000) 
plt.ylim(-1,80) 
plt.plot()
#And there is still that pattern, this time in close-up!
[]


# COMMAND ----------

#They are used both in selecting data from
#the DataFrame and plotting the data so I've assigned
#them to variables to increase consistency and make things easier
#when playing with the variables. 
price_start = 0 
price_end = 50 
price_interval = 1
#Creating the buckets to collect the data accordingly
buckets = np.arange(price_start,price_end,price_interval)
#Select the data and sum
revenue_per_price = online_rt.groupby(pd.cut(online_rt.UnitPrice, 
buckets)).Revenue.sum()
revenue_per_price.head()




# COMMAND ----------

revenue_per_price.plot()
plt.xlabel('Unit Price (in intervals of '+str(price_interval)+')')
plt.ylabel('Revenue')
plt.show()


# COMMAND ----------

revenue_per_price.plot()
#Place labels
plt.xlabel('Unit Price (in buckets of '+str(price_interval)+')') 
plt.ylabel('Revenue')


# COMMAND ----------

revenue_per_price.plot()
#Place labels
plt.xlabel('Unit Price (in buckets of '+str(price_interval)+')') 
plt.ylabel('Revenue')

plt.xticks(np.arange(price_start,price_end,3),
np.arange(price_start,price_end,3))
plt.yticks([0, 500000, 1000000, 1500000, 2000000, 2500000],['0', '$0.5M', '$1M', '$1.5M', '$2M', '$2.5M']) 
plt.show() 

# COMMAND ----------

