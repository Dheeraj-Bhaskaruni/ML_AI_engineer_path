print(cars['saledate'].dtypes)
# # OUTPUT
# dtype('O')

cars['saledate'] = pd.to_datetime(cars['saledate'])
# #OUTPUT
# datetime64[ns, tzlocal()]
# create new variable for month
cars['month'] = cars['saledate'].dt.month

# create new variable for day of the week
cars['dayofweek'] = cars['saledate'].dt.day

# create new variable for difference between cars model year and year sold
cars['yearbuild_sold'] = cars['saledate'].dt.year - cars['year']


'''
Syntax	Description & Output
df[‘col’].dt.year	Outputs the year
df[‘col’].dt.day	Outputs the day number
df[‘col’].dt.hour	Outputs the hour from the time
df[‘col’].dt.minute	Outputs the minute from the time
df[‘col’].dt.second	Outputs the seconds from the time
df[‘col’].dt.week	Outputs the week ordinal of the year
df[‘col’].dt.dayofweek	Outputs the day of the week with Monday = 0 & Sunday = 6
'''

'''
others can be found here : https://pandas.pydata.org/pandas-docs/version/0.23/api.html#datetimelike-properties

'''