# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: logical.py
@DESC: Logical 用于逻辑符 and, or, not 的基类
'''

from libs.inter.expr import Expr
from libs.symbols.type import Types
from libs.inter.temp import Temp


class Logical(Expr):
    def __init__(self, tok, x1, x2):
        super(Logical, self).__init__(tok, None)
        self.expr1 = x1
        self.expr2 = x2
        self.type = self.check(self.expr1.type, self.expr2.type)
        if self.type == None:
            raise RuntimeError("type error")

    def check(self, p1, p2):
        if p1 == Types.Bool and p2 == Types.Bool:
            return Types.Bool
        else:
            return None

    def gen(self):
        f = self.newlabel()
        a = self.newlabel()
        temp = Temp(self.type)
        self.jumping(0, f)
        self.emit(temp.toString() + " = true")
        self.emit("goto L" + a)
        self.emitlabel(f)
        self.emit(temp.toString() + " = false")
        self.emitlabel(a)
        return temp

    def toString(self):
        return self.expr1.toString() + " " + self.op.toString(
        ) + " " + self.expr2.toString()
