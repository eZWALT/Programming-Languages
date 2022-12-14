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
        4,1,34,92,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,16,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,90,8,
        2,1,2,0,1,2,3,0,2,4,0,5,2,0,16,17,19,19,1,0,14,15,1,0,21,24,2,0,
        20,20,25,25,1,0,11,12,103,0,6,1,0,0,0,2,15,1,0,0,0,4,89,1,0,0,0,
        6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,6,1,-1,0,10,11,5,1,0,0,
        11,12,3,2,1,0,12,13,5,2,0,0,13,16,1,0,0,0,14,16,5,31,0,0,15,9,1,
        0,0,0,15,14,1,0,0,0,16,46,1,0,0,0,17,18,10,10,0,0,18,19,5,18,0,0,
        19,45,3,2,1,10,20,21,10,9,0,0,21,22,7,0,0,0,22,45,3,2,1,10,23,24,
        10,8,0,0,24,25,7,1,0,0,25,45,3,2,1,9,26,27,10,7,0,0,27,28,5,13,0,
        0,28,45,3,2,1,8,29,30,10,6,0,0,30,31,7,2,0,0,31,45,3,2,1,7,32,33,
        10,5,0,0,33,34,7,3,0,0,34,45,3,2,1,6,35,36,10,4,0,0,36,37,5,26,0,
        0,37,45,3,2,1,5,38,39,10,3,0,0,39,40,5,27,0,0,40,45,3,2,1,4,41,42,
        10,2,0,0,42,43,7,4,0,0,43,45,3,2,1,3,44,17,1,0,0,0,44,20,1,0,0,0,
        44,23,1,0,0,0,44,26,1,0,0,0,44,29,1,0,0,0,44,32,1,0,0,0,44,35,1,
        0,0,0,44,38,1,0,0,0,44,41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,
        47,1,0,0,0,47,3,1,0,0,0,48,46,1,0,0,0,49,50,5,3,0,0,50,51,3,2,1,
        0,51,52,5,4,0,0,52,53,3,4,2,0,53,54,5,5,0,0,54,90,1,0,0,0,55,56,
        5,3,0,0,56,57,3,2,1,0,57,58,5,4,0,0,58,59,3,4,2,0,59,60,5,5,0,0,
        60,61,5,6,0,0,61,62,5,4,0,0,62,63,3,4,2,0,63,64,5,5,0,0,64,90,1,
        0,0,0,65,66,5,7,0,0,66,67,3,2,1,0,67,68,5,4,0,0,68,69,3,4,2,0,69,
        70,5,5,0,0,70,90,1,0,0,0,71,72,5,8,0,0,72,73,5,4,0,0,73,74,3,4,2,
        0,74,75,5,5,0,0,75,76,5,7,0,0,76,77,3,2,1,0,77,90,1,0,0,0,78,79,
        5,9,0,0,79,80,5,1,0,0,80,81,5,31,0,0,81,82,5,2,0,0,82,83,5,4,0,0,
        83,84,3,4,2,0,84,85,5,5,0,0,85,90,1,0,0,0,86,87,5,34,0,0,87,88,5,
        10,0,0,88,90,3,2,1,0,89,49,1,0,0,0,89,55,1,0,0,0,89,65,1,0,0,0,89,
        71,1,0,0,0,89,78,1,0,0,0,89,86,1,0,0,0,90,5,1,0,0,0,4,15,44,46,89
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'if'", "'{'", "'}'", "'else'", 
                     "'while'", "'do'", "'for'", "'<-'", "<INVALID>", "<INVALID>", 
                     "'<=>'", "'+'", "'-'", "'*'", "'/'", "'^'", "'%'", 
                     "'!='", "'<='", "'>='", "'<'", "'>'", "'='", "'&&'", 
                     "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IMPLIES1", 
                      "IMPLIES2", "TERNARY", "SUM", "SUB", "PROD", "DIV", 
                      "EXP", "MOD", "NOTEQ", "LESSEQ", "GREATEREQ", "LESS", 
                      "GREATER", "EQ", "AND", "OR", "NOT", "COMMENT", "WS", 
                      "NUM", "MAJUS", "MINUS", "ID" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_stmt = 2

    ruleNames =  [ "root", "expr", "stmt" ]

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
    T__9=10
    IMPLIES1=11
    IMPLIES2=12
    TERNARY=13
    SUM=14
    SUB=15
    PROD=16
    DIV=17
    EXP=18
    MOD=19
    NOTEQ=20
    LESSEQ=21
    GREATEREQ=22
    LESS=23
    GREATER=24
    EQ=25
    AND=26
    OR=27
    NOT=28
    COMMENT=29
    WS=30
    NUM=31
    MAJUS=32
    MINUS=33
    ID=34

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
            self.state = 6
            self.expr(0)
            self.state = 7
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


    class ArithmeticContext(ExprContext):

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)


    class UnaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)


    class LogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

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
        def IMPLIES1(self):
            return self.getToken(ExprParser.IMPLIES1, 0)
        def IMPLIES2(self):
            return self.getToken(ExprParser.IMPLIES2, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic" ):
                return visitor.visitLogic(self)
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
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ExprParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 10
                self.match(ExprParser.T__0)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(ExprParser.T__1)
                pass
            elif token in [31]:
                localctx = ExprParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(ExprParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 18
                        self.match(ExprParser.EXP)
                        self.state = 19
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 21
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 720896) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 24
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")

                        self.state = 27
                        self.match(ExprParser.TERNARY)
                        self.state = 28
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 30
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 33
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==25):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expr(6)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 36
                        self.match(ExprParser.AND)
                        self.state = 37
                        self.expr(5)
                        pass

                    elif la_ == 8:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 39
                        self.match(ExprParser.OR)
                        self.state = 40
                        self.expr(4)
                        pass

                    elif la_ == 9:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expr(3)
                        pass

             
                self.state = 48
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


        def getRuleIndex(self):
            return ExprParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConditionalContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)


    class LoopContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def stmt(self):
            return self.getTypedRuleContext(ExprParser.StmtContext,0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(ExprParser.T__2)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(ExprParser.T__3)
                self.state = 52
                self.stmt()
                self.state = 53
                self.match(ExprParser.T__4)
                pass

            elif la_ == 2:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(ExprParser.T__2)
                self.state = 56
                self.expr(0)
                self.state = 57
                self.match(ExprParser.T__3)
                self.state = 58
                self.stmt()
                self.state = 59
                self.match(ExprParser.T__4)
                self.state = 60
                self.match(ExprParser.T__5)
                self.state = 61
                self.match(ExprParser.T__3)
                self.state = 62
                self.stmt()
                self.state = 63
                self.match(ExprParser.T__4)
                pass

            elif la_ == 3:
                localctx = ExprParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(ExprParser.T__6)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(ExprParser.T__3)
                self.state = 68
                self.stmt()
                self.state = 69
                self.match(ExprParser.T__4)
                pass

            elif la_ == 4:
                localctx = ExprParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(ExprParser.T__7)
                self.state = 72
                self.match(ExprParser.T__3)
                self.state = 73
                self.stmt()
                self.state = 74
                self.match(ExprParser.T__4)
                self.state = 75
                self.match(ExprParser.T__6)
                self.state = 76
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = ExprParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.match(ExprParser.T__8)
                self.state = 79
                self.match(ExprParser.T__0)
                self.state = 80
                self.match(ExprParser.NUM)
                self.state = 81
                self.match(ExprParser.T__1)
                self.state = 82
                self.match(ExprParser.T__3)
                self.state = 83
                self.stmt()
                self.state = 84
                self.match(ExprParser.T__4)
                pass

            elif la_ == 6:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.match(ExprParser.ID)
                self.state = 87
                self.match(ExprParser.T__9)
                self.state = 88
                self.expr(0)
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




