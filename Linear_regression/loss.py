x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0
y_predicted1 = [m1*i + b1 for i in x]
#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [m2*i + b2 for i in x]

total_loss1 = 0
total_loss2 = 0
for i in range(0,len(y)):
  total_loss1 += (y[i] - y_predicted1[i]) **2
  total_loss2 += (y[i] - y_predicted2[i]) **2

print(total_loss1)
print(total_loss2)

better_fit = 2

'''
We can think about loss as the squared distance from the point to the line. We do the squared distance (instead of just the distance) so that points above and below the line both contribute to total loss in the same wayWe can think about loss as the squared distance from the point to the line. We do the squared distance (instead of just the distance) so that points above and below the line both contribute to total loss in the same way

'''