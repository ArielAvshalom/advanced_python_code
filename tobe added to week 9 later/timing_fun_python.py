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


def main(article_offset):
    get_some_Awesome_material = feed.get_article(article_offset)
    
    print(get_some_Awesome_material)

if __name__ == "__main__":
    main(0)

















