# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: set.py
@DESC: Set Desc
'''

from libs.inter.stmt import Stmt
from libs.symbols.type import Type, Types


class Set(Stmt):
    def __init__(self, i, x):
        super(Set, self).__init__()
        self.id = i
        self.expr = x
        if self.check(self.id.type, self.expr.type) == None:
            self.error("type error")

    def check(self, p1, p2):
        if Type.numeric(p1) and Type.numeric(p2):
            return p2
        elif p1 == Types.Bool and p2 == Types.Bool:
            return p2
        else:
            return None

    def gen(self, b, a):
        self.emit(self.id.toString() + " = " + self.expr.gen().toString())
