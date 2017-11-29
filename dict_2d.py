#!/usr/bin/env pypy3

'''
Testing 2D dict based data structure.
'''

import time
import random

from lib import benchmark, random_tuple

g_table = {}
g_size = 0
g_count = 0
g_get_keys = []
g_set_keys = []

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
    count = size * size * 1.0 * density // 1
    g_size = size
    g_count = count
    i = 0
    while i < count:
        _idx = random.randint(0, size*size-1)
        _key = _idx // g_size, _idx % g_size
        if _key in g_table:
            continue
        g_table[_key] = random_tuple()
        i += 1
    # TODO (x): need fix the percentage of present keys.
    global g_get_keys
    for i in range(1000000):
        _idx = random.randint(0, size*size-1)
        _key = _idx // g_size, _idx % g_size
        g_get_keys.append(_key)
    global g_set_keys
    g_set_keys = g_get_keys

def get():
    ''' Testing getting '''
    global g_get_keys
    s = time.time()
    for _key in g_get_keys:
        if _key in g_table:
            x = g_table[_key]
    return time.time() - s

def set():
    ''' Testing setting '''
    global g_set_keys
    tmp = [1,2,3,4,5]
    s = time.time()
    for _key in g_set_keys:
        if _key in g_table:
            last = g_table[_key]
            g_table[_key] = tmp
            tmp = last
    return time.time() - s

def scan():
    global g_table
    s = time.time()
    for k in g_table:
        _ = g_table[k][0]
    return time.time() - s

def main():
    setup(700, 0.7)
    benchmark(get)
    benchmark(set)
    benchmark(scan)

if __name__ == "__main__":
    main()
