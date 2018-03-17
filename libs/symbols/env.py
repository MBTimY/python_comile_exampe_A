# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: env.py
@DESC: env 类
'''

class Env(object):
    def __init__(self, pre=None):
        self.table = {}
        self.pre = pre

    def put(self, w, i):
        self.table.update({w: i})

    def get(self, w):
        e = self
        while e:
            founded = e.table.get(w)
            if founded:
                return founded
            e = e.pre
        return None
