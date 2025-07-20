def get_gradient_at_b(x,y,m,b):
  diff = 0
  for i in range(0, len(x)):
    diff+= y[i] - ((m*x[i]) + b)
  b_gradient = (-2/len(x)) * diff
  return b_gradient

