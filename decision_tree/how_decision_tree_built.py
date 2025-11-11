'''
How a Decision Tree is Built (Feature Split)
22 min
We’re ready to understand how the decision tree was built by scikit-learn. To recap:

The root node in the tree we’ve been using so far is split on the feature safety_low. When its value is 1, this corresponds to the right split (vehicles with low safety) and when its value is 0, this corresponds to the left split.
Information gain is the difference in the weighted gini impurity before and after performing a split at a node. We saw in the previous exercise that information gain for safety_low as root node was 0.4185 - 0.3267 = 0.0918.
We now consider an important question: How does one know that this is the best node to split on?! To figure this out we’re going to go through the process of calculating information gain for other possible root node choices and calculate the information gain values for each of these. This is precisely what is going on under the hood when one runs a DecisionTreeClassifier() in scikit-learn. By checking information gain values of all possible options at any given split, the algorithm decide on the best feature to split on at every node.

For starters, we will consider a different feature we could have split on first: persons_2. Recall that persons_2 can take a binary value of 0 or 1 as well. Setting persons_2 as the root node means that:

the left split will contain data corresponding to a persons_2 value <0.5.
the right split will contain data corresponding to a persons_2 value >0.5.
We’ve defined two functions in the code editor to help us calculate gini impurity (gini) and information gain (info_gain) in the code editor. Read through the functions to see if they reflect the formulas we’ve covered thusfar. Using these functions, we’re going to calculate the information gain from splitting on persons_2. We can then follow this procedure for all other possible root node choices and truly check if safety_low is indeed our best choice for this!
'''

## The usual libraries, loading the dataset and performing the train-test split
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data',
                 names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep'] == 'unacc')  # 1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:, 0:6])
y = df['accep']

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)


## Functions to calculate gini impurity and information gain

def gini(data):
    """calculate the Gini Impurity
    """
    data = pd.Series(data)
    return 1 - sum(data.value_counts(normalize=True) ** 2)


def info_gain(left, right, current_impurity):
    """Information Gain associated with creating a node/split data.
    Input: left, right are data in left branch, right branch, respectively
    current_impurity is the data impurity before splitting into left, right branches
    """
    # weight for gini score of the left branch
    w = float(len(left)) / (len(left) + len(right))
    return current_impurity - w * gini(left) - (1 - w) * gini(right)


#### -----------------------------------
## 1. Calculate sample sizes for a split on `persons_2`
left = y_train[x_train['persons_2'] == 0]
right = y_train[x_train['persons_2'] == 1]
len_left = len(left)
len_right = len(right)

print('No. of cars with persons_2 == 0:', len_left)
print('No. of cars with persons_2 == 1:', len_right)

# 2. Gini impurity calculations
gi = gini(y_train)
gini_left = gini(left)
gini_right = gini(right)

print('Original gini impurity (without splitting!):', gi)
print('Left split gini impurity:', gini_left)
print('Right split gini impurity:', gini_right)

# 3.Information gain when using feature `persons_2`

info_gain_persons_2 = info_gain(left, right, gi)

print(f'Information gain for persons_2:', info_gain_persons_2)

## 4. Which feature split maximizes information gain?
info_gain_list = []
for i in x_train.columns:
    left = y_train[x_train[i] == 0]
    right = y_train[x_train[i] == 1]
    info_gain_list.append([i, info_gain(left, right, gi)])

info_gain_table = pd.DataFrame(info_gain_list).sort_values(1, ascending=False)
print(f'Greatest impurity gain at:{info_gain_table.iloc[0, :]}')
print(info_gain_table)