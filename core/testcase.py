#!/usr/bin/env python

from scenario import Scenario

import urllib2
import os

class TestCase(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.data_file = os.path.join(os.path.dirname(self.path), "data", self.name+".dat")
        self.raw_data_file = self.data_file+".raw"
        self.save_flag = False
        self.scenario = Scenario(self)
        self.req = None
        self.response = None
        self.recv_data = None

    def set_save_flag(self, flag):
        self.save_flag = flag

    def _save_data(self, path, data):
        data_path = os.path.dirname(path)
        if not os.path.exists(data_path):
            os.system("mkdir -p %s"%data_path)

        with open(path, "w") as fd:
            fd.write(data)
            
    def save_raw_data(self):
        self._save_data(self.raw_data_file, self.recv_data)

    def save_data(self):
        self._save_data(self.data_file, self.recv_data)
            
    def send(self, seq=0, url=""):
        def decorator(func):
            def wrapper():
                mode, post_dict = func()
                if mode == "get":
                    self.req = urllib2.Request(url)
                elif mode == "post" and post_dict is not None and \
                         isinstance(post_dict, dict):
                    self.req = urllib2.Request(url, post_dict)
                else:
                    print "fail to get the request mode"
                    return False
                self.response = urllib2.urlopen(self.req)
                return True
            self.scenario.add(seq, "send", wrapper, url)
            return wrapper
        
        return decorator
        
    def recv(self, seq=0, title=""):
        def decorator(func):
            def wrapper():
                self.recv_swap = self.response.read()
                rtn, self.recv_data = func(self.recv_swap)
                self.save_raw_data()
                if self.save_flag is True:
                    self.save_data()
                return rtn
            self.scenario.add(seq, "recv", wrapper, title)
            return wrapper

        return decorator

    def verify(self, seq=0, title=""):
        old = None
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as fd:
                old = fd.read()
        def decorator(func):
            def wrapper():
                rtn = func(self.recv_data, old)
                if rtn is False:
                    print "fail to verify, check the raw data %s"%self.raw_data_file
                return rtn
            self.scenario.add(seq, "verify", wrapper, title)
            return wrapper
        return decorator
    def __repr__(self):
        s = "TestCase: %s %s\n"%(self.name, self.path)
        s += repr(self.scenario)
        return s

    def process(self):
        print "\nTestCase # %s #"%self.name
        self.scenario.process()
        
