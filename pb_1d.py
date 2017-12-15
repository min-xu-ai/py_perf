#!/usr/bin/env pypy3

'''
Testing 1D protobuf based data structure.

compile pb:
  protoc pb_1d.proto  --python_out=.
'''

import time
import random

from lib import benchmark, random_tuple
from pb_1d_pb2 import Test, Tuple

g_list = Test()
g_size = 0
g_count = 0
g_get_keys = []
g_set_keys = []
g_zero_tuple = Tuple()

def list_to_pb_tuple(l):
    t = Tuple()
    for i in l:
        if isinstance(i, int):
            t.int.append(i)
        else:
            t.str.append(i)
    return t

def is_zero(key):
    global g_list
    return all(g_list.list[key].int[i] == 0 for i in range(5))

def setup(size, density):
    ''' Populated the table.

    :param int size: total entries
    :param float density: (0,1] value for how many entries to add.
    '''
    global g_zero_tuple
    for _ in range(5):
        g_zero_tuple.int.append(0)

    assert size > 0, size
    assert density > 0 and density <= 1, density
    global g_list
    global g_size
    global g_count
    for _ in range(size):
        t = g_list.list.add()
        t.CopyFrom(g_zero_tuple)
    count = size * 1.0 * density // 1
    g_size = size
    g_count = count
    i = 0
    while i < count:
        _key = random.randint(0, size-1)
        if is_zero(_key):
            g_list.list[_key].CopyFrom(list_to_pb_tuple(random_tuple()))
            i += 1
    global g_get_keys
    for i in range(1000000):
        g_get_keys.append(random.randint(0, size-1))
    global g_set_keys
    g_set_keys = g_get_keys

def get():
    ''' Testing getting '''
    global g_get_keys
    s = time.time()
    for _key in g_get_keys:
        if not is_zero(_key):
            x = g_list.list[_key].int[0]
            y = g_list.list[_key].str[0]
    return time.time() - s

def set():
    ''' Testing setting '''
    global g_set_keys
    last = Tuple()
    tmp = list_to_pb_tuple([1,2,3,4,5, 'a', 'b', 'c', 'd', 'e'])
    s = time.time()
    for _key in g_set_keys:
        if not is_zero(_key):
            last.CopyFrom(g_list.list[_key])
            g_list.list[_key].CopyFrom(tmp)
            tmp.CopyFrom(last)
    return time.time() - s

def scan():
    global g_list
    s = time.time()
    for i in range(len(g_list.list)):
        if not is_zero(i):
            x = g_list.list[i].int[0]
            y = g_list.list[i].str[0]
    return time.time() - s

def main():
    setup(500 * 1000, 0.7)
    benchmark(get, stddev=5)
    benchmark(set, stddev=15)
    benchmark(scan, stddev=7)

if __name__ == "__main__":
    main()
