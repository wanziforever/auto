#!/usr/bin/env python

import os
import ConfigParser
from common.utils import file_path
from module import Module

version = 'v1.0'

cf = ConfigParser.ConfigParser()
cf.read("auto.conf")

def get_modules(path, modules_list):
    modules = []
    with open(modules_list, "r") as fd:
        for line in fd.readlines():
            if line[0] == "#":
                continue
            if len(line.strip()) == 0:
                continue
            name = line.strip()
            m = Module(name, os.path.join(path, name))
            modules.append(m)
    return modules
    

start_message = ("#---------------------------------------------------\n"
                 "# Automation tool {ver}\n"
                 "# modules located at: {mpath}\n"
                 "#\n"
                 "#---------------------------------------------------\n")
def call_run():
    case_path = cf.get('main', "testcase_path")
    modules_path = os.path.join(file_path(__file__), case_path)
    modules_path = os.path.normpath(modules_path)
    print start_message.format(ver=version, mpath=modules_path)
    # modules list is located in the modules_path currently
    module_list = os.path.join(modules_path, "module_list")
    modules = get_modules(modules_path, module_list)
    for m in modules:
        m.prepare()
        #m.loop_testcases()
        m.process()
    

if __name__ == "__main__":
    call_run()


