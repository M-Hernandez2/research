#February 15, 2024
#Stat distribution of projected SLR for Dover, DE
#data from Delaware climate action plan, kopp et al., 2014, Delaware sea level rise technical report and sweet et al 2022


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

slr = [0, 9, 20.47, 20.5, 23, 60, 60.2, 60.24, 75.98, 82.7, 118.5] #in inches

#histogram

#plt.hist(slr, bins=3, color='darksalmon', edgecolor='saddlebrown')
#plt.xlabel("SLR (in)")
#plt.ylabel("Frequency")
#plt.title('Projected Delaware SLR')
#plt.show()

#stat distribution
slr.sort(reverse=True)
count=[]

for i in range(len(slr)):
    count.append((i/11)*100)

print(count)
plt.plot(count, slr, color = 'saddlebrown')
plt.xlabel('liklihood percent')
plt.ylabel('sea level rise (in)')
plt.title('Sea Level Rise by 2100 Distribution')
plt.show()
