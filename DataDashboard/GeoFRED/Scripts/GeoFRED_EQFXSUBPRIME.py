#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Imports  
import pandas as pd 


# In[7]:


# Create backups
df_backup = pd.read_csv('./Updates/STG_FRED_EQFXSUBPRIME.txt')
df_backup.to_csv('./Backups/STG_FRED_EQFXSUBPRIME_BACKUP.txt')


# In[8]:


# Getting and reading new data 
df = pd.read_excel("https://geofred.stlouisfed.org/api/download.php?theme=pubugn&colorCount=5&reverseColors=false&intervalMethod=fractile&displayStateOutline=true&lng=-89.96&lat=40.81&zoom=4&showLabels=true&showValues=true&regionType=county&seriesTypeId=147149&attributes=Not+Seasonally+Adjusted%2C+Quarterly%2C+Percent&aggregationFrequency=Quarterly&aggregationType=Average&transformation=lin&date=2019-04-01&type=xls&startDate=1999-01-01&endDate=2019-04-01&mapWidth=999&mapHeight=521&hideLegend=false", skiprows = 1)
df.head()


# In[9]:


# Filter data to display only North Carolina
filter1 = df['Region Name'].str.contains(', NC')
df_nc = df[filter1]
df_nc.head()


# In[10]:


# Save file to tab delimited txt for upload to SSMS
df_nc.to_csv('./Updates/STG_FRED_EQFXSUBPRIME.txt', sep = '\t')
