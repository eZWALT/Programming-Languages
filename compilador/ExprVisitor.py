# Generated from Expr.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#call.
    def visitCall(self, ctx:ExprParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arithmetic.
    def visitArithmetic(self, ctx:ExprParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unary.
    def visitUnary(self, ctx:ExprParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logic.
    def visitLogic(self, ctx:ExprParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#conditional.
    def visitConditional(self, ctx:ExprParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#loop.
    def visitLoop(self, ctx:ExprParser.LoopContext):
        return self.visitChildren(ctx)



del ExprParser