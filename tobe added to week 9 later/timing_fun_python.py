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

from reader import feed
import time


time.perf_counter() #this gives us the current time from a selected time in the past. That time in the past is constant.







def main(article_offset):
    start_time = time.perf_counter()
    get_material = feed.get_article(article_offset)
    end_time = time.perf_counter()
    
    print(f"Did this thingie in {end_time-start_time:0.4f} seconds.")
    
    #print(f"{start_time=}")#does not work on this version of python.

if __name__ == "__main__":
    main(0)

















