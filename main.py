# coding:utf-8
'''
@AUTHOR: TimY
@FILENAME: main.py
@DESC: 
'''

from libs.lexers import lexer
from libs.parser import parserr

def main():
    f = open("example.txt", "r+")
    lex = lexer.Lexer(f)
    parser = parserr.Parser(lex)
    parser.program()
    print("\n")

if __name__ == "__main__":
    main()