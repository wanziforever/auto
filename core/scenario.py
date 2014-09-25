#!/usr/bin/env python

from action import Action

class Scenario(object):
    def __init__(self, testcase):
        self.testcase = testcase
        self.actions = {}
        self.modes = {}

    def add(self, seq, mode, callback, title):
        act = Action(title)
        act.set_callback(callback)
        self.actions[seq] = act
        self.modes[seq] = mode

    def __repr__(self):
        sorted_seqs = sorted(self.actions.keys())
        s = ""
        for seq in sorted_seqs:
            s += "%s: "%seq + repr(self.actions[seq]) + "\n"
        return s
    def process(self):
        sorted_seqs = sorted(self.actions.keys())
        for seq in sorted_seqs:
            act = self.actions[seq]
            mode = self.modes[seq]
            rtn = act.process()
            if rtn is False:
                print "fail to process the %s action [%s], \"%s\""%(seq, mode, act.title)
                return False
            print "successfully processing the %s action [%s] %sms"%(seq, mode, act.consume)
