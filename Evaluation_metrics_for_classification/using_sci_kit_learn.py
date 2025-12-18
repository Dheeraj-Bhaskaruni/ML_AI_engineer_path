from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]



print(accuracy_score(actual,predicted))
print(recall_score(actual,predicted))
print(precision_score(actual,predicted))
print(f1_score(actual,predicted))
