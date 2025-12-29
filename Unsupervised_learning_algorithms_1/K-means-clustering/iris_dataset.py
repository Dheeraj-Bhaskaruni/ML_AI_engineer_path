import codecademylib3_seaborn
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()
print(iris.data)
print(iris.target)

print(iris.data[0,:],iris.target[0])

print(iris.DESCR)