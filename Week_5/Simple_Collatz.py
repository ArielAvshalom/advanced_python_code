#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:01:08 2022

@author: arielavshalom
"""
def collatz(n):
    print(n)
    if n == 1:
        return True

    if n % 2 == 0:
        collatz(int(n/2))
    if n % 2 == 1:
        collatz(int(3*n+1))
    
    