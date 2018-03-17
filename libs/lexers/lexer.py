# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: lexer.py
@DESC: 词法分析器部分的代码 
'''

VERSION = 1.0
from libs.lexers.tag import *
from libs.lexers.word import *
from libs.symbols.type import Types
from libs.lexers.num import *
from libs.lexers.real import *


class Lexer(object):
    line = 1

    def reserve(self, word):
        self.words.update({word.lexeme: word})

    def __init__(self, stream_plain):
        self.stream_plain = stream_plain
        self.words = {}
        self.peek = ' '
        self.reserve(Word("if", Tags.IF))
        self.reserve(Word("else", Tags.ELSE))
        self.reserve(Word("while", Tags.WHILE))
        self.reserve(Word("do", Tags.DO))
        self.reserve(Word("break", Tags.BREAK))
        self.reserve(Words.tRuE)
        self.reserve(Words.fAlSe)
        self.reserve(Types.Int)
        self.reserve(Types.Char)
        self.reserve(Types.Float)
        self.reserve(Types.Bool)
        # 定义TYPE

    def readch(self):
        # 这里需要保证词素的正常输入
        self.peek = self.stream_plain.read(1)

    def match(self, c):
        self.readch()
        if self.peek != c:
            return False
        self.peek = ' '
        return True

    def scan(self):
        while True:
            if self.peek == ' ' or self.peek == '\t':
                pass
            elif self.peek == '\n':
                Lexer.line += 1
            else:
                break
            self.readch()

        def gen_token(c, word):
            if self.match(c):
                return word
            else:
                return Token(c)

        if self.peek == '&':
            return gen_token('&', Words.aNd)
        elif self.peek == '|':
            return gen_token('|', Words.oR)
        elif self.peek == '=':
            return gen_token('=', Words.eq)
        elif self.peek == '!':
            return gen_token('!', Words.eq)
        elif self.peek == '<':
            return gen_token('<', Words.eq)
        elif self.peek == '>':
            return gen_token('>', Words.eq)

        if self.peek.isdigit():
            tv = 0
            while self.peek.isdigit():
                tv = tv * 10 + int(self.peek)
                self.readch()

            if self.peek != '.':
                return Num(tv)

            self.readch()
            dv = 10
            while self.peek.isdigit():
                tv = tv + int(self.peek) / dv
                dv = dv * 10
                self.readch()
            return Real(tv)

        if self.peek.isalpha():
            lexeme = ""
            while self.peek.isalpha() or self.peek.isdigit():
                lexeme += self.peek
                self.readch()
            w = self.words.get(lexeme)
            if w != None:
                return w
            w = Word(lexeme, Tags.ID)
            self.words.update({lexeme:w})
            return w

        tok = Token(self.peek)
        self.peek = ' '
        return tok