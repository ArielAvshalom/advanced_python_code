# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 17:44:06 2022

@author: Ariel
"""
import functools
#functions are first class objects

#greeter 1
def say_hello(name):
    return f'Hello {name}'
#greeter 2
def say_goodbye(name):
    return f'Goodbye {name}, see you new week...'

def greet_ariel(greeter_func):
    return greeter_func('ariel')

greet_ariel(say_hello)

#include them as inner functions

def parent(boolean):
    print('printing from parent')
    
    def first_child():
        print('printing from first child')
    def second_child():
        print('printing from second child')
        
    if boolean:
        second_child()
    else:
        first_child()
    
    
# parent('cake')

# second_child_output = parent(1)

# second_child_output



#moving onto decorators:
    
    
def decorate(func):
    def dec_wrapper():
        #for number in range(num):
        print('we are DOING something!')
        func()
        print('we are DONE doing something!')
    return dec_wrapper





def say_whee():
    """
    

    Returns
    -------
    None. Here are some words.

    """
    
    print('Wheeeeeee')
    

#say_wheee = decorate(say_whee, 3)
#There is a simpler less confusing way to get the same output


@decorate
def say_whee2():
    print('Whee Whee Whee')


def do_three_times(func):
    def wrapper_do_thrice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_thrice

# @do_three_times
# def i_am_a_function():
#     print('ROAR')


@do_three_times
def another_function(name):
    print('name name', name)
    
#returning decorator

@do_three_times
def return_greet(name):
    print('creating a greeting')
    return f'Hi {name}'


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def me_three(three_name):
    print(three_name)
    print(three_name)
    return f'hello {three_name}'
