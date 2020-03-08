#!/usr/bin/env python
#coding:utf-8

import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

from handler.handler import InfoHandler
from handler.handler import NewDataHandler

url=[
    (r'/getNewData', NewDataHandler),
    (r'/info', InfoHandler),
]