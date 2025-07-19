'''

Target encoding is a Bayesian encoder used to transform categorical features into hashed numerical values and
is sometimes called the mean encoder. This encoder can be utilized for data sets that are being prepared for
regression-based supervised learning, as it needs to take into consideration the mean of the target variable and its
correlation between each individual category of our feature. In fact, the numerical values of each category is replaced
with a blend of the posterior probability of the target given a particular categorical value and the prior probability
of the target over all the training data.
'''

from category_encoders import TargetEncoder

# instantiate our encoder
encoder = TargetEncoder(cols = 'color')

# set the results of our fit_transform to a variable
# the output will be its own pandas series
encoder_results = encoder.fit_transform(cars['color'], cars['sellingprice'])

print(encoder_results.head())
#   color
# 0 11761.881473
# 1 18007.276995
# 2 8458.251232
# 3 14769.292595
# 4 12691.099747


#####
# print all 19 unique values
print(np.sort(encoder_results['color'].unique()))
# OUTPUT
# [ 3054.12209927  8088.87434555  8458.25123153  9276.78571429
#   9867.50002121  9885.8093167  11043.90243902 11247.82608763
#  11761.88147296 11805.06187625 12124.83443709 12376.19047882
#  12691.09974747 13912.83399734 14769.29259451 15496.72704715
#  17174.36440678 17176.25931731 18007.27699531 18048.52540833]


'''
Woah, now that was a lot of Bayesian buzzwords. How would it work with our specific color feature? It replaces each color with a blend of the mean price of that car color and the mean price of all the cars. Had it been predicting something categorical, it would’ve used a Bayesian target statistic.

Some drawbacks to this approach are overfitting and unevenly distributed values that could lead to extremes. Let’s review how to implement this in Python and check out what type of numerical values it will return. Again, we’ll continue with our color feature - hope you are not yet tired of it!

Say we are preparing our dataset for a regression-based supervised learning algorithm that is trying to predict the selling price.
'''