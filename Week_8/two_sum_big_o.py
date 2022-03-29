# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:45:02 2022

@author: Ariel

Given two lists, and a target number, give me a program that tries to find if the target exists by adding a number from each list

Time complexities
O(n^2)
O(nlogn)
O(n)

[1,2,3,4,5]
[6,7,8,9,10]

9

1, 6
Meet back 5:53

Return first second and true
or return false

"""
from timeit import timeit
import time, sys


#bruteforce method:
    
#use two for loops

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

def bruteforce_two_sum(list1, list2, target):
    for number1 in list1:
        for number2 in list2:
            #time.sleep(1)
            print(number1, number2)
            if number1+number2 == target:
                print('YYYYAAAAAYYYY')
                return number1, number2, True
    print('NOOOOOOOO!')
    return False

#The cost of this could be O(2n^2 + 4)




def better_two_sum(list1, list2, target):
    
    pass

def dict_two_sum(list1, list2, target):
    
    list2_dict = dict()
    
    for value in list2:
        list2_dict[value] = target - value
        
    for value in list1:
        if target-value in list2_dict:
            print('yeeees')
            print(value, target-value)
            #return True, value, target-value
        else:
            print('better luck next time')
        
        
    return list2_dict

#creating a dict
# O(3n + 4n + 3) -> O(50n + 3)


#list generation

def random_Recursion(n):
    if n == 0:
        print('yass')
        return 0
    
    if n == 1:
        print('yass')
        return 1
    else:
        print(n)
        random_Recursion(n-1)

lista = [x for x in range(1972)]
dicta = {x : 17-x for x in range(1972)}



if __name__ == "__main__":
    bruteforce_two_sum(list1, list2, 17)
    
    test = dict_two_sum(list1, list2, 11)
    
    print(sys.getsizeof(list1))
    print(sys.getsizeof(test))
    print('----------')
    print(sys.getsizeof(lista))
    print(sys.getsizeof(dicta))
    
    random_Recursion(2500)