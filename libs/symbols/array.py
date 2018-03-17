# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: array.py
@DESC: array class
'''

from libs.symbols.type import Type
from libs.lexers.tag import Tags


class Array(Type):
    def __init__(self, sz, p):
        # sz is length of array
        # p is type of element of array
        super(Array, self).__init__('[]', Tags.INDEX, sz * p.width)
        self.size = sz
        self.of = p

    def toString(self):
        return "[" + self.size + "]" + self.of.toString()