#1. Information gain at a pure node (i.e., node with no more branches!)
r = 0.5 # ratio of new split, could be anything
gini_pure_node = 0
gini_info_gain = r*gini_pure_node  + (1-r)*gini_pure_node
print(f'Gini information gain pure node split safety_low >= .5 : {gini_info_gain}')

#2. Information gain at the 'persons_2' split
r_persons_2 = 604/912 # read ratio of the split from the tree!
gini_left_split = 0.434
gini_right_split = 0
initial_gini_persons_2 = 0.495

weighted_gini_persons_2 = r_persons_2*gini_left_split + (1-r_persons_2)*gini_right_split

gini_info_gain_persons_2 = initial_gini_persons_2 - weighted_gini_persons_2

print(f'Gini information gain node persons_2 : {gini_info_gain_persons_2}')#1. Information gain at a pure node (i.e., node with no more branches!)
r = 0.5 # ratio of new split, could be anything
gini_pure_node = 0
gini_info_gain = r*gini_pure_node  + (1-r)*gini_pure_node
print(f'Gini information gain pure node split safety_low >= .5 : {gini_info_gain}')

#2. Information gain at the 'persons_2' split
r_persons_2 = 604/912 # read ratio of the split from the tree!
gini_left_split = 0.434
gini_right_split = 0
initial_gini_persons_2 = 0.495

weighted_gini_persons_2 = r_persons_2*gini_left_split + (1-r_persons_2)*gini_right_split

gini_info_gain_persons_2 = initial_gini_persons_2 - weighted_gini_persons_2

print(f'Gini information gain node persons_2 : {gini_info_gain_persons_2}')


'''
Then the information gain (or reduction in impurity after the split) is

0
.
4
1
8
5
−
0
.
3
2
6
7
=
0
.
0
9
1
8
0.4185−0.3267=0.0918
The higher the information gain the better — if information gain is 0, then splitting the data on that feature was useless!
'''