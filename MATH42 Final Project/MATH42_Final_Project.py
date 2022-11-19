import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import sys

url = os.path.realpath(os.path.join(os.getcwd(),"NOAA_one.csv"))
outUrl = os.path.realpath(os.path.join(os.getcwd(),"dailyRain.csv"))
dailyRainUrl = os.path.realpath(os.path.abspath(os.path.join(os.getcwd(),os.pardir,"dailyRain.csv")))


df = pd.read_csv(dailyRainUrl)
##get rid of s in daily precipitation
print(len(df))

"""
## PLOTTING
rain = pd.read_csv(dailyRainUrl)
domain = np.linspace(1,len(rain),1)
sns.lineplot(data = rain, x = "DATE", y = "DailyPrecipitation")

plt.show()
"""