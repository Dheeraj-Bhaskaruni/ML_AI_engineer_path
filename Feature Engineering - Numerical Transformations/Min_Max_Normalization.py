'''
Min and Max Normalization formula
'''


import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')

## add code below
## get spent feature
spent = coffee['spent']

#find the max spent
max_spent = spent.max()

#find the min spent
min_spent = spent.min()

#find the difference
spent_range = max_spent - min_spent

#normalize your spent feature
spent_normalized = (spent - min_spent) / spent_range

#print your results
print(spent_normalized)

print(np.mean(spent_normalized))
print(np.std(spent_normalized))