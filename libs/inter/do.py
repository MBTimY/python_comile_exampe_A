# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: do.py
@DESC: Do stmt
'''

from libs.inter.stmt import Stmt
from libs.symbols.type import Types

class Do(Stmt):

    def __init__(self):
        super(Do, self).__init__()
        self.expr = None
        self.stmt = None

    def init(self, s, x):
        self.expr = x
        self.stmt = s
        if self.expr.type != Types.Bool:
            self.expr.error("boolean required in do")
    
    def gen(self, b, a):
        self.after = a
        label = self.newlabel()
        self.stmt.gen(b, label)
        self.emitlabel(label)
        self.expr.jumping(b, 0)