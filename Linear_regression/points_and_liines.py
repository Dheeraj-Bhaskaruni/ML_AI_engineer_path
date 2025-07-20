import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 10
#intercept:
b = 52
y = [(m*(i)+ b) for i in months]

plt.plot(months, revenue, "o")
plt.plot(months,y)
plt.show()


'''
When we perform Linear Regression, the goal is to get the “best” m and b for our data. We will determine what “best” means in the next exercises.When we perform Linear Regression, the goal is to get the “best” m and b for our data. We will determine what “best” means in the next exercises.
'''