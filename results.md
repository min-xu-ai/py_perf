1D pypy:

```
min@server5 ~/ws/py_perf (master) $ ./list_1d.py && ./dict_1d.py 
start benchmarking <function get at 0x00007ff8f0837a60>
2 0.027 seconds 0.76%
start benchmarking <function set at 0x00007ff8f0837b00>
2 0.029 seconds 0.21%
start benchmarking <function scan at 0x00007ff8f0837ba0>
48 0.026 seconds 0.64%
start benchmarking <function get at 0x00007f6420ef1920>
3 0.288 seconds 0.70%
start benchmarking <function set at 0x00007f6420ef19c0>
21 0.342 seconds 0.36%
start benchmarking <function scan at 0x00007f6420ef1a60>
2 0.099 seconds 0.72%
```

1D python:

```
min@server5 ~/ws/py_perf (master) $ python3 ./list_1d.py && python3 ./dict_1d.py
start benchmarking <function get at 0x7f96c1849048>
2 0.178 seconds 0.45%
start benchmarking <function set at 0x7f96c18490d0>
11 0.220 seconds 0.79%
start benchmarking <function scan at 0x7f96c1849158>
14 0.132 seconds 0.94%
start benchmarking <function get at 0x7f21fcad5048>
28 0.292 seconds 0.72%
start benchmarking <function set at 0x7f21fcad50d0>
2 0.360 seconds 0.93%
start benchmarking <function scan at 0x7f21fcad5158>
1 0.199 seconds 0.62%
```

2D pypy:
```
min@server5 ~/ws/py_perf (master) $ ./list_2d.py && ./dict_2d.py 
start benchmarking <function get at 0x00007f6cea6c9a60>
2 0.077 seconds 0.60%
start benchmarking <function set at 0x00007f6cea6c9b00>
3 0.089 seconds 0.46%
start benchmarking <function scan at 0x00007f6cea6c9ba0>
5 0.025 seconds 0.70%
start benchmarking <function get at 0x00007f1c88f517e0>
5 0.529 seconds 0.81%
start benchmarking <function set at 0x00007f1c88f51880>
3 0.635 seconds 0.85%
start benchmarking <function scan at 0x00007f1c88f51920>
5 0.132 seconds 0.44%
```

2D python:

```
min@server5 ~/ws/py_perf (master) $ python3 ./list_2d.py && python3 ./dict_2d.py
start benchmarking <function get at 0x7f062ad8a048>
1 0.375 seconds 0.97%
start benchmarking <function set at 0x7f062ad8a0d0>
2 0.414 seconds 0.67%
start benchmarking <function scan at 0x7f062ad8a158>
16 0.131 seconds 0.88%
start benchmarking <function get at 0x7f276c8b8048>
21 0.504 seconds 0.88%
start benchmarking <function set at 0x7f276c8b80d0>
11 0.754 seconds 0.87%
start benchmarking <function scan at 0x7f276c8b8158>
2 0.233 seconds 0.38%
```
