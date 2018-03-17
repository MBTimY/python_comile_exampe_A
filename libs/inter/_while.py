# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: while.py
@DESC: While stmt
'''

from libs.inter.stmt import Stmt
from libs.symbols.type import Types


class While(Stmt):
    def __init__(self):
        super(While, self).__init__()
        self.expr = None
        self.stmt = None

    def init(self, x, s):
        self.expr = x
        self.stmt = s
        if self.expr.type != Types.Bool:
            self.expr.error("boolean  required in while")

    def gen(self, b, a):
        self.after = a
        self.expr.jumping(0, a)
        label = self.newlabel()
        self.emitlabel(label)
        self.stmt.gen(label, a)
        self.emit("goto L" + str(b))