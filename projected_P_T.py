#February 13, 2024
#statistical distribution for projected temp and precip data
#https://psl.noaa.gov/ipcc/cmip6/timeseries6.html
#Source: NOAA Climate Science Web Portal CMIP6 downscaled to US Northeastern Continental Shelf

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#read in projected t and p data using pandas to create dataframe
p_df = pd.read_excel(r"C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\proj_T_P.xlsx", sheet_name='AvgP')
t_df = pd.read_excel(r"C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\proj_T_P.xlsx", sheet_name='AvgT')

#print(p_df)

#TIME SERIES - precipitation
#p_df.plot(x='year')
#plt.title('Projected Precipitation Time Series')
#plt.xlabel('year')
#plt.ylabel('annual mean precipitation (inches)')
#plt.show()


#TIME SERIES - temperature
#t_df.plot(x='year')
#plt.title('Projected Temperature Time Series')
#plt.xlabel('year')
#plt.ylabel('annual mean temperature (degrees F)')
#plt.show()



#STAT DISTRIBUTION - precipitation
p_df_all = []
#remove missing values
p_df = p_df.dropna()
#print(p_df.head())

#make list with all pr values
p_df = p_df.drop('year', axis=1)
#print(p_df)

p_df_all = np.ravel(p_df.values).tolist()
print(p_df_all)

#sort pr data for distribution
p_df_all.sort(reverse = True)
#print(p_df_all)

#add with NOAA historical annual pr data dist
p_hist_yr = [41.19, 36.77, 42.58, 40.01, 44.6, 39.49, 48.96, 50.67, 57.9, 44.1, 32.21, 50.82, 34, 60.05, 39.25,
             48.11, 40.62, 43.48, 46.7, 35.86, 33.96, 36.04, 21.37, 37.27, 52.89, 33.52, 51.3, 35.87, 57.25,
             55.22, 40.1, 61.37, 40.56, 43.68, 35.59, 39.56, 58.69, 41.64, 46.74, 37.29, 36.2, 40.37, 62.82,
             41.67, 40.89, 39.63, 41.87, 47.64, 38.04, 61.9, 46.93, 42.05, 44.23, 51.48, 38.75, 51.49, 62.97,
             44.88, 44.44, 41.48, 52.58, 46.03, 49.07, 67.21, 44.04]
p_hist_yr.sort(reverse = True)
py_count = []
pp_count = []
#historical range x values out of 100%
for i in range(0, len(p_hist_yr)):
    py_count.append((i/65)*100)
#projected range x values out of 100%
for i in range(0, len(p_df_all)):
    pp_count.append((i/504)*100)

#plt.plot(py_count, p_hist_yr, color = 'forestgreen')
#plt.plot(pp_count, p_df_all, color = 'darkgreen')
#plt.title('Annual Precipitation Values Distribution')
#plt.xlabel('liklihood percent')
#plt.ylabel('precipitation (in)')
#plt.legend(['historical', 'projected'], loc = 'lower left')
#plt.show()

#STAT DISTRIBUTION - temperature
t_df_all = []
#remove missing values
t_df = t_df.dropna()
#print(t_df.head())

#make list with all temp values
t_df = t_df.drop('year', axis=1)
#print(t_df)

t_df_all = np.ravel(t_df.values).tolist()
#print(t_df_all)

#sort temp data for distribution
t_df_all.sort(reverse = True)
#print(t_df_all)

#add in NOAA historical temp data
t_hist_yr = [53.4, 54.2, 53.5, 54.7, 54.9, 61.9, 52.7, 54.7, 55.3, 55.2, 56, 54.7, 57.3, 55, 54.9, 45, 57.1,
             54.4, 57.9, 55.5, 55.1, 53.7, 55.7, 54, 55.6, 55, 55.9, 56.4, 57.4, 56.8, 56.4, 54.7, 54.6, 55.1,
             55.4, 56.8, 56.7, 53.5, 56.8, 56.6, 54.4, 56.1, 56.3, 57, 56.9, 55.5, 59.6, 55.3, 56.7, 57.1, 59.5,
             57.2, 56.6, 57, 57.1, 54.4, 57.8, 55.4, 55.7, 54.7, 54.8, 56.5, 56.2, 55.6, 54.8, 55.8, 55.3, 55.5,
             56.2, 55.6, 57.5, 56.6, 57.1, 56.1, 57.1, 54.1, 57.5, 56.2, 55.5, 56.2, 57, 56.8, 57.6, 57.3, 57.7,
             58.7, 57.3, 58.9, 59.1, 55.9, 57.5, 56, 56.5, 55, 55.8, 58.1, 57.3, 55.4, 57, 58.2, 55.5, 57, 58.5,
             58.8, 57.7, 57.8, 59.1, 57.8, 58.8, 59, 56.2, 55.5, 57.6, 58.4, 58.5, 57.9, 58.1, 49.6, 45.7, 57.5,
             60.4]
t_hist_yr.sort(reverse = True)

ty_count = []
tp_count = []

#make x axis for hist out of 100%
for i in range(0, len(t_hist_yr)):
    ty_count.append((i/121)*100)
#make x axis for projected temp data out of 100%
for i in range(0, len(t_df_all)):
    tp_count.append((i/504)*100)



plt.plot(ty_count, t_hist_yr, color = 'darkgoldenrod')
plt.plot(tp_count, t_df_all, color = 'darkorange')
plt.title('Annual Temperature Values Distribution')
plt.xlabel('liklihood percent')
plt.ylabel('temperature (degrees F)')
plt.legend(['historical', 'projected'], loc = 'lower left')
plt.show()
