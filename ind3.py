#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    for x in range(10, 100):
        if (x % ((x // 10) + (x % 10)) == 0):
            print(f"{x} " , end="")