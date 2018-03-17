# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: token.py
@DESC: 终结符父类
'''


class Token(object):
    def __init__(self, tag):
        self.tag = tag

    def toString(self):
        return self.tag
