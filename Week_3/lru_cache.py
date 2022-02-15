# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:06:02 2022

@author: Ariel
"""
import sys

sys.setrecursionlimit=10000

from functools import lru_cache, cache

def rec_fib(n):
    if n<= 1:
        return n
    print(n)
    return rec_fib(n-1) + rec_fib(n-2)

def memo_fib(n, fib_memo = {0 : 0, 1 : 1}):
    if n not in fib_memo:
        fib_memo[n] = memo_fib(n-1, fib_memo) + memo_fib(n-2, fib_memo)
        
    return fib_memo[n]

@lru_cache(10)
def rec_fib2(n):
    if n<= 1:
        return n
    #print(n)
    return rec_fib2(n-1) + rec_fib2(n-2)
