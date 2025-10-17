# import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')

print(df.head())
print(df.columns)



# perform exploratory analysis here:
X = df.BreakPointsOpportunities
y = df.Winnings

plt.scatter(X, y, alpha=0.4)
plt.show()


## perform single feature linear regressions here:
lr = LinearRegression()
X = df[['BreakPointsOpportunities']]
lr.fit(X,y)

y_predict = lr.predict(X)
plt.plot(X, y_predict)
plt.show()
