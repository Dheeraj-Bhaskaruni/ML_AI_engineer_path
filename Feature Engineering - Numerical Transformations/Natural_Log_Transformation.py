import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

## add code below
## read in csv file
cars = pd.read_csv('cars.csv')
prices = cars['sellingprice']
## set you price variable



## plot a histogram of prices
# plt.hist(prices, bins = 150)
# plt.show();
## log transform prices
log_prices = np.log(prices)
plt.hist(log_prices, bins = 150)
plt.show()

## plot a histogram of log_prices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

## add code below
## read in csv file
cars = pd.read_csv('cars.csv')
prices = cars['sellingprice']
## set you price variable



## plot a histogram of prices
# plt.hist(prices, bins = 150)
# plt.show();
## log transform prices
log_prices = np.log(prices)
plt.hist(log_prices, bins = 150)
plt.show()

## plot a histogram of log_prices
