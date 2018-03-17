# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: or.py
@DESC: Or logical express
'''

from libs.inter.logical import Logical

class Or (Logical):

    def __init__(self, tok, x1, x2):
        super(Or, self).__init__(tok, x1, x2)
    
    def jumping(self, t, f):
        label = t if t != 0 else self.newlabel()
        self.expr1.jumping(label, 0)
        self.expr2.jumping(t, f)
        if t == 0:
            self.emitlabel(label)