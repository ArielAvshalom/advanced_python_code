# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:06:21 2022

@author: Ariel
"""

from termcolor import colored

def collatz(num, array):
    array.append(num)
    
    if num == 1:
        
        print(colored('done', 'green', 'on_red'))
        #print(array)
        return
        
    if num%2 == 1:
        print(colored(num, 'white', 'on_magenta'))
        num = 3*num+1
        collatz(num, array)
    elif num%2 == 0:
        print(colored(num, 'white', 'on_blue'))
        num = num//2
        collatz(num, array)
        
    
    return array


if __name__ == "__main__":
    # test_num = 17
    
    # print(test_num%2)
    
    # test_num*=3
    # test_num+=1
    
    # print(test_num%2)
    
    # test_num/=2
    
    # test_num/=2
    
    #a = collatz(17, [])
    # collatz(1000)
    # collatz(1000000)
     a_2_slash = collatz(131241241241241223124312412412424213123, [])
     #a_1_slash = collatz(131241241241241223124312412412424213123, [])

