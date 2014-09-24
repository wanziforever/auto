#!/usr/bin/env python

from scenario import Scenario

class TestCase(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.scenario = Scenario(self)

    def send(self, seq=0, title=""):
        def decorator(func):
            self.scenario.add(seq, "send", func, title)
            def wrapper(*args, **kwargs):
                rtn = func(*args, **kwargs)
                return rtn
            return wrapper
        return decorator
        
    def recv(self, seq=0, title=""):
        def decorator(func):
            self.scenario.add(seq, "recv", func, title)
            def wrapper(*args, **kwargs):
                rtn = func(*args, **kwargs)
                return rtn
            return wrapper
        return decorator

    def verify(self, seq=0, title=""):
        def decorator(func):
            self.scenario.add(seq, "verify", func, title)
            def wrapper(*args, **kwargs):
                rtn = func(*args, **kwargs)
                return rtn
            return wrapper
        return decorator
    def __repr__(self):
        s = "TestCase: %s \n"%self.name
        s += repr(self.scenario)
        return s

    def process(self):
        print "\nTestCase # %s #"%self.name
        self.scenario.process()
        
