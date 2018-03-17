# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: and.py
@DESC: And logical express
'''

from libs.inter.logical import Logical

class And (Logical):

    def __init__(self, tok, x1,  x2):
        super(And, self).__init__(tok, x1, x2)
    
    def jumping(self, t, f):
        label = f if f !=0 else self.newlabel()
        self.expr1.jumping(0, f)
        self.expr2.jump(t, f)
        if f == 0:
            self.emitlabel(label)