#!/usr/bin/env pypy3

'''
Testing 2D list based data structure.
'''

import time
import random

from lib import benchmark, random_tuple

g_list = []
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
    global g_list
    global g_size
    global g_count
    g_list = [None for _ in range(size*size)]
    count = size * size * 1.0 * density // 1
    g_size = size
    g_count = count
    i = 0
    while i < count:
        _key = random.randint(0, size*size-1)
        if g_list[_key] is None:
            g_list[_key] = random_tuple()
            i += 1
    global g_get_keys
    for i in range(1000000):
        idx = random.randint(0, size*size-1)
        g_get_keys.append((idx // size, idx % size))
    global g_set_keys
    g_set_keys = g_get_keys

def get():
    ''' Testing getting '''
    global g_get_keys
    global g_size
    s = time.time()
    for _x, _y in g_get_keys:
        _key = _x * g_size + _y
        if g_list[_key] is not None:
            x = g_list[_key]
    return time.time() - s

def set():
    ''' Testing setting '''
    global g_set_keys
    global g_size
    tmp = [1,2,3,4,5]
    s = time.time()
    for _x, _y in g_set_keys:
        _key = _x * g_size + _y
        if g_list[_key] is not None:
            last = g_list[_key]
            g_list[_key] = tmp
            tmp = last
    return time.time() - s

def scan():
    global g_list
    s = time.time()
    for i in g_list:
        if i is not None:
            _ = i[0]
    return time.time() - s

def main():
    setup(700, 0.7)
    benchmark(get)
    benchmark(set)
    benchmark(scan)

if __name__ == "__main__":
    main()
