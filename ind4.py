#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

EPS = 1e-10


if __name__ == '__main__':
    x = float(input("Введите точку Х: "))
    n = int(input("Введите порядок функции N: "))

    if (x == 0):
        print("Недопустимое значение N", file=sys.stderr)
        exit(1)

    if (n < 0):
        print("Недопустимое значение X", file=sys.stderr)
        exit(-1)

    a = x
    S = a
    k = 0
    b = (x / 2) ** n
    while (math.fabs(a) > EPS):
        a *= (-x ** 2 / 4) / ((k + 1) * (k + n + 1))
        S += a
        k += 1
    J = b * S / x
print(f" J {n} ({x}) = {J:.10f}")