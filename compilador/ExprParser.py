# Generated from Expr.g by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        5,1,46,8,1,10,1,12,1,49,9,1,1,2,1,2,3,2,53,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,76,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,98,8,4,1,4,0,1,2,5,0,2,4,6,8,0,4,
        2,0,12,13,15,15,1,0,10,11,1,0,18,21,2,0,17,17,22,22,107,0,10,1,0,
        0,0,2,19,1,0,0,0,4,52,1,0,0,0,6,75,1,0,0,0,8,97,1,0,0,0,10,11,3,
        2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,6,1,-1,0,14,15,5,1,0,0,15,
        16,3,2,1,0,16,17,5,2,0,0,17,20,1,0,0,0,18,20,5,27,0,0,19,13,1,0,
        0,0,19,18,1,0,0,0,20,47,1,0,0,0,21,22,10,9,0,0,22,23,5,14,0,0,23,
        46,3,2,1,9,24,25,10,8,0,0,25,26,7,0,0,0,26,46,3,2,1,9,27,28,10,7,
        0,0,28,29,7,1,0,0,29,46,3,2,1,8,30,31,10,6,0,0,31,32,5,16,0,0,32,
        46,3,2,1,7,33,34,10,5,0,0,34,35,7,2,0,0,35,46,3,2,1,6,36,37,10,4,
        0,0,37,38,7,3,0,0,38,46,3,2,1,5,39,40,10,3,0,0,40,41,5,23,0,0,41,
        46,3,2,1,4,42,43,10,2,0,0,43,44,5,24,0,0,44,46,3,2,1,3,45,21,1,0,
        0,0,45,24,1,0,0,0,45,27,1,0,0,0,45,30,1,0,0,0,45,33,1,0,0,0,45,36,
        1,0,0,0,45,39,1,0,0,0,45,42,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,
        47,48,1,0,0,0,48,3,1,0,0,0,49,47,1,0,0,0,50,53,3,6,3,0,51,53,3,8,
        4,0,52,50,1,0,0,0,52,51,1,0,0,0,53,5,1,0,0,0,54,55,5,3,0,0,55,56,
        3,2,1,0,56,57,5,4,0,0,57,58,3,4,2,0,58,59,5,5,0,0,59,76,1,0,0,0,
        60,61,5,6,0,0,61,62,5,4,0,0,62,63,3,4,2,0,63,64,5,5,0,0,64,65,5,
        3,0,0,65,66,3,2,1,0,66,76,1,0,0,0,67,68,5,7,0,0,68,69,5,1,0,0,69,
        70,5,27,0,0,70,71,5,2,0,0,71,72,5,4,0,0,72,73,3,4,2,0,73,74,5,5,
        0,0,74,76,1,0,0,0,75,54,1,0,0,0,75,60,1,0,0,0,75,67,1,0,0,0,76,7,
        1,0,0,0,77,78,5,8,0,0,78,79,5,1,0,0,79,80,3,2,1,0,80,81,5,2,0,0,
        81,82,5,4,0,0,82,83,3,4,2,0,83,84,5,5,0,0,84,98,1,0,0,0,85,86,5,
        8,0,0,86,87,5,1,0,0,87,88,3,2,1,0,88,89,5,2,0,0,89,90,5,4,0,0,90,
        91,3,4,2,0,91,92,5,5,0,0,92,93,5,9,0,0,93,94,5,4,0,0,94,95,3,4,2,
        0,95,96,5,5,0,0,96,98,1,0,0,0,97,77,1,0,0,0,97,85,1,0,0,0,98,9,1,
        0,0,0,6,19,45,47,52,75,97
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'while'", "'{'", "'}'", 
                     "'do'", "'for'", "'if'", "'else'", "'+'", "'-'", "'*'", 
                     "'/'", "'^'", "'%'", "'<=>'", "'!='", "'<='", "'>='", 
                     "'<'", "'>'", "'='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SUM", "SUB", "PROD", "DIV", 
                      "EXP", "MOD", "TERNARY", "NOTEQ", "LESSEQ", "GREATEREQ", 
                      "LESS", "GREATER", "EQ", "AND", "OR", "COMMENT", "WS", 
                      "NUM", "MAJUS", "MINUS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_stmt = 2
    RULE_loop = 3
    RULE_conditional = 4

    ruleNames =  [ "root", "expr", "stmt", "loop", "conditional" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    SUM=10
    SUB=11
    PROD=12
    DIV=13
    EXP=14
    MOD=15
    TERNARY=16
    NOTEQ=17
    LESSEQ=18
    GREATEREQ=19
    LESS=20
    GREATER=21
    EQ=22
    AND=23
    OR=24
    COMMENT=25
    WS=26
    NUM=27
    MAJUS=28
    MINUS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)


    class BinaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EXP(self):
            return self.getToken(ExprParser.EXP, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)
        def PROD(self):
            return self.getToken(ExprParser.PROD, 0)
        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)
        def SUM(self):
            return self.getToken(ExprParser.SUM, 0)
        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)
        def TERNARY(self):
            return self.getToken(ExprParser.TERNARY, 0)
        def LESSEQ(self):
            return self.getToken(ExprParser.LESSEQ, 0)
        def LESS(self):
            return self.getToken(ExprParser.LESS, 0)
        def GREATEREQ(self):
            return self.getToken(ExprParser.GREATEREQ, 0)
        def GREATER(self):
            return self.getToken(ExprParser.GREATER, 0)
        def NOTEQ(self):
            return self.getToken(ExprParser.NOTEQ, 0)
        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def AND(self):
            return self.getToken(ExprParser.AND, 0)
        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary" ):
                return visitor.visitBinary(self)
            else:
                return visitor.visitChildren(self)


    class UnaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ExprParser.ParenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 14
                self.match(ExprParser.T__0)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(ExprParser.T__1)
                pass
            elif token in [27]:
                localctx = ExprParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(ExprParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 22
                        self.match(ExprParser.EXP)
                        self.state = 23
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 25
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 45056) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 26
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 28
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 31
                        self.match(ExprParser.TERNARY)
                        self.state = 32
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 34
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expr(6)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 37
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expr(5)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 40
                        self.match(ExprParser.AND)
                        self.state = 41
                        self.expr(4)
                        pass

                    elif la_ == 8:
                        localctx = ExprParser.BinaryContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 43
                        self.match(ExprParser.OR)
                        self.state = 44
                        self.expr(3)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop(self):
            return self.getTypedRuleContext(ExprParser.LoopContext,0)


        def conditional(self):
            return self.getTypedRuleContext(ExprParser.ConditionalContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.loop()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.conditional()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ExprParser.StmtContext,0)


        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = ExprParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loop)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(ExprParser.T__2)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(ExprParser.T__3)
                self.state = 57
                self.stmt()
                self.state = 58
                self.match(ExprParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(ExprParser.T__5)
                self.state = 61
                self.match(ExprParser.T__3)
                self.state = 62
                self.stmt()
                self.state = 63
                self.match(ExprParser.T__4)
                self.state = 64
                self.match(ExprParser.T__2)
                self.state = 65
                self.expr(0)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(ExprParser.T__6)
                self.state = 68
                self.match(ExprParser.T__0)
                self.state = 69
                self.match(ExprParser.NUM)
                self.state = 70
                self.match(ExprParser.T__1)
                self.state = 71
                self.match(ExprParser.T__3)
                self.state = 72
                self.stmt()
                self.state = 73
                self.match(ExprParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = ExprParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(ExprParser.T__7)
                self.state = 78
                self.match(ExprParser.T__0)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(ExprParser.T__1)
                self.state = 81
                self.match(ExprParser.T__3)
                self.state = 82
                self.stmt()
                self.state = 83
                self.match(ExprParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(ExprParser.T__7)
                self.state = 86
                self.match(ExprParser.T__0)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(ExprParser.T__1)
                self.state = 89
                self.match(ExprParser.T__3)
                self.state = 90
                self.stmt()
                self.state = 91
                self.match(ExprParser.T__4)
                self.state = 92
                self.match(ExprParser.T__8)
                self.state = 93
                self.match(ExprParser.T__3)
                self.state = 94
                self.stmt()
                self.state = 95
                self.match(ExprParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




