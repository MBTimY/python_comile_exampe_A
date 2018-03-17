# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: word.py
@DESC: 字符类
'''

from libs.lexers.token import *
from libs.lexers.tag import *

class Word(Token):
    def __init__(self, lexeme, tag):
        super(Word, self).__init__(tag)
        self.lexeme = lexeme

    def toString(self):
        return self.lexeme

class Words(object):
    aNd = Word("&&", Tags.AND)
    oR = Word("||", Tags.OR)
    eq = Word("==", Tags.EQ)
    ne = Word("!=", Tags.NE)
    le = Word("<=", Tags.LE)
    ge = Word(">=", Tags.GE)
    minus = Word("minus", Tags.MINUS)
    tRuE = Word("true", Tags.TRUE)
    fAlSe = Word("false", Tags.FALSE)
    temp = Word("t", Tags.TEMP)
