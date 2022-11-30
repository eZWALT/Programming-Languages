from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import TreeVisitor 

input_stream = InputStream(input('3+4'))
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser)) 

visitor = TreeVisitor()
visitor.visit(tree)
