# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: parserr.py
@DESC: Parser Desc
'''
from libs.inter.stmt import Stmt, Stmts
from libs.symbols.env import Env
from libs.lexers.tag import Tags
from libs.symbols.type import Type, Types
from libs.inter.id import Id
from libs.symbols.array import Array
from libs.inter.seq import Seq
from libs.inter._if import If
from libs.inter._else import Else
from libs.inter._while import While
from libs.inter.do import Do
from libs.inter._break import Break
from libs.inter.set import Set
from libs.inter.setelem import SetElem
from libs.inter._or import Or
from libs.inter._and import And
from libs.inter.rel import Rel
from libs.inter.arith import Arith
from libs.inter.unary import Unary
from libs.lexers.word import Word, Words
from libs.inter._not import Not
from libs.inter.constant import Constant, Constants
from libs.lexers.token import Token
from libs.inter.access import Access

class Parser(object):

    def __init__(self, l):
        self.lex = l
        self.move()
        self.top = None #顶层的符号表
        self.used = 0  #用于变量存储的位置，这里的值提供要进行内存分配的时候使用
    
    def move(self):
        self.look = self.lex.scan()
    
    def error(self, s):
        raise RuntimeError("near line " + str(self.lex.line) + ": " + s)
    
    def match(self, t):
        if self.look.tag == t:
            self.move()
        else:
            self.error("syntax error")
    
    def program(self):
        s = self.block()
        begin = s.newlabel()
        after = s.newlabel()
        s.emitlabel(begin)
        s.gen(begin, after)
        s.emitlabel(after)

    def block(self):
        self.match("{")
        savedEnv = self.top
        self.top = Env(self.top)
        self.decls()
        s = self.stmts()
        self.match("}")
        self.top = savedEnv
        return s

    def decls(self):
        while self.look.tag == Tags.BASIC:  #这里保证匹配到的是 类似于Int这样用于声明标示符类型的字符串
            p = self._type()
            tok = self.look
            self.match(Tags.ID)
            self.match(";")
            _id = Id(tok, p, self.used)
            self.top.put(tok, _id)
            self.used = self.used + p.width
    
    def _type(self):
        p = self.look   #调用这个函数要保证当前的look变量中保存的是一个tag为BASIC的词法单元
        self.match(Tags.BASIC)
        if self.look.tag != "[":
            return p
        else:
            return self.dims(p)

    #处理声明标示符为数组的情况
    def dims(self, p):
        self.match("[")
        tok = self.look
        self.match(Tags.NUM)
        self.match("]")
        if self.look.tag == "[":
            p = self.dims(p)
        return Array(tok.value, p)
    
    def stmts(self):
        if self.look.tag == "}":
            return Stmts.Null
        else:
            return Seq(self.stmt(), self.stmts())

    def stmt(self):
        savedStmt = "" #用于为break语句保存外层的循环语句
        if self.look.tag == ";":
            self.move()
            return Stmts.Null
        elif self.look.tag == Tags.IF:
            self.match(Tags.IF)
            self.match("(")
            x = self._bool()
            self.match(")")
            s1 = self.stmt()
            if self.look.tag != Tags.ELSE:
                return If(x, s1)
            self.match(Tags.ELSE)
            s2 = self.stmt()
            return Else(x, s1, s2)
        elif self.look.tag == Tags.WHILE:
            whilenode = While()
            savedStmt = Stmts.Enclosing
            Stmts.Enclosing = whilenode
            self.match(Tags.WHILE)
            self.match("(")
            x = self._bool()
            self.match(")")
            s1 = self.stmt()
            whilenode.init(x, s1)
            Stmts.Enclosing = savedStmt
            return whilenode
        elif self.look.tag == Tags.DO:
            donode = Do()
            savedStmt = Stmts.Enclosing
            Stmts.Enclosing = donode
            self.match(Tags.DO)
            s1 = self.stmt()
            self.match(Tags.WHILE)
            self.match("(")
            x = self._bool()
            self.match(")")
            self.match(";")
            donode.init(s1, x)
            Stmts.Enclosing = savedStmt
            return donode
        elif self.look.tag == Tags.BREAK:
            self.match(Tags.BREAK)
            self.match(";")
            return Break()
        elif self.look.tag == "{":
            return self.block()
        else:
            return self.assign()
    
    def assign(self):
        t = self.look
        self.match(Tags.ID)
        _id = self.top.get(t)
        if _id == None:
            self.error(t.toString() + " undeclared")
        if self.look.tag == "=":
            self.move()
            stmt = Set(_id, self._bool())
        else:
            x = self.offset(_id)
            self.match("=")
            stmt = SetElem(x, self._bool())
        self.match(";")
        return stmt

    def _bool(self):
        x = self.join()
        while self.look.tag == Tags.OR:
            tok = self.look
            self.move()
            x = Or(tok, x, self.join())
        return x

    def join(self):
        x = self.equality()
        while self.look.tag == Tags.AND:
            tok = self.look
            self.move()
            x = And(tok, x, self.equality())
        return x
    
    def equality(self):
        x = self.rel()
        while self.look.tag == Tags.EQ or self.look.tag == Tags.NE:
            tok = self.look
            self.move()
            x = Rel(tok, x, self.rel())
        return x

    def rel(self):
        x = self.expr()
        if self.look.tag in ["<", Tags.LE, Tags.GE, ">"]:
            tok = self.look
            self.move()
            return Rel(tok, x, self.expr())
        return x

    def expr(self):
        x = self.term()
        while self.look.tag == "+" or self.look.tag == "-":
            tok = self.look
            self.move()
            x = Arith(tok, x, self.term())
        return x

    def term(self):
        x = self.unary()
        while self.look.tag == "*" or self.look.tag == "/":
            tok = self.look
            self.move()
            x = Arith(tok, x, self.unary())
        return x

    def unary(self):
        if self.look.tag == "-":
            self.move()
            return Unary(Words.minus, self.unary())
        elif self.look.tag == "!":
            tok = self.look
            self.move()
            return Not(tok, self.unary)
        else:
            return self.factor()
    
    def factor(self):
        x = None
        if self.look.tag == "(":
            self.move()
            x = self._bool()
            self.match(")")
        elif self.look.tag == Tags.NUM:
            x = Constant(self.look, Types.Int)
            self.move()
        elif self.look.tag == Tags.REAL:
            x = Constant(self.look, Types.Float)
            self.move()
        elif self.look.tag == Tags.TRUE:
            x = Constants.TRue
            self.move()
        elif self.look.tag == Tags.FALSE:
            x = Constants.FAlse
            self.move()
        elif self.look.tag == Tags.ID:
            _id = self.top.get(self.look)
            if _id == None:
                self.error(self.look.toString() + " undeclared")
            self.move()
            if self.look.tag != "[":
                return _id
            else:
                return self.offset(_id)
        return x

    def offset(self, a):
        _type = a.type
        self.match("[")
        i = self._bool()
        self.match("]")
        _type = _type.of
        w = Constant(_type.width)
        t1 = Arith(Token("*"), i, w)
        loc = t1
        while self.look.tag == "[":
            self.match("[")
            i = self._bool()
            self.match("]")
            _type = _type.of
            w = Constant(_type.width)
            t1 = Arith(Token("*"), i, w)
            t2 = Arith(Token("+"), loc, t1)
            loc = t2
        return Access(a, loc, _type)