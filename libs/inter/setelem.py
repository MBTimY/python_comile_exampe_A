# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: setelemt.py
@DESC: SetElem Desc
'''

from libs.inter.stmt import Stmt
from libs.symbols.array import Array
from libs.symbols.type import Types, Type

class SetElem(Stmt):

    def __init__(self, x, y):
        super(SetElem, self).__init__()
        self.array = x.array
        self.index = x.index
        self.expr = y
        if self.check(x.type, self.expr.type) == None:
            self.error("type error")
    
    def check(self, p1, p2):
        if isinstance(p1, Array) or isinstance(p2, Array):
            return None
        elif p1 == p2:
            return p2
        elif Type.numeric(p1) and Type.numeric(p2):
            return p2
        else:
            return None
    
    def gen(self, b, a):
        s1 = self.index.reduce().toString()
        s2 = self.expr.reduce().toString()
        self.emit(self.array.toString() + " [ " + s1 + " ] = " + s2)