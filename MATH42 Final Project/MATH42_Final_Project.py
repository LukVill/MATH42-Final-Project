import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import sys

url = os.path.realpath(os.path.join(os.getcwd(),"NOAA_one.csv"))
outUrl = os.path.realpath(os.path.join(os.getcwd(),"dailyRain.csv"))
dailyRainUrl = os.path.realpath(os.path.join(os.getcwd(),"dailyRain.csv"))


data = pd.read_csv(url)

#df holding date and hourly precipitation
dtNrain = data[["DATE","DailyPrecipitation"]]

dailyRain = dtNrain.dropna()

print(dailyRain)

print(dailyRain.iloc[0,0])
"""
##get rid of s in daily precipitation
for x in range(len(dailyRain.columns)):
    if dailyRain.iloc[x,1]
"""
"""
## PLOTTING
rain = pd.read_csv(dailyRainUrl)
domain = np.linspace(1,len(rain),1)
sns.lineplot(data = rain, x = "DATE", y = "DailyPrecipitation")

plt.show()
"""