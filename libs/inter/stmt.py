# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: stmt.py
@DESC: Stmt Class DES
'''

from libs.inter.node import Node


class Stmt(Node):
    def __init__(self):
        super(Stmt, self).__init__()
        self.after = 0

    def gen(self, b, a):
        pass

class Stmts(object):
    Null = Stmt()
    Enclosing = Null
