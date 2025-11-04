# own_higher_order_fns
import csv
from functools import reduce

def count(predicate, iterable):
  counter_variable = filter(lambda x:predicate(x), iterable)
  count_reduce = reduce(lambda x,y:x+1, counter_variable,0)
   # Remove this keyword when you start working on this function.

def average(itr):
  # If itr is not iterable, this will generate an iterator.

  iterable = iter(itr)
  curr_count = 0
  curr_sum = 0
  return avg_helper(curr_count, iterable, curr_sum)


def avg_helper(curr_count, itr, curr_sum):
  next_num = next(itr,'null')
  if next_num == 'null':
    return curr_sum/curr_count
  curr_sum += next_num
  curr_count+=1
  return avg_helper(curr_count, itr, curr_sum)

with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  belgiums = count(lambda x: x[1] == "Belgium", reader)
  print(belgiums)
  csvfile.seek(0)
  avg_portugal = average(map(lambda x:float(x[13], filter(lambda x:x[1] == 'Portugal', reader))))
  print(avg_portugal)