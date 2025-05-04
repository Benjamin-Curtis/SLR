# Sea Level Rise & Financial Risk in NYC

This project evaluates financial risks posed by sea level rise in New York City, focusing on parcel-level data in Brooklyn and Queens. It estimate which parcels are projected to be impacted under a 75-inch rise scenario by 2100, group them by school district, and explore exposure by owner type (business vs non-business). The goal is to understand whether local institutions may face financial risk due to non-geographically diverse investments.


## Motivation

Due to climate change, sea levels are rising as ice caps continue to melt. Scientists have projected different sea level rise scenarios depending on the trajectory of global emissions and human behavior. These rising seas pose a growing risk to coastal areas, including major population centers like New York City. 

This analysis was conducted to investigate whether projected flooding poses a financial risk to the institutions that operate in these areas, particularly neighborhood banks and property owners, as well as to the communities who live there. By identifying vulnerable properties and quantifying their value, the aim is to better understand the potential scale financial exposure.

## Methodology

- **Data Source**: NYC parcel geometry and sea level rise projections
- **Preprocessing**:
  - Used QGIS to extract parcels intersecting with 2100 sea level rise projections.
  - Exported trimmed parcels and attributes to CSV for analysis in Python.
- **In Python**:
  - Parcels were tagged as impacted based on their ID matching the trimmed layer.
  - Owners were classified as business if they owned ≥2 residential parcels or ≥1 non-residential parcel.
  - Grouped parcels by `SCHOOL_CODE`, `business`, and `is_impacted` to summarize total assessed value.
- **Visualizations**:
  - Total value at risk by school district
  - Differences between business vs. non-business risk
  - Pie charts of share of value at risk

## Scripts Overview

### `scripts/queens_direct_risk.py`
1. Loads trimmed Queens parcel data and full parcel data.
2. Flags impacted parcels based on their `SWIS_SBL_ID`.
3. Cleans and standardizes owner names.
4. Identifies business owners based on parcel count and type.
5. Merges ownership info back to the parcel file.
6. Groups by `SCHOOL_CODE`, `business`, and `is_impacted` to calculate:
   - Total parcel count
   - Total assessed value
7. Exports the result to CSV/Excel for visualization.



### `scripts/brooklyn_direct_risk.py` and `brooklyn_plots.py`
These scripts mirror the logic of the Queens scripts but use the Brooklyn dataset and filenames.


## Visualizations


![alt text](figures/Queens_Value_by_Impact.png)


 Assessed Value by Business Ownership and Flood Risk in Queens

![alt text](figures/value_at_risk_queens.png)


  Share of Total Assessed Value at Risk (Queens)



## Tools Used

- **Python**:
  - `pandas` 
  - `geopandas` 
  - `matplotlib` 
- **QGIS** — used to extract impacted parcels and create base maps

## Author

Benjamin Curtis