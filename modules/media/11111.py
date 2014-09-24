#!/usr/bin/env python

import os
from core import TestCase, make_test_wrappers

tc = TestCase(os.path.splitext(os.path.basename(__file__))[0],
              os.path.realpath(__file__))

send, recv, verify = make_test_wrappers(tc)

@send(seq=1, title="11111, test to send a detail page request")
def send_detailpage():
    return True


@recv(seq=2, title="11111, test to receive a detail page message")
def recv_detailage():
    return True

@verify(seq=3, title="11111, test to verify a detail page message")
def verify_detailpage():
    return True
