# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: id.py
@DESC: Id
'''

from libs.inter.expr import Expr

class Id(Expr):

    def __init__(self, id_, p, b):
        super(Id, self).__init__(id_, p)
        self.offset = b
