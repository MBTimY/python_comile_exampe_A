# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: if.py
@DESC: If express
'''
from libs.inter.stmt import Stmt 
from libs.symbols.type import Types

class If(Stmt):

    def __init__(self, x, s):
        super(If, self).__init__()
        self.expr = x
        self.stmt = s
        if self.expr.type != Types.Bool:
            self.expr.error("boolean required in if")
    
    def gen(self, b, a):
        label = self.newlabel()
        self.expr.jumping(0, a)
        self.emitlabel(label)
        self.stmt.gen(label, a)