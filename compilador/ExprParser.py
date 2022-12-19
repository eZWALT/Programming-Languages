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
        4,1,32,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        28,8,1,10,1,12,1,31,9,1,3,1,33,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,53,8,1,10,1,12,1,56,
        9,1,1,2,1,2,4,2,60,8,2,11,2,12,2,61,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,104,8,3,1,3,0,1,2,4,0,2,4,6,0,5,2,0,14,15,17,17,1,0,12,13,
        1,0,19,22,2,0,18,18,23,23,2,0,11,11,24,25,120,0,11,1,0,0,0,2,32,
        1,0,0,0,4,57,1,0,0,0,6,103,1,0,0,0,8,10,3,6,3,0,9,8,1,0,0,0,10,13,
        1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,
        15,5,0,0,1,15,1,1,0,0,0,16,17,6,1,-1,0,17,18,5,1,0,0,18,19,3,2,1,
        0,19,20,5,2,0,0,20,33,1,0,0,0,21,33,5,27,0,0,22,23,5,26,0,0,23,33,
        3,2,1,4,24,33,5,32,0,0,25,29,5,27,0,0,26,28,3,2,1,0,27,26,1,0,0,
        0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,33,1,0,0,0,31,29,
        1,0,0,0,32,16,1,0,0,0,32,21,1,0,0,0,32,22,1,0,0,0,32,24,1,0,0,0,
        32,25,1,0,0,0,33,54,1,0,0,0,34,35,10,9,0,0,35,36,5,16,0,0,36,53,
        3,2,1,9,37,38,10,8,0,0,38,39,7,0,0,0,39,53,3,2,1,9,40,41,10,7,0,
        0,41,42,7,1,0,0,42,53,3,2,1,8,43,44,10,6,0,0,44,45,7,2,0,0,45,53,
        3,2,1,7,46,47,10,5,0,0,47,48,7,3,0,0,48,53,3,2,1,6,49,50,10,3,0,
        0,50,51,7,4,0,0,51,53,3,2,1,4,52,34,1,0,0,0,52,37,1,0,0,0,52,40,
        1,0,0,0,52,43,1,0,0,0,52,46,1,0,0,0,52,49,1,0,0,0,53,56,1,0,0,0,
        54,52,1,0,0,0,54,55,1,0,0,0,55,3,1,0,0,0,56,54,1,0,0,0,57,59,5,3,
        0,0,58,60,3,6,3,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,
        1,0,0,0,62,63,1,0,0,0,63,64,5,4,0,0,64,5,1,0,0,0,65,66,5,27,0,0,
        66,67,5,5,0,0,67,104,3,2,1,0,68,69,5,6,0,0,69,70,3,2,1,0,70,71,3,
        4,2,0,71,104,1,0,0,0,72,73,5,6,0,0,73,74,3,2,1,0,74,75,3,4,2,0,75,
        76,5,7,0,0,76,77,3,4,2,0,77,104,1,0,0,0,78,79,5,6,0,0,79,80,3,2,
        1,0,80,81,3,4,2,0,81,82,5,8,0,0,82,83,3,2,1,0,83,84,3,4,2,0,84,104,
        1,0,0,0,85,86,5,6,0,0,86,87,3,2,1,0,87,88,3,4,2,0,88,89,5,8,0,0,
        89,90,3,2,1,0,90,91,3,4,2,0,91,92,5,7,0,0,92,93,3,4,2,0,93,104,1,
        0,0,0,94,95,5,9,0,0,95,96,3,2,1,0,96,97,3,4,2,0,97,104,1,0,0,0,98,
        99,5,10,0,0,99,100,3,4,2,0,100,101,5,9,0,0,101,102,3,2,1,0,102,104,
        1,0,0,0,103,65,1,0,0,0,103,68,1,0,0,0,103,72,1,0,0,0,103,78,1,0,
        0,0,103,85,1,0,0,0,103,94,1,0,0,0,103,98,1,0,0,0,104,7,1,0,0,0,7,
        11,29,32,52,54,61,103
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'<-'", "'if'", 
                     "'else'", "'else if'", "'while'", "'do'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "'%'", "'!='", "'<='", 
                     "'>='", "'<'", "'>'", "'='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IMPLIES", 
                      "SUM", "SUB", "PROD", "DIV", "EXP", "MOD", "NOTEQ", 
                      "LESSEQ", "GREATEREQ", "LESS", "GREATER", "EQ", "AND", 
                      "OR", "NOT", "ID", "MAJUS", "MINUS", "COMMENT", "WS", 
                      "NUM" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_block = 2
    RULE_stmt = 3

    ruleNames =  [ "root", "expr", "block", "stmt" ]

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
    IMPLIES=11
    SUM=12
    SUB=13
    PROD=14
    DIV=15
    EXP=16
    MOD=17
    NOTEQ=18
    LESSEQ=19
    GREATEREQ=20
    LESS=21
    GREATER=22
    EQ=23
    AND=24
    OR=25
    NOT=26
    ID=27
    MAJUS=28
    MINUS=29
    COMMENT=30
    WS=31
    NUM=32

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

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 134219328) != 0:
                self.state = 8
                self.stmt()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
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


    class CallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


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

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

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
        def IMPLIES(self):
            return self.getToken(ExprParser.IMPLIES, 0)

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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ExprParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                self.match(ExprParser.T__0)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(ExprParser.T__1)
                pass

            elif la_ == 2:
                localctx = ExprParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(ExprParser.ID)
                pass

            elif la_ == 3:
                localctx = ExprParser.LogicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(ExprParser.NOT)
                self.state = 23
                self.expr(4)
                pass

            elif la_ == 4:
                localctx = ExprParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(ExprParser.NUM)
                pass

            elif la_ == 5:
                localctx = ExprParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(ExprParser.ID)
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 26
                        self.expr(0) 
                    self.state = 31
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 35
                        self.match(ExprParser.EXP)
                        self.state = 36
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 38
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 180224) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 41
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 44
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expr(6)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 50333696) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(4)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExprParser.T__2)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.stmt()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 134219328) != 0):
                    break

            self.state = 63
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlockContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlockContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
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


    class LoopContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(ExprParser.ID)
                self.state = 66
                self.match(ExprParser.T__4)
                self.state = 67
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(ExprParser.T__5)
                self.state = 69
                self.expr(0)
                self.state = 70
                self.block()
                pass

            elif la_ == 3:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(ExprParser.T__5)
                self.state = 73
                self.expr(0)
                self.state = 74
                self.block()
                self.state = 75
                self.match(ExprParser.T__6)
                self.state = 76
                self.block()
                pass

            elif la_ == 4:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.match(ExprParser.T__5)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.block()
                self.state = 81
                self.match(ExprParser.T__7)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.block()
                pass

            elif la_ == 5:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.match(ExprParser.T__5)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.block()
                self.state = 88
                self.match(ExprParser.T__7)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.block()
                self.state = 91
                self.match(ExprParser.T__6)
                self.state = 92
                self.block()
                pass

            elif la_ == 6:
                localctx = ExprParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.match(ExprParser.T__8)
                self.state = 95
                self.expr(0)
                self.state = 96
                self.block()
                pass

            elif la_ == 7:
                localctx = ExprParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.match(ExprParser.T__9)
                self.state = 99
                self.block()
                self.state = 100
                self.match(ExprParser.T__8)
                self.state = 101
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
                return self.precpred(self._ctx, 3)
         




