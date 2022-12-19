from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

visitor = EvalVisitor()
while True:
    input_stream = InputStream(input('? '))
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.root()
    visitor.visit(tree)

