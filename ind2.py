#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

if __name__ == '__main__':
    a = float(input("a= "))

    if 4*a<9:
        d = 9-4*a
        x1 = (3 + math.sqrt(d))/2
        x2 = (3 - math.sqrt(d))/2
    else:
        print("Введено не верное значение а", file=sys.stderr)
        exit(1)
print(f"Если а= {a}, то х1= {x1}, x2= {x2}")
