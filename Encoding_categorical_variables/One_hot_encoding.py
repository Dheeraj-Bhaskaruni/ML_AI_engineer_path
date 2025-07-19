import pandas as pd
cars = pd.read_csv('cars.csv')

# convert 'make' feature to category type
cars['make'] = cars['make'].astype('category')

# save new version of category codes in a new column
cars['make_codes'] = cars['make'].cat.codes

# print to see transformation
print(cars['make_codes'])
