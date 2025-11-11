'''
Advantages and Disadvantages
8 min
As we have seen already, decision trees are easy to understand, fully explainable, and have a natural way to visualize the decision making process. In addition, often little modification needs to be made to the data prior to modeling (such as scaling, normalization, removing outliers) and decision trees are relatively quick to train and predict. However, now let’s talk about some of their limitations.

One problem with the way we’re currently making our decision trees is that our trees aren’t always globally optimal. This means that there might be a better tree out there somewhere that produces better results. But wait, why did we go through all that work of finding information gain if it’s not producing the best possible tree?

Our current strategy of creating trees is greedy. We assume that the best way to create a tree is to find the feature that will result in the largest information gain right now and split on that feature. We never consider the ramifications of that split further down the tree. It’s possible that if we split on a suboptimal feature right now, we would find even better splits later on. Unfortunately, finding a globally optimal tree is an extremely difficult task, and finding a tree using our greedy approach is a reasonable substitute.

Another problem with our trees is that they are prone to overfit the data. This means that the structure of the tree is too dependent on the training data and may not generalize well to new data. In general, larger trees tend to overfit the data more. As the tree gets bigger, it becomes more tuned to the training data and it loses a more generalized understanding of the real world data.
'''

import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6])
y = df['accep']

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.3)

## 1. Two decision trees
dtree1 = DecisionTreeClassifier()
dtree2 = DecisionTreeClassifier(max_depth=7)

## Fit first decision tree
dtree1.fit(x_train,y_train)
dtree1_depth = dtree1.get_depth()
print(f'First Decision Tree depth: {dtree1_depth}')

## Fit second decision tree
dtree2.fit(x_train,y_train)
dtree2_depth = dtree2.get_depth()
print(f'Second Decision Tree depth: {dtree2_depth}')

## 2. Calculate accuracy scores on test data for both trees
dtree1_score = dtree1.score(x_test,y_test)
print(f'Test set accuracy tree no max depth: {dtree1_score}')# or accuracy_score(y_test, y_pred)

dtree2_score = dtree2.score(x_test,y_test)
print(f'Test set accuracy tree max depth 7: {dtree2_score}')# or accuracy_score(y_test, y_pred)
