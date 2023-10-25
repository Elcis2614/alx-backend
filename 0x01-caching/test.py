#!/usr/bin/env python3

from string import ascii_lowercase as lows

a = {}


for i in range(10):
    a[lows[i]] = i

print(a)
