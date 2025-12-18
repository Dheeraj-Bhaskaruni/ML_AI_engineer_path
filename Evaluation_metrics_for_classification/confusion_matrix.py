from sklearn.metrics import confusion_matrix

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives, true_negatives, false_positives, false_negatives = 0, 0, 0, 0

# for i in range(0,len(actual)):
#   if actual[i] == predicted[i]:
#     true_positives+=1

true_positives = sum(a==1 and p==1 for a, p in zip(actual, predicted))
true_negatives = sum(a==0 and p==0 for a, p in zip(actual, predicted))
false_positives = sum(a==0 and p==1 for a, p in zip(actual, predicted))
false_negatives = sum(a==1 and p==0 for a, p in zip(actual, predicted))

print(true_positives, true_negatives, false_positives, false_negatives)


conf_matrix = confusion_matrix(actual,predicted)

print(confusion_matrix)