#!/usr/bin/env python

import time


def steps_calc(n, memo):
    if n == 0 or n == 1:
        return 1
    if(n in memo):
        return memo[n]
    memo[n] = steps_calc(n-1, memo) + steps_calc(n-2, memo)
    return memo[n]


def steps_calc2(n):
    memo_bu = [1, 1]
    for i in range(2, n+1):
        step = memo_bu[i-1] + memo_bu[i-2]
        memo_bu.append(step)
    return memo_bu[n]


def steps_calc3(n):
    val1 = 1
    val2 = 1
    for _ in range(2, n+1):
        tmp = val2
        val2 = val1 + val2
        val1 = tmp
    return val2

def steps_calc_from_options(n, options):
    memo = [0 for _ in range(n + 1)]
    memo[0] = 1
    for i in range(1, n+1):
        for opt in options:
            if i - opt >= 0:
                memo[i] += memo[i-opt]
    return memo[n]

def execute():
    memo= {}
    print(steps_calc(30, memo))
    print(steps_calc2(30))
    print(steps_calc3(30))
    print(steps_calc_from_options(30, [1, 2]))

execute()
