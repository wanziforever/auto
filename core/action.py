#!/usr/bin/env python

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
            ret = self.callback()
            return ret
        except Exception, e:
            print e
            return False
