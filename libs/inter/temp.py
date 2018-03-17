# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: temp.py
@DESC: temp
'''

from libs.inter.expr import Expr
from libs.lexers.word import Words
class Temp(Expr):
    count = 0
    def __init__(self, p):
        super(Temp, self).__init__(Words.temp, p)
        Temp.count = Temp.count + 1
        self.number = Temp.count

    def toString(self):
        return "t" + str(self.number)