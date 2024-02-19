#February 12, 2024
#trying to access netcdf file for downscaled temp data for Dover DE
#USING X ARRAY

import xarray as xr
import pandas as pd
import numpy as np

#import temp data and view via xarray
data_26_45 = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\AvgT_projected\AvgT_26_45.nc")
data_70_85 = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\AvgT_projected\AvgT_70_85.nc")
#print(data_70_85)
#print(data_26_45['mean_ssp1'])

#save to numpy dataframe and then to csv to use
df1 = data_26_45['mean_ssp1'].to_dataframe()
df1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\AvgT_projected\AvgT_26.csv")

df2 = data_26_45['mean_ssp2'].to_dataframe()
df2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\AvgT_projected\AvgT_45.csv")

df3 = data_70_85['mean_ssp1'].to_dataframe()
df3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\AvgT_projected\AvgT_70.csv")

df4 = data_70_85['mean_ssp2'].to_dataframe()
df4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\AvgT_projected\AvgT_85.csv")


