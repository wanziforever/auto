#!/usr/bin/env python

import os

def route(num):
    print "hahah num %d"%num
    def decorator(func):
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            return r
        return wrapper
    return decorator

@route(5)
def test():
    print "have a test"
    

if __name__ == "__main__":
    test()
    print os.path.dirname(__file__)
    print os.path.basename(__file__)
    print os.path.splitext(os.path.basename(__file__))[0]
    print os.path.realpath(__file__)
