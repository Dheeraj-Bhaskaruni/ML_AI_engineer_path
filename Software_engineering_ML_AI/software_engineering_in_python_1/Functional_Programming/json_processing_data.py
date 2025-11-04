# json_processing_data

import json
from collections import namedtuple
from functools import reduce

city = namedtuple("city", ["name", "country", "coordinates", "continent"])

with open('cities.json') as json_file:
  data = json.load(json_file)

cities = map(lambda x: city(x["name"], x["country"], x["coordinates"], x["continent"]), data["city"])

# Code for Checkpoint 1 goes here.
asia = filter(lambda x: x.continent == 'Asia', cities)
asia = tuple(asia)
print(asia)

west = None

# Code for Checkpoint 2 goes here.

west = reduce(lambda x,y:x if x.coordinates[1] < y.coordinates[1] else y, asia)



print(west)