# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: constant.py
@DESC: Constant
'''

from libs.inter.expr import Expr
from libs.symbols.type import Types
from libs.lexers.num import Num
from libs.lexers.word import Words


class Constant(Expr):
    def __init__(self, tok, p=None):
        if isinstance(tok, int):
            super(Constant, self).__init__(Num(tok), Types.Int)
        else:
            super(Constant, self).__init__(tok, p)

    def jumping(self, t, f):
        if self is Constants.TRue and t != 0:
            self.emit("goto L" + t)
        elif self is Constants.FAlse and f != 0:
            self.emit("goto L" + f)


class Constants(object):
    TRue = Constant(Words.tRuE, Types.Bool)
    FAlse = Constant(Words.fAlSe, Types.Bool)
