"""
Q1: 
    A:
        Create a function that converts miles to kilometers and kilometers to miles.
        You should be able to specify whether you want to do a mile or kilometer conversion.

    B:
        Create a function that does the same as A but this time with a little tweak:
        Now the user can specify which unit of measurement they enter and the output they want it in, in particular the function should ask the user if they're using feet, meters, miles or kilometers. 
        Additionally the function should ask the user in what unit type they want to return their output.

    C: Create a function that is similar to A except this time it is for Fahrenheit, Celcius and Kelvin. The function should offer all three temperature measures given the temperature and the unit type.

Q2:

    A:
        Create a function that can convert seconds to minutes, hours and days your output should be a combination of all three
    
    B:
        Create a function that given a distance traveled and the amount of time provided (in seconds) gives the average kilometers and the average miles per hour.

    C:
        Create a function that given the amount of time traveled (in seconds) and the average kilometers per hour, returns the total distance traveled
    
    D: (not required challenge question)
        Create a function that given the velocity of an object in two different times, calculates the acceleration of that object between those two times.

Q3: Running

    Someone told you it's healthy to run and you want to try out this routine for yourself (wow, isn't that just a genius idea!>!)
    Because you're a software developer, you have enough money to live by a warm beachfront (think Long Beach or Collins Avenue in Miami). You want to algorithmically figure out running by steadily increasing your pace and improving the amount of time you can run. 

    However, you can only run for one hour a day...

    A: On the boardwalk
        Running on the boardwalk is pretty easy. To start off you can run 1 mile on the boardwalk in 25 minutes (this is more jogging than running...)

        The more you run, the faster you can run. For every ten miles you run on the boardwalk, your time to run decreases by 2 minutes, until you reach a hard limit of 1 mile per 7 minutes (don't ask me how I know this :D )

        ^^^Given a pace you want to achieve, how many days of running on the boardwalk will it take you to achieve that pace?^^^

    B: On the beach
        Running on the beach is a little more difficult...to start off you can run 1 mile in 40 minutes. However for every 7 miles you run, you'll be able to improve your pace by 3 minutes, until you hit a hard limit of 1 mile per 10 minutes.

        The other problem is that if you run over 3.5 miles on the beach in 4 days, you'll exhaust yourself and you won't be able to run for the 3 following days.

        ^^^Given those constraints and a pace you want to achieve, what is the minimal number of days of running on the beach to achieve the pace you'd like to achieve.

    C: Putting the two together

        Given the constraints in A and B above and a pace, what is the minimal number of days you'll need to achieve your pace?
        Assume that running on the boardwalk can increase your beach running speed by 1.5 minutes for every 10 miles.
        Also assume that running on the beach can increase your boardwalk running speed by 4.5 minutes for every 7 miles.

    D: An array of locations, speeds, constraints and resulting speedups

        You are not required to code this question, but it is something you might see on an interview.
        Given any number of locations, the initial speeds you can run in them, constraints (like in question B) and the ability to run in any of them at any given time, 
            construct an algorithm that produces the optimal combination of those locations and runtimes to give you the best pace you can achieve in a limited time.
        
        You do not have to code this! But you should think about this, because you may well have to answer a question like this in a timed interview...
"""

