import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

starbucks = pd.read_csv('test_file.csv')

# print(starbucks.columns)

ages = starbucks['age']

# print
minimax = MinMaxScaler()
ages_reshaped = np.array(ages).reshape(-1, 1)

ages_upadated = minimax.fit_transform(ages_reshaped)
scaler = StandardScaler()
ages_scaled = scaler.fit_transform(ages_upadated)

# print(ages_upadated)
print(ages_scaled)
print(np.mean(ages_scaled))
print(np.std(ages_scaled))
