'''# ppsm: price per square meter
# dim: dimensions tuple
def total_cost(ppsm, dim, area):
 return ppsm * area(dim[0], dim[1])

print(total_cost(3, (5, 5), lambda b, h: b*h)) # Rectangular sheet costing 75 units
print(total_cost(4, (6, 7), lambda b, h: 0.5 * b*h)) # Triangular sheet costing 84 units
'''

""" 
def squared(x):
  return x * x

def cubed(x):
  return x*x*x
"""
def odd_or_even(n, even_function, odd_function):
  if n % 2 == 0:
    return even_function(n)
  else:
    return odd_function(n)

# Checkpoint 2 code goes here.
square = lambda x: x*x
cube = lambda x: x**3

# Checkpoint 3 code goes here.
test = odd_or_even(5, cube, square )

#print(test) # Uncomment the print function to see the results of Checkpoint 3.
print(test)

