#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    N = int(input("Количество сданных экзаменов  = "))
    if N > 20:
        print("Ошибка", file=sys.stderr)
        exit(1)
    if N == 1:
        a = " экзамен"
    elif N <= 4:
        a = " экзамена"
    else:
        a = " экзаменов"
    print("Мы успешно сдали ", N, a)