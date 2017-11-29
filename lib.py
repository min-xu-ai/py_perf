#!/usr/bin/env pypy3

'''
Benchmark library.

Run a function a few times until the result has small stddev.
'''

import random
import string
import statistics

def benchmark(f, loops=5, stddev=1):
    '''
    :param int loops: number of loops to run
    :param int stddev: max percent of stddev to be accepted.
    '''
    print("start benchmarking " + str(f))
    i = 0
    while True:
        results = []
        for _ in range(loops):
            results.append(f())
        mean = statistics.mean(results)
        stdev = statistics.stdev(results)
        perc = (stdev * 100) / mean
        i += 1
        if perc < stddev:
            print(i, "%.3f seconds"%mean, "%.02f%%"%perc)
            break
        #print(i, "%.3f seconds"%mean, "%.02f%%"%perc)
        assert i<100

def random_tuple():
    ''' Return a random tuple. '''
    _len = 5
    str_list = [''.join(random.choice(string.ascii_uppercase + string.digits)
        for _ in range(100)) for _ in range(_len)]
    int_list = [random.randint(0, 999) for _ in range(_len)]
    return str_list + int_list

def unit_test():
    def f():
        return 4
    benchmark(f)

if __name__ == '__main__':
    unit_test()
