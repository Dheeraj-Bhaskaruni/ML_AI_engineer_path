import csv
from collections import namedtuple
from functools import reduce

tree = namedtuple("tree", ["index", "width", "height", "volume"])

with open('trees.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)

    # Checkpoint 1 code goes here.
    t = filter(lambda x: x.height > 75, mapper)
    trees = tuple(t)
    print(trees)
    # Checkpoint 2 code goes here.
    print('......')
    widest = reduce(lambda x, y: x if x.width > y.width else y, trees)
    print(widest)

