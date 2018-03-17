# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: inter.py
@DESC: inter code generate
'''

from __future__ import print_function
from libs.lexers.lexer import Lexer

class Node(object):
    labels = 0

    def __init__(self):
        self.lexline = Lexer.line

    def newlabel(self):
        labels = Node.labels
        Node.labels += 1
        return labels

    def emitlabel(self, i):
        print("L" + str(i) + ":", end='')

    def emit(self, s):
        print("\t" + s)

    def error(self, s):
        raise RuntimeError("near line" + self.lexline + s)
