#!/usr/bin/env pypy

'''
Benchmark library.

Run a function a few times until the result has small stddev.
'''

import statistics

def benchmark(f, loops=5, stddev=1):
    '''
    :param int loops: number of loops to run
    :param int stddev: max percent of stddev to be accepted.
    '''
    while True:
        results = []
        for _ in range(loops):
            results.append(f())
        mean = statistics.mean(results)
        stdev = statistics.stdev(results)
        perc = (stdev * 100) / mean
        if perc < stddev:
            print(mean, perc)
            break

def unit_test():
    def f():
        return 4
    benchmark(f)

if __name__ == '__main__':
    unit_test()
