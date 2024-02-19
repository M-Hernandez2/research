#February 13, 2024
#trying to access netcdf file for downscaled pr data for DOver DE
#Using NOAA downscaled data
#USING X ARRAY

import xarray as xr
import pandas as pd
import numpy as np


#TESTING IT JUST A TEST NOT THIS THIS IS A TEST
#pr_data = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_Projected\pr_day_ACCESS-CM2_historical_r1i1p1f1_gn_2014.nc")

#print(pr_data)
#print(pr_data['pr'])
#xr.plot.scatter(pr_data, 'time', 'pr')

#df = pr_data['pr'].to_dataframe()
#print(df)
#df.to_csv('C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_Projected\pr_proj_2014.csv')



#import precip data and open via xarray
pr_26_45 = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_projected\pr_26_45.nc")
pr_70_85 = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_projected\pr_70_85.nc")
#print(pr_70_85)

#save to numpy dataframe then to csv to access
df1 = pr_26_45['mean_ssp1'].to_dataframe()
df1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_projected\AvgP_26.csv")

df2 = pr_26_45['mean_ssp2'].to_dataframe()
df2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_projected\AvgP_45.csv")

df3 = pr_70_85['mean_ssp1'].to_dataframe()
df3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_projected\AvgP_70.csv")

df4 = pr_70_85['mean_ssp2'].to_dataframe()
df4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\P_projected\AvgP_85.csv")

