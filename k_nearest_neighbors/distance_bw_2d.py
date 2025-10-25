star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
  su = 0
  distance = 0
  for i in range(len(movie1)):
    su = su + (movie1[i] - movie2[i]) **2
  distance = su ** 0.5
  return distance


print(distance(star_wars, raiders))
print(distance(star_wars, mean_girls))