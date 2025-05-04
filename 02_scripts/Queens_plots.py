#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 18:37:33 2025

@author: benjamincurtis
"""
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
#find value of impacted parcels compared to those not, split by if its a business
#load in queens summary csv
df=pd.read_csv('/Users/benjamincurtis/Library/Mobile Documents/com~apple~CloudDocs/Sea Level Rise NYC /data/school_district_summary_queens.csv')

#group by business and impact status and find sum of those values
grouped=df.groupby(['business', 'is_impacted'])['total_value'].sum().unstack()

# Plot
plt.rcParams['figure.dpi'] = 300
fig1, ax1=plt.subplots()
grouped.plot.bar(stacked=True, ax=ax1)
fig1.suptitle('Total Assessed Value by Business Ownership and Flood Risk in Queens')
ax1.set_ylabel('Assessed Value')
fig1.tight_layout()
fig1.savefig('value_by_impact_queens.png')
#%%
#Risk by School Code
#filter for only at risk parcels
at_risk=df[df['is_impacted'] == 1]

#group total value by school code 
by_school = at_risk.groupby('SCHOOL_CODE')['total_value'].sum()

# Plot
plt.rcParams['figure.dpi']= 300
fig2, ax2=plt.subplots()
by_school.plot.bar(title='Total Assessed Value at Risk by School Districts in Queens', ax=ax2)
ax1.set_ylabel('Assessed Value')
fig1.tight_layout()
fig1.savefig('risk_value_by_queens_district.png')
#%%
#pie chart to show scale of value of impacted parcels
total_values=df['total_value'].sum()
total_impacted_value=df.loc[df['is_impacted'], 'total_value'].sum()
not_impacted_value=total_values - total_impacted_value

#Values and labels
values=[not_impacted_value, total_impacted_value]
labels=['Not at Risk', 'At Risk']

#Plot
plt.rcParams['figure.dpi'] = 300
fig3, ax3=plt.subplots()
fig3.suptitle('Share of Total Assessed Property Value at Risk in Queens')
plt.pie(values, labels=labels,autopct='%1.1f%%')
fig3.tight_layout()
fig3.savefig("value_at_risk_queens.png")











