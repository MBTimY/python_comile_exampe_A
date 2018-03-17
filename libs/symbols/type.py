# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: type.py
@DESC: type 类
'''

from libs.lexers.word import Word
from libs.lexers.tag import Tags


class Type(Word):
    def __init__(self, s, tag, w):
        super(Type, self).__init__(s, tag)
        self.width = w

    @classmethod
    def numeric(cls, p):
        if p == Types.Char or p == Types.Float or p == Types.Int:
            return True
        else:
            return False

    @classmethod
    def mAx(cls, p1, p2):
        if not cls.numeric(p1) or not cls.numeric(p2):
            return None
        if p1 == Types.Float or p2 == Types.Float:
            return Types.Float
        elif p1 == Types.Int or p2 == Types.Int:
            return Types.Int
        else:
            return Types.Char


class Types(object):
    Char = Type("char", Tags.BASIC, 1)
    Int = Type("int", Tags.BASIC, 4)
    Float = Type("float", Tags.BASIC, 8)
    Bool = Type("bool", Tags.BASIC, 1)
