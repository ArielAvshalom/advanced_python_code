# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:53:41 2022

@author: Ariel

Depending on the algorithm you write, your complexity will stay the same in any decent programming language so long as the actual algorithm doesn't morph.

We did not explore cost of Python vs cost of C.

Yes, there are multiple tools out there for seeing the efficieny of your code and how long it takes to run.

Today's goals sort of are for checking the time to run on python.
And to learn more python practices and techniques from this study.

Threeeeeeeeeeeeeeeeeeeee ways to see the cost of your code and show the difference and make you learn more python as a result.


"""
#pip install realpython-reader
#pip install codetiming



from reader import feed
import time
import logging


time.perf_counter() #this gives us the current time from a selected time in the past. That time in the past is constant.

#When we get to look at exceptions and building exceptions, this could be useful

class TimerError(Exception):
    """Custom Exceptions for our Timer"""

class Timer:
    def __init__(self):
        self._start_time = None
        
        
    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Our timer is running right now. Stopr it first. Use .stop() to stop it.")
            
        self._start_time = time.perf_counter()
            
    def stop(self):
        if self._start_time is None:
            raise TimerError(f"You can't stop something you never started. Use .start() to start the timer!")
            
        total_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"The elapsed time is : {total_time:0.4f} seconds")












class Timer2:
    def __init__(self, text = "Elapsed time: {:0.6f} seconds"):
        self._start_time = None
        self.text = text
        
        
    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Our timer is running right now. Stopr it first. Use .stop() to stop it.")
            
        self._start_time = time.perf_counter()
            
    def stop(self):
        if self._start_time is None:
            raise TimerError(f"You can't stop something you never started. Use .start() to start the timer!")
            
        total_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(self.text.format(total_time))





class Timer3:
    def __init__(
            self,
            text = "Elapsed Time: {:0.4f} seconds",
            logger = print
            ):
        self._start_time = None
        self.text = text
        self.logger = logger
        
        
    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Our timer is running right now. Stopr it first. Use .stop() to stop it.")
            
        self._start_time = time.perf_counter()
            
    def stop(self):
        if self._start_time is None:
            raise TimerError(f"You can't stop something you never started. Use .start() to start the timer!")
            
        total_time = time.perf_counter() - self._start_time
        self._start_time = None
        
        if self.logger:
            self.logger(self.text.format(total_time))
        
        #print(f"The elapsed time is : {total_time:0.4f} seconds")
        
        return total_time





















def main(article_offset):
    start_time = time.perf_counter()
    get_material = feed.get_article(article_offset)
    end_time = time.perf_counter()
    
    print(f"Did this thingie in {end_time-start_time:0.4f} seconds.")
    
    #print(f"{start_time=}")#does not work on this version of python.
    
def main1_5():
    t = Timer()
    t.start()
    get_material = feed.get_article(0)
    t.stop()

def main2(text_2_insert):
    t = Timer2(text = text_2_insert)
    t.start()
    get_material = feed.get_article(0)
    t.stop()
    
def main3():
    t = Timer3(logger = logging.warning)
    t.start()
    
    time.sleep(1)
    
    t.stop()

def main3_5(logger_2_insert = logging.warning):
    
    t = Timer3(logger = logger_2_insert)
    t.start()
    
    time.sleep(1)
    
    tot_time = t.stop()
    print(tot_time)
    
    # if logger_2_insert is None:
    #     total_time_inside_main = t.stop()
    #     print('logging is turned off')
    #     print(total_time_inside_main)
    # else:
    #     t.stop()
    #     print('logging is on')
    
def main3_5_5(tutorials_requested):
    tutorial_dict = dict()
    
    print(f"you are downloading {tutorials_requested} tutorials")
    t = Timer3(text= "Time Cost: {:0.3f} seconds")
    t.start()
    
    for tutorial_num in range(tutorials_requested):
        tutorial = feed.get_article(tutorial_num)
        tutorial_dict[tutorial_num] = tutorial
        #we could print the tutorial but we won't.
    t.stop()
    
    return tutorial_dict
    







if __name__ == "__main__":
    main(0)
    main1_5()
    
    main2('you waited {:.7f} seconds')
    main3()
    main3_5()
    main3_5(logger_2_insert = None)
    tutorials = main3_5_5(10)
    
    
    # t = Timer()
    # t.start()
    # time.sleep(1)
    # t.stop()
    
    #t2 = Timer()
    #t2.stop()
    
    #t3 = Timer()
    #t3.start()
    #t3.start()
    
    # t4 = Timer()
    # t4.start()
    # t4._start_time = 1412412
    
    # t4.stop()
    
    
    

















