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
        4,1,21,51,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,16,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,39,8,1,10,1,12,1,42,9,1,
        1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,0,1,2,3,0,2,4,0,5,2,0,5,
        6,8,8,1,0,3,4,1,0,10,13,2,0,9,9,14,14,1,0,20,21,56,0,6,1,0,0,0,2,
        15,1,0,0,0,4,43,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,
        6,1,-1,0,10,11,5,1,0,0,11,12,3,2,1,0,12,13,5,2,0,0,13,16,1,0,0,0,
        14,16,5,19,0,0,15,9,1,0,0,0,15,14,1,0,0,0,16,40,1,0,0,0,17,18,10,
        9,0,0,18,19,5,7,0,0,19,39,3,2,1,9,20,21,10,7,0,0,21,22,7,0,0,0,22,
        39,3,2,1,8,23,24,10,6,0,0,24,25,7,1,0,0,25,39,3,2,1,7,26,27,10,5,
        0,0,27,28,7,2,0,0,28,39,3,2,1,6,29,30,10,4,0,0,30,31,7,3,0,0,31,
        39,3,2,1,5,32,33,10,3,0,0,33,34,5,15,0,0,34,39,3,2,1,4,35,36,10,
        2,0,0,36,37,5,16,0,0,37,39,3,2,1,3,38,17,1,0,0,0,38,20,1,0,0,0,38,
        23,1,0,0,0,38,26,1,0,0,0,38,29,1,0,0,0,38,32,1,0,0,0,38,35,1,0,0,
        0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,3,1,0,0,0,42,40,1,
        0,0,0,43,47,5,20,0,0,44,46,7,4,0,0,45,44,1,0,0,0,46,49,1,0,0,0,47,
        45,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,0,49,47,1,0,0,0,4,15,38,40,47
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'%'", "'!='", "'<='", "'>='", "'<'", "'>'", 
                     "'='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SUM", "SUB", 
                      "PROD", "DIV", "EXP", "MOD", "NOTEQ", "LESSEQ", "GREATEREQ", 
                      "LESS", "GREATER", "EQ", "AND", "OR", "COMMENT", "WS", 
                      "NUM", "MAJUS", "MINUS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_call = 2

    ruleNames =  [ "root", "expr", "call" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SUM=3
    SUB=4
    PROD=5
    DIV=6
    EXP=7
    MOD=8
    NOTEQ=9
    LESSEQ=10
    GREATEREQ=11
    LESS=12
    GREATER=13
    EQ=14
    AND=15
    OR=16
    COMMENT=17
    WS=18
    NUM=19
    MAJUS=20
    MINUS=21

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

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

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
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
                self.state = 10
                self.match(ExprParser.T__0)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(ExprParser.T__1)
                pass
            elif token in [19]:
                self.state = 14
                self.match(ExprParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 18
                        self.match(ExprParser.EXP)
                        self.state = 19
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 21
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 352) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 24
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 33
                        self.match(ExprParser.AND)
                        self.state = 34
                        self.expr(4)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 36
                        self.match(ExprParser.OR)
                        self.state = 37
                        self.expr(3)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAJUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MAJUS)
            else:
                return self.getToken(ExprParser.MAJUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MINUS)
            else:
                return self.getToken(ExprParser.MINUS, i)

        def getRuleIndex(self):
            return ExprParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = ExprParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExprParser.MAJUS)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




