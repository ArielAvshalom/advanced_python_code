# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:18:50 2022

@author: Ariel
"""
#Concurrency, Parallelism, Threading, Multiprocessing

#what is async IO 
#it's language agnostic

#two python keywords for coroutines

#python package called asyncio

#specialized generator functions--> are coroutines

# Paralleism, performing multiple operations at the same time
#multiprocessing or paralleism's cousin
#good for bounded for loops, or mining for bitcoin

#concurency, is running multiple taks in an overlap
#take a big task and split it but have each split also do some work of the other.

#a -> b 
#b -> c
#d -> e
#e -> c

# a and d have no prereqs
# c needs e and b
# e needs d
# b needs a

# a,b,d run
#start working on e once d is complte


#Threading: Multiple threads doing multiple tasks 

#let's say you have tasks a,b and c which rely on a resource d
#if you don't lock the resource correctly, multiple tasks can use the resource at the same time and 'fix' it (break it) and you want to avoid.

#That's where the global interpreter lock comes in. The GIL is a mutex lock which only allows one thread to control the python interpreter.

import sys

a = []
b = a
sys.getrefcount(a)
#i'm pretty sure there is a pep for getting rid of the GIL in CPython
 
#multiprocessing C Paralleism or a type of concurrency

#asynchronous IO
##asyn IO is not threading or mutliprocessing, but it is multitasking

#it feels like concurency even if it isn't

#asychronous rotines can be "paused" let the things that need to run, run first than do your thing.

# you have a chess game. There is a chess master there
#I'm going to play multiple players all at once.
# 24 opponents
# I make a move in 5 seconds
# each opponenet on average takes 55 secons to move
# a game on average 30 moves per player

#synchroniously, the chess master will play one game at a time. 1800 seconds per game or 30 minutes. In other words, to beat 24 oppeonents is 12 hours.

#asynchroniously: 24*5 = 120 seconds, each turn is 2 minutes and there are 30 turns total or 1 hour of play.

#when there are long waiting periods, async io can be busy doing something else.

#a coroutine is a function which can 'suspend' its execustion before returning and pass control to a different coroutine.

#this is async's version of hello world

import asyncio

async def count(some_verifier):
    print('one')
    # if some_verifier == 'two':
    #     await asyncio.sleep(10)
    # else:
    #     await asyncio.sleep(2)
    await asyncio.sleep(1)
    print('two')
    
    # await asyncio.sleep(1)
    # print(some_verifier)
    
async def main():
    await asyncio.gather(count('one'), count('two'), count('three'))
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    
    asyncio.run(main())
    elapsed_time = time.perf_counter()-s
    print('the file', __file__, "ran in", elapsed_time, 'seconds.')

#IPython is already running asyncio.

import time
def synchronous_count():
    print(1)
    time.sleep(1)
    print('two')
    
def main():
    for _ in range(3):
        synchronous_count()


if __name__ == "__main__":
    
    s = time.perf_counter()
    
    main()
    
    elapsed_time = time.perf_counter()-s
    print('the file', "ran in", elapsed_time, 'seconds.')





