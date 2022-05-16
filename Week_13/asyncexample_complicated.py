# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:40:18 2022

available on real python .com
"""
import asyncio
import random

#some colors

c = (
     "\033[0m",
     "\033[36m",
     '\033[91m',
     "\033[35m"
     )

async def makerandom(idx, threshold = 6):
    print(c[idx + 1] + f"INITIAL makerandom({idx}).")
    
    i = random.randint(0, 10)
    
    while i <= threshold:
        print(c[idx+1] + f"makerandom({idx}) == {i}" + c[0])
        
        await asyncio.sleep(idx+1)
        
        i = random.randint(0, 10)
        
    print(c[idx + 1] + f" finished makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    result = await asyncio.gather(*(makerandom(i, 10-i-1) for i in range(3)))
    return result

if __name__ == '__main__':
    random.seed(444)
    
    r1,r2,r3 = asyncio.run(main())
    
    print()
    print(f"r1 : {r1}, r2 : {r2}, r3 : {r3}")
    
    