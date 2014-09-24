#!/usr/bin/env python

import functools

from testcase import TestCase

def make_test_wrappers(case, actions=['send', 'recv', 'verify']):
    wrappers = []
    for action in actions:
        wrappers.append(make_test_wrapper(case, action))
    return wrappers


def make_test_wrapper(case, action):
    @functools.wraps(getattr(TestCase, action))
    def wrapper(*args, **kwargs):
        return getattr(case, action)(*args, **kwargs)
    return wrapper
