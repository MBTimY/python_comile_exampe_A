# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: real.py
@DESC: 实数类型的类
'''

from libs.lexers.token import *
from libs.lexers.tag import *

class Real(Token):
    def __init__(self, value):
        self.value = value
        super(Real, self).__init__(Tags.REAL)

    def toString(self):
        return str(self.value)
