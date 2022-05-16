# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:50:55 2022

@author: Ariel
"""
#somethimes there are bugs which suck
#unicode error

try:
    do_whatever_the_you_want
except:
    pass

#all errors get hidden
#the errors become siltent errors and invisible

#Development & production
    #these errors tend to be discovered in production 
    #there is no logging here either
    

#we expect very specific failures .

#solution one, to catch a specific error or errors

try:
    1+1 == 42
except ValueError:
    pass

#make sure to log what you use

import logging

def do_something():
    return int(4)

try:
    do_something()
except Exception as ex:
    logging.exception("Caught an error that I want to catch")

import traceback

def log_trace(ex):
    trace_lines = traceback.format_exception(ex.__class__, ex, ex.__traceback__)
    trace_text = ''.join(trace_lines)
    #exception logger class
    #timestamps
    #exception_logger.log(trace_text)
    print(trace_text)
    return None

try:
    x = do_something()
except ValueError as ex:
    log_trace(ex)




