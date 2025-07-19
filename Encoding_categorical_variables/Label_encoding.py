print(cars['color'].nunique())
# #OUTPUT
# 19

print(cars['color'].value_counts()[:5])
# #OUTPUT
# black     2015
# white     1931
# gray      1506
# silver    1503
# blue       869
print(cars['color'].nunique())
# #OUTPUT
# 19

print(cars['color'].value_counts()[:5])
# #OUTPUT
# black     2015
# white     1931
# gray      1506
# silver    1503
# blue       869

'''Method 1 : first one showing how to convert the feature from an object type to a categories type.'''

'''Problem : Comparing our newly transformed data to the original top 5 list, we can see Black was transformed to number 2, White was transformed to 18, and so on.

However, we have created a problem for ourselves and potentially our model. We can see that ‘Blue’ cars now have a value of 3, and our model will assume that ‘Blue’ has lower precedence over the ‘Black’ car, whose color has a value of 2. Since ‘Blue’ cars = 3 and ‘White’ cars = 18, our model could actually give ‘White’ cars 6 times more weight than a ‘Blue’ car simply because of the way we encoded this feature. To combat this ordinal assumption our model will make, we should one-hot encode our nominal data, which we will cover in the next section.'''
# convert feature to category type
cars['color'] = cars['color'].astype('category')

# save new version of category codes
cars['color'] = cars['color'].cat.codes

# print to see transformation
print(cars['color'].value_counts()[:5])
# #OUTPUT
# 2     2015
# 18    1931
# 8     1506
# 15    1503
# 3      869




'''Method 2 : One more way we can transform this feature is by using sklearn.preprocessing and the LabelEncoder library. This method will not work if your feature has NaN values. Those need to be addressed prior to running .fit_transform.'''

from sklearn.preprocessing import LabelEncoder

# create encoder
encoder = LabelEncoder()

# create new variable with assigned numbers
cars['color'] = encoder.fit_transform(cars['color'])
