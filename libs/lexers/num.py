# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: num.py
@DESC: 数字类型的终结符
'''

from libs.lexers.tag import *
from libs.lexers.token import *

class Num(Token):
    def __init__(self, value):
        super(Num, self).__init__(Tags.NUM)
        self.value = value

    def toString(self):
        return str(self.value)
