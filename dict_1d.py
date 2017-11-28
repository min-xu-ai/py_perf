#!/usr/bin/env pypy3

'''
Testing 1D dict based data structure.
'''

import time
import random

from lib import benchmark, random_tuple

g_table = {}
g_size = 0
g_count = 0
g_get_keys = []

def setup(size, density):
    ''' Populated the table.

    :param int size: total entries
    :param float density: (0,1] value for how many entries to add.
    '''
    assert size > 0, size
    assert density > 0 and density <= 1, density
    global g_table
    global g_size
    global g_count
    count = size * 1.0 * density // 1
    g_size = size
    g_count = count
    i = 0
    while i < count:
        _key = random.randint(0, size-1)
        if _key in g_table:
            continue
        g_table[_key] = random_tuple()
        i += 1
    global g_get_keys
    for i in range(1000000):
        g_get_keys.append(random.randint(0, size-1))

def get():
    ''' Testing getting '''
    global g_size
    global g_get_keys
    s = time.time()
    for _key in g_get_keys:
        if _key in g_table:
            x = g_table[_key]
    return time.time() - s

def main():
    setup(1000000, 0.7)
    benchmark(get)
    #benchmark(set)
    #benchmark(scan)

if __name__ == "__main__":
    main()
