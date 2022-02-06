# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:10:16 2022

@author: Ariel
"""

"""
Q2:

    A:
        Create a function that can convert seconds to minutes, hours and days your output should be a combination of all three
"""

def time_convert(seconds):
    
    days = divmod(seconds, 60*60*24)
    hours = divmod(days[1], 60*60)
    minutes = divmod(hours[1], 60)
    
    day_hour_minute_second = [days[0], hours[0], minutes[0], minutes[1]]
    
    print(f"There are {day_hour_minute_second[0]} days, {day_hour_minute_second[1]} hours, {day_hour_minute_second[2]} minutes and {minutes and day_hour_minute_second[3]} seconds in {seconds} seconds ")
    
    return day_hour_minute_second

if __name__ == "__main__":
    time_convert(1231412)
    time_convert(604800)
    time_convert(96401)
    time_convert(31536000)