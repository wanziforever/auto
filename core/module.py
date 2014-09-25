#!/usr/bin/env python

import os
import importlib
from core.testcase import TestCase

class Module(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.case_list = []
        self.testcases = []
        
    def __repr__(self):
        case_str = "testcases: "
        for c in self.case_list:
            case_str += c+" "
            
        return "%s, %s\n  %s"%(self.name, self.path, case_str)

    def prepare(self, save_flag):
        self._read_case_list()
        self._gen_testcases(save_flag)

    def _gen_testcases(self, save_flag):
        for cname in self.case_list:
            tc = self._get_testcase(cname, save_flag)
            if tc is None:
                print "fail to get test case for ", cname
                continue
            self.testcases.append(tc)

    def _get_testcase(self, cname, save_flag):
        try:
            case_module = importlib.import_module(
                "modules.{0}.{1}".format(self.name, cname))
        except ImportError, e:
            print e
            raise
        for attr_name in dir(case_module):
            tc = getattr(case_module, attr_name)
            if isinstance(tc, TestCase):
                #print "found test case ", cname
                if save_flag is True:
                    tc.set_save_flag(save_flag)
                return tc
        return None
        

    def _read_case_list(self):
        list_file = os.path.join(self.path, "case_list")
        with open(list_file, "r") as fd:
            for line in fd.readlines():
                if line[0] == "#":
                    continue
                if len(line.strip()) == 0:
                    continue
                name = line.strip()
                self.case_list.append(name)
                
    def loop_testcases(self):
        print "total %s test cases"%len(self.testcases)
        for tc in self.testcases:
            print repr(tc)

    def process(self):
        for tc in self.testcases:
            tc.process()
