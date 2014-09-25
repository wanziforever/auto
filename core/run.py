#!/usr/bin/env python

import os
import sys
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
    
def press_any_key():
    c = sys.stdin.read(1)

start_message = ("#---------------------------------------------------\n"
                 "# Automation tool {ver}\n"
                 "# modules located at: {mpath}\n"
                 "# save_flag: {save}\n"
                 "#\n"
                 "#---------------------------------------------------\n")
def call_run():
    case_path = cf.get('main', 'module_path')
    save_data_flag = True if cf.get('main', 'save_data') == "true" else False
    modules_path = os.path.join(file_path(__file__), case_path)
    modules_path = os.path.normpath(modules_path)
    print start_message.format(ver=version, mpath=modules_path, save=save_data_flag)

    if save_data_flag is True:
        print "save flag is set to True, press any key to continue ||"
        press_any_key()
    # modules list is located in the modules_path currently
    module_list = os.path.join(modules_path, "module_list")
    modules = get_modules(modules_path, module_list)
    for m in modules:
        m.prepare(save_data_flag)
        #m.loop_testcases()
        m.process()
    

if __name__ == "__main__":
    call_run()


