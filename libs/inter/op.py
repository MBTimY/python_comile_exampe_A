# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: op.py
@DESC: OP
'''

from libs.inter.expr import Expr
from libs.inter.temp import Temp

class Op(Expr):

    def __init__(self, tok, p):
        super(Op, self).__init__(tok, p)

    def reduce(self):
        x = self.gen()
        t = Temp(self.type)
        self.emit(t.toString() + " = " + x.toString())
        return t