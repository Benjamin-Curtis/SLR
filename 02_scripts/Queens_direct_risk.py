#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:42:57 2025

@author: benjamincurtis
"""
# author: benjamincurtis

#load in library
import pandas as pd
import geopandas as gpd
#%%
#1 load in parcels and impacted parcels
#read in parcel data
parcels = pd.read_csv("Queens_Parcels.csv", dtype=str)

#load trimmed parcels 
impacted_parcels=gpd.read_file('Queens_trimmed.gpkg',layer='queensvulnerable__trimmed')
impacted_swis=impacted_parcels['SWIS_SBL_ID'].unique()

#add impact status to full parcel DataFrame
parcels['is_impacted'] = parcels['SWIS_SBL_ID'].isin(impacted_swis)

#residential classes
#1-Family, 2-Family, 3-Family
res_classes = ['01', '02', '03']  

#convert assessed value to float
parcels['TOTAL_AV'] = parcels['TOTAL_AV'].astype(float)

#find any missing values
print(parcels['TOTAL_AV'].isna().sum())

#drop any missing values
parcels = parcels.dropna(subset='TOTAL_AV')

#verify
print(parcels['TOTAL_AV'].isna().sum()) 
#%%
#2.identify Business Owners
#clean owner column
#clean owner type column
parcels['owner_clean']=parcels['PRIMARY_OWNER'].str.lower()
parcels['owner_clean']=parcels['owner_clean'].str.replace(r'[^\w\s]', '', regex=True)
parcels['owner_clean']=parcels['owner_clean'].fillna('unkown')

#Flag each parcel as residential 
parcels['residential']=parcels['PROP_CLASS'].isin(res_classes)

parcels['non_residential']= ~parcels['PROP_CLASS'].isin(res_classes)


#Group by owner and count parcel types
owner_summary = parcels.groupby('owner_clean').agg(
    total_parcels=('SWIS_SBL_ID', 'count'),
    res_parcels=('residential', 'sum'),
    nonres_parcels=('non_residential', 'sum'))

#business rule:owner has ≥1 non-residential or ≥2 residential
owner_summary['business']=(owner_summary['nonres_parcels'] > 0) | (owner_summary['res_parcels'] >= 2)

#%%
#3.merge business info back onto parcels
parcels = parcels.merge(owner_summary, on='owner_clean', how='left')
#%%
#4. count by school district
direct_risk = parcels.groupby(['SCHOOL_CODE', 'business','is_impacted']).agg(
    parcel_count=('SWIS_SBL_ID', 'count'),
    total_value=('TOTAL_AV', 'sum'))
#%%
# 5. export
direct_risk.to_csv('school_district_summary_queens.csv')
direct_risk.to_excel('school_district_summary_queens.xlsx')

