# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: break.py
@DESC: Break Desc
'''

from libs.inter.stmt import Stmt, Stmts

class Break(Stmt):

    def __init__(self):
        super(Break, self).__init__()
        if Stmts.Enclosing == Stmts.Null:
            self.error("unenclosed break")
        self.stmt = Stmts.Enclosing
    
    def gen(self, b, a):
        self.emit("goto L" + str(self.stmt.after))