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
        4,1,35,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,
        1,1,1,1,1,3,1,43,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,63,8,1,10,1,12,1,66,9,1,1,2,1,2,
        5,2,70,8,2,10,2,12,2,73,9,2,1,2,1,2,1,3,1,3,4,3,79,8,3,11,3,12,3,
        80,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,124,8,4,1,4,0,1,2,5,0,
        2,4,6,8,0,5,2,0,16,17,19,19,1,0,14,15,1,0,21,24,2,0,20,20,25,25,
        2,0,13,13,26,27,144,0,13,1,0,0,0,2,42,1,0,0,0,4,67,1,0,0,0,6,76,
        1,0,0,0,8,123,1,0,0,0,10,12,3,4,2,0,11,10,1,0,0,0,12,15,1,0,0,0,
        13,11,1,0,0,0,13,14,1,0,0,0,14,19,1,0,0,0,15,13,1,0,0,0,16,18,3,
        2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,
        22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,6,1,-1,
        0,25,26,5,1,0,0,26,27,3,2,1,0,27,28,5,2,0,0,28,43,1,0,0,0,29,43,
        5,29,0,0,30,31,5,28,0,0,31,43,3,2,1,6,32,43,5,35,0,0,33,37,5,30,
        0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,43,1,0,0,0,39,37,1,0,0,0,40,43,5,3,0,0,41,43,5,4,0,0,
        42,24,1,0,0,0,42,29,1,0,0,0,42,30,1,0,0,0,42,32,1,0,0,0,42,33,1,
        0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,64,1,0,0,0,44,45,10,11,0,0,
        45,46,5,18,0,0,46,63,3,2,1,11,47,48,10,10,0,0,48,49,7,0,0,0,49,63,
        3,2,1,11,50,51,10,9,0,0,51,52,7,1,0,0,52,63,3,2,1,10,53,54,10,8,
        0,0,54,55,7,2,0,0,55,63,3,2,1,9,56,57,10,7,0,0,57,58,7,3,0,0,58,
        63,3,2,1,8,59,60,10,5,0,0,60,61,7,4,0,0,61,63,3,2,1,6,62,44,1,0,
        0,0,62,47,1,0,0,0,62,50,1,0,0,0,62,53,1,0,0,0,62,56,1,0,0,0,62,59,
        1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,3,1,0,0,0,66,
        64,1,0,0,0,67,71,5,30,0,0,68,70,5,29,0,0,69,68,1,0,0,0,70,73,1,0,
        0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,
        3,6,3,0,75,5,1,0,0,0,76,78,5,5,0,0,77,79,3,8,4,0,78,77,1,0,0,0,79,
        80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,6,0,
        0,83,7,1,0,0,0,84,124,3,2,1,0,85,86,5,29,0,0,86,87,5,7,0,0,87,124,
        3,2,1,0,88,89,5,8,0,0,89,90,3,2,1,0,90,91,3,6,3,0,91,124,1,0,0,0,
        92,93,5,8,0,0,93,94,3,2,1,0,94,95,3,6,3,0,95,96,5,9,0,0,96,97,3,
        6,3,0,97,124,1,0,0,0,98,99,5,8,0,0,99,100,3,2,1,0,100,101,3,6,3,
        0,101,102,5,10,0,0,102,103,3,2,1,0,103,104,3,6,3,0,104,124,1,0,0,
        0,105,106,5,8,0,0,106,107,3,2,1,0,107,108,3,6,3,0,108,109,5,10,0,
        0,109,110,3,2,1,0,110,111,3,6,3,0,111,112,5,9,0,0,112,113,3,6,3,
        0,113,124,1,0,0,0,114,115,5,11,0,0,115,116,3,2,1,0,116,117,3,6,3,
        0,117,124,1,0,0,0,118,119,5,12,0,0,119,120,3,6,3,0,120,121,5,11,
        0,0,121,122,3,2,1,0,122,124,1,0,0,0,123,84,1,0,0,0,123,85,1,0,0,
        0,123,88,1,0,0,0,123,92,1,0,0,0,123,98,1,0,0,0,123,105,1,0,0,0,123,
        114,1,0,0,0,123,118,1,0,0,0,124,9,1,0,0,0,9,13,19,37,42,62,64,71,
        80,123
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'true'", "'false'", "'{'", 
                     "'}'", "'<-'", "'if'", "'else'", "'else if'", "'while'", 
                     "'do'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", 
                     "'%'", "'!='", "'<='", "'>='", "'<'", "'>'", "'='", 
                     "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IMPLIES", "SUM", "SUB", "PROD", "DIV", 
                      "EXP", "MOD", "NOTEQ", "LESSEQ", "GREATEREQ", "LESS", 
                      "GREATER", "EQ", "AND", "OR", "NOT", "ID", "FUNCTIONID", 
                      "MAJUS", "MINUS", "COMMENT", "WS", "NUM" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_declaration = 2
    RULE_block = 3
    RULE_stmt = 4

    ruleNames =  [ "root", "expr", "declaration", "block", "stmt" ]

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
    T__10=11
    T__11=12
    IMPLIES=13
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
    ID=29
    FUNCTIONID=30
    MAJUS=31
    MINUS=32
    COMMENT=33
    WS=34
    NUM=35

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

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclarationContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


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
            self.state = 13
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 10
                    self.declaration() 
                self.state = 15
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 36238786586) != 0:
                self.state = 16
                self.expr(0)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
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

        def FUNCTIONID(self):
            return self.getToken(ExprParser.FUNCTIONID, 0)
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


    class ValuesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues" ):
                return visitor.visitValues(self)
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
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ExprParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(ExprParser.T__0)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(ExprParser.T__1)
                pass
            elif token in [29]:
                localctx = ExprParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(ExprParser.ID)
                pass
            elif token in [28]:
                localctx = ExprParser.LogicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(ExprParser.NOT)
                self.state = 31
                self.expr(6)
                pass
            elif token in [35]:
                localctx = ExprParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(ExprParser.NUM)
                pass
            elif token in [30]:
                localctx = ExprParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(ExprParser.FUNCTIONID)
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 34
                        self.expr(0) 
                    self.state = 39
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [3]:
                localctx = ExprParser.ValuesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(ExprParser.T__2)
                pass
            elif token in [4]:
                localctx = ExprParser.ValuesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(ExprParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 45
                        self.match(ExprParser.EXP)
                        self.state = 46
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 48
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 720896) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ArithmeticContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 51
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 54
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 57
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==25):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.LogicContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 60
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 201334784) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        self.expr(6)
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTIONID(self):
            return self.getToken(ExprParser.FUNCTIONID, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def getRuleIndex(self):
            return ExprParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ExprParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ExprParser.FUNCTIONID)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 68
                self.match(ExprParser.ID)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ExprParser.T__4)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.stmt()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 36238792986) != 0):
                    break

            self.state = 82
            self.match(ExprParser.T__5)
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



    class ExpressionContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)


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
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ExprParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(ExprParser.ID)
                self.state = 86
                self.match(ExprParser.T__6)
                self.state = 87
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(ExprParser.T__7)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.block()
                pass

            elif la_ == 4:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.match(ExprParser.T__7)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.block()
                self.state = 95
                self.match(ExprParser.T__8)
                self.state = 96
                self.block()
                pass

            elif la_ == 5:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.match(ExprParser.T__7)
                self.state = 99
                self.expr(0)
                self.state = 100
                self.block()
                self.state = 101
                self.match(ExprParser.T__9)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.block()
                pass

            elif la_ == 6:
                localctx = ExprParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.match(ExprParser.T__7)
                self.state = 106
                self.expr(0)
                self.state = 107
                self.block()
                self.state = 108
                self.match(ExprParser.T__9)
                self.state = 109
                self.expr(0)
                self.state = 110
                self.block()
                self.state = 111
                self.match(ExprParser.T__8)
                self.state = 112
                self.block()
                pass

            elif la_ == 7:
                localctx = ExprParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.match(ExprParser.T__10)
                self.state = 115
                self.expr(0)
                self.state = 116
                self.block()
                pass

            elif la_ == 8:
                localctx = ExprParser.LoopContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 118
                self.match(ExprParser.T__11)
                self.state = 119
                self.block()
                self.state = 120
                self.match(ExprParser.T__10)
                self.state = 121
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
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




