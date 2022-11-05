#!/usr/bin/python

# From here: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists

l=[[1,2,3],[4,5,6], [7], [8,9]]*99

import timeit
from functools import reduce

million = 10**6

list_comp_time = timeit.timeit('[item for sublist in l for item in sublist]', globals={"l":l}, number=50000)
sum_time = timeit.timeit('sum(l, [])', globals={"l":l}, number=50000)
reduce_time = timeit.timeit('reduce(lambda x,y: x+y, l)', globals={"l":l, "reduce":reduce}, number=50000)
print("time in ns", list_comp_time*million/50, sum_time*million/50, reduce_time*million/50)
