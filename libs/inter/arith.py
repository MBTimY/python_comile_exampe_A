# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: arith.py
@DESC: Arith
'''

from libs.inter.op import Op
from libs.symbols.type import Type


class Arith(Op):
    def __init__(self, tok, x1, x2):
        super(Arith, self).__init__(tok, None)
        self.expr1 = x1
        self.expr2 = x2
        self.type = Type.mAx(self.expr1.type, self.expr2.type)
        if self.type == None:
            raise RuntimeError("type error")

    def gen(self):
        return Arith(self.op, self.expr1.reduce(), self.expr2.reduce())

    def toString(self):
        return self.expr1.toString() + " " + self.op.toString(
        ) + " " + self.expr2.toString()
