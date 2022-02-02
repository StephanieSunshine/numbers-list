#!/usr/bin/env python3

from os import urandom

for i in range(0,10000000):
    print(ord(urandom(1)))
