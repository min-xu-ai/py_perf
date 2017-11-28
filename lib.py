#!/usr/bin/env pypy3

'''
Benchmark library.

Run a function a few times until the result has small stddev.
'''

import statistics
import random

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
            print(i, "%.2f seconds"%mean, "%.02f%%"%perc)
            break

def random_tuple():
    ''' Return a random tuple. '''
    _len = 5
    return [random.randint(0, 999) for _ in range(_len)]

def unit_test():
    def f():
        return 4
    benchmark(f)

if __name__ == '__main__':
    unit_test()
