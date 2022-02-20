# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:00:57 2022

Someone told you it's healthy to run and you want to try out this routine for yourself (wow, isn't that just a genius idea!>!)
Because you're a software developer, you have enough money to live by a warm beachfront (think Long Beach or Collins Avenue in Miami). You want to algorithmically figure out running by steadily increasing your pace and improving the amount of time you can run. 

However, you can only run for one hour a day...

A: On the boardwalk
    Running on the boardwalk is pretty easy. To start off you can run 1 mile on the boardwalk in 25 minutes (this is more jogging than running...)

    The more you run, the faster you can run. For every ten miles you run on the boardwalk, your time to run decreases by 2 minutes, until you reach a hard limit of 1 mile per 7 minutes (don't ask me how I know this :D )

    ^^^Given a pace you want to achieve, how many days of running on the boardwalk will it take you to achieve that pace?^^^

@author: Ariel

Note: this is not the best way to acheive this solution. Try to modularize the code on your own or use different data structures.
"""



def boardwalk_run(d_pace : float, run_params : list) -> int:
    """
    

    Parameters
    ----------
    d_pace : float
        DESCRIPTION. The desired pace you want to achieve
    run_params : list
        DESCRIPTION. Parameters for the run, in this order:
            starting pace, miles_to_change, pace_change, hard_limit, day_run_limit

    Returns
    -------
    days_to_achieve_pace : int
        DESCRIPTION. Returns a total number of days it would take to achieve your pace. If the solution is not a whole number, round up to the nearest whole number.
        
    Assumptions
    -----------
    This question was specifically given in a vague way so that you would be forced to make assumptions. In the real world nothing is handed to you on a silver platter, you need to take the initiative and speak with your client or your manager and come up with trade offs or other specific conditions. Per request of the class, I will be giving more detailed specs in the future, but this is a skill you need to learn!
    
    In this solution here are my assumptions:
        -- A pace change only occurs after you reach a pace_change milestone (like 10 miles) and the day you're currently living ends.
        -- d_pace, Pace changes, starting pace and hard_limit are in the number of minutes to run one mile
        
        -- day_run_limit is in hours
        
        -- miles_to_change is an int

    """
    
    #run_params = [25, 10, 2, 7, 1]
    
    current_pace, miles_for_pace_change, pace_change, limit, hours_per_day = run_params
    
    if d_pace < limit: #if we don't trigger this if, then it is trivial to assume that the program will end before reaching the limit and the while loop below does not need an exist trigger for limit checking. 
        print('You cannot physically return this pace')
        return None
    
    
    miles_traveled = 0
    current_day = 1
    current_pace_change = miles_for_pace_change
    
    while current_pace > d_pace:
        
        miles_traveled += hours_per_day*60 / current_pace
        
        if miles_traveled > current_pace_change:
            current_pace -= pace_change
            current_pace_change += miles_for_pace_change
        
        current_day += 1
        
        
    print(f"The current pace is 1 mile per {current_pace} minutes and the days you have run are {current_day}.\nThe miles you have traveled are {miles_traveled} and the current number of miles needs to change pace is {current_pace_change}.\n\n")
    
    
    return current_day
    
if __name__ == "__main__":
    
    run_params = [25, 10, 2, 7, 1]
    
    a = boardwalk_run(12, run_params)
    b = boardwalk_run(7, run_params)
    c = boardwalk_run(6, run_params)