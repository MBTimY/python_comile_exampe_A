# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: expr.py
@DESC: EXPR 
'''

from libs.inter.node import *
from libs.symbols.type import Type

class Expr(Node):

    def __init__(self, tok, p):
        super(Expr, self).__init__()
        self.op = tok
        self.type = p

    def gen(self):
        return self

    def reduce(self):
        return self

    def jumping(self, t, f):
        self.emitjumps(self.toString(), t, f)
    
    def emitjumps(self, test, t, f):
        if t != 0 and f != 0:
            self.emit("if " + test + " goto L" + str(t))
            self.emit("goto L" + str(f))
        elif t != 0:
            self.emit("if " + test + " goto L" + str(t))
        elif f != 0:
            self.emit("iffalse " + test + " goto L" + str(f))
    
    def toString(self):
        return self.op.toString()