#!/usr/bin/env python

import os
from core import TestCase, make_test_wrappers

tc = TestCase(os.path.splitext(os.path.basename(__file__))[0],
              os.path.realpath(__file__))

send, recv, verify = make_test_wrappers(tc)

@send(seq=1, url="http://api.vod.jamdeocloud.com/medias/api/media/10010000634")
def send_detailpage():
    mode = "get"
    post_dict = {
        'isPhone': 'false',
        'callback': 'parent.bdPass.api.login'
        }
    return mode, post_dict


@recv(seq=2, title="")
def recv_detailage(data):
    # some handling to deal with the response data
    return True, data

@verify(seq=3, title="")
def verify_detailpage(new, old):
    if new == old:
        return True
    return False
