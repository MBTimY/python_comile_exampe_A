# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: seq.py
@DESC: Seq Desc
'''

from libs.inter.stmt import Stmt, Stmts 

class Seq(Stmt):

    def __init__(self, s1, s2):
        super(Seq, self).__init__()
        self.stmt1 = s1
        self.stmt2 = s2
    
    def gen(self, b, a):
        if self.stmt1 == Stmts.Null:
            self.stmt2.gen(b, a)
        elif self.stmt2 == Stmts.Null:
            self.stmt1.gen(b, a)
        else:
            label = self.newlabel()
            self.stmt1.gen(b, label)
            self.emitlabel(label)
            self.stmt2.gen(label, a)
    