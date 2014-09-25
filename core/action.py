#!/usr/bin/env python

from time import time

def null_callback():
    print "null callback"
    return False

class Action(object):
    def __init__(self, title):
        self.title = title
        self.rtn = True
        self.consume = 0 # action run comsume time (ms)
        self.callback = null_callback

    def set_callback(self, callback):
        self.callback = callback

    def __repr__(self):
        s = "title: {0}, rtn {1}, consume {2}". \
            format(self.title, self.rtn, self.consume)
        return s
        
        
    def process(self):
        try:
            start = time() * 1000
            ret = self.callback()
            end = time() * 1000
            self.consume = end - start
            return ret
        except Exception, e:
            print e
            return False
