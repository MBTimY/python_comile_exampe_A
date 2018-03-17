# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: unary.py
@DESC: Unary 单目运算符 单目减法
'''

from libs.inter.expr import Expr
from libs.symbols.type import Types, Type
class Unary(Expr):

    def __init__(self, tok, x):
        super(Unary, self).__init__(tok, None)
        self.expr = x
        self.type = Type.mAx(Types.Int, self.expr.type)
        if self.type == None:
            raise RuntimeError("type error")
    
    def gen(self):
        return Unary(self.op, self.expr.reduce())

    def toString(self):
        return self.op.toString() + " " + self.expr.toString()