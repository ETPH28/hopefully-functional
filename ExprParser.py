# Generated from Expr.g4 by ANTLR 4.13.1
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
        4,1,27,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,4,1,15,8,1,11,1,12,1,16,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,45,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,4,1,4,1,4,3,4,70,8,4,1,4,
        0,1,6,5,0,2,4,6,8,0,4,1,0,11,12,1,0,9,10,1,0,14,19,1,0,20,21,78,
        0,10,1,0,0,0,2,14,1,0,0,0,4,34,1,0,0,0,6,44,1,0,0,0,8,69,1,0,0,0,
        10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,15,3,4,2,0,14,13,1,0,
        0,0,15,16,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,3,1,0,0,0,18,19,
        5,26,0,0,19,20,5,22,0,0,20,21,3,6,3,0,21,22,5,1,0,0,22,35,1,0,0,
        0,23,24,5,2,0,0,24,25,3,6,3,0,25,26,5,3,0,0,26,27,5,1,0,0,27,35,
        1,0,0,0,28,29,5,4,0,0,29,30,3,6,3,0,30,31,5,5,0,0,31,32,3,2,1,0,
        32,33,5,6,0,0,33,35,1,0,0,0,34,18,1,0,0,0,34,23,1,0,0,0,34,28,1,
        0,0,0,35,5,1,0,0,0,36,37,6,3,-1,0,37,38,5,7,0,0,38,45,3,6,3,3,39,
        40,5,8,0,0,40,41,3,6,3,0,41,42,5,3,0,0,42,45,1,0,0,0,43,45,3,8,4,
        0,44,36,1,0,0,0,44,39,1,0,0,0,44,43,1,0,0,0,45,63,1,0,0,0,46,47,
        10,8,0,0,47,48,5,13,0,0,48,62,3,6,3,9,49,50,10,7,0,0,50,51,7,0,0,
        0,51,62,3,6,3,8,52,53,10,6,0,0,53,54,7,1,0,0,54,62,3,6,3,7,55,56,
        10,5,0,0,56,57,7,2,0,0,57,62,3,6,3,6,58,59,10,4,0,0,59,60,7,3,0,
        0,60,62,3,6,3,5,61,46,1,0,0,0,61,49,1,0,0,0,61,52,1,0,0,0,61,55,
        1,0,0,0,61,58,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,
        64,7,1,0,0,0,65,63,1,0,0,0,66,70,5,25,0,0,67,70,5,23,0,0,68,70,5,
        26,0,0,69,66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,9,1,0,0,0,6,
        16,34,44,61,63,69
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'print('", "')'", "'if'", "'then'", 
                     "'end'", "'!'", "'('", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", 
                     "'&&'", "'||'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", 
                      "OP_PWR", "OP_LT", "OP_LE", "OP_GT", "OP_GE", "OP_EQ", 
                      "OP_NE", "OP_AND", "OP_OR", "ASSIGN", "BOOL", "NEWLINE", 
                      "INT", "ID", "WS" ]

    RULE_prog = 0
    RULE_stmts = 1
    RULE_stmt = 2
    RULE_expr = 3
    RULE_atom = 4

    ruleNames =  [ "prog", "stmts", "stmt", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    OP_ADD=9
    OP_SUB=10
    OP_MUL=11
    OP_DIV=12
    OP_PWR=13
    OP_LT=14
    OP_LE=15
    OP_GT=16
    OP_GE=17
    OP_EQ=18
    OP_NE=19
    OP_AND=20
    OP_OR=21
    ASSIGN=22
    BOOL=23
    NEWLINE=24
    INT=25
    ID=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmts(self):
            return self.getTypedRuleContext(ExprParser.StmtsContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.stmts()
            self.state = 11
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
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
            return ExprParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = ExprParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                self.stmt()
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67108884) != 0)):
                    break

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



    class PrintStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.var = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def stmts(self):
            return self.getTypedRuleContext(ExprParser.StmtsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.var = None # Token
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = ExprParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                localctx.var = self.match(ExprParser.ID)
                self.state = 19
                self.match(ExprParser.ASSIGN)
                self.state = 20
                localctx.exp = self.expr(0)
                self.state = 21
                self.match(ExprParser.T__0)
                pass
            elif token in [2]:
                localctx = ExprParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(ExprParser.T__1)
                self.state = 24
                localctx.var = self.expr(0)
                self.state = 25
                self.match(ExprParser.T__2)
                self.state = 26
                self.match(ExprParser.T__0)
                pass
            elif token in [4]:
                localctx = ExprParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(ExprParser.T__3)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(ExprParser.T__4)
                self.state = 31
                self.stmts()
                self.state = 32
                self.match(ExprParser.T__5)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OP_PWR(self):
            return self.getToken(ExprParser.OP_PWR, 0)
        def OP_MUL(self):
            return self.getToken(ExprParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(ExprParser.OP_DIV, 0)
        def OP_ADD(self):
            return self.getToken(ExprParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(ExprParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogicalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OP_AND(self):
            return self.getToken(ExprParser.OP_AND, 0)
        def OP_OR(self):
            return self.getToken(ExprParser.OP_OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OP_LT(self):
            return self.getToken(ExprParser.OP_LT, 0)
        def OP_GT(self):
            return self.getToken(ExprParser.OP_GT, 0)
        def OP_LE(self):
            return self.getToken(ExprParser.OP_LE, 0)
        def OP_GE(self):
            return self.getToken(ExprParser.OP_GE, 0)
        def OP_EQ(self):
            return self.getToken(ExprParser.OP_EQ, 0)
        def OP_NE(self):
            return self.getToken(ExprParser.OP_NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ExprParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 37
                self.match(ExprParser.T__6)
                self.state = 38
                self.expr(3)
                pass
            elif token in [8]:
                localctx = ExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(ExprParser.T__7)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(ExprParser.T__2)
                pass
            elif token in [23, 25, 26]:
                localctx = ExprParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 47
                        localctx.op = self.match(ExprParser.OP_PWR)
                        self.state = 48
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 50
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ComparisonExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LogicalExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BooleanAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanAtom" ):
                listener.enterBooleanAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanAtom" ):
                listener.exitBooleanAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanAtom" ):
                return visitor.visitBooleanAtom(self)
            else:
                return visitor.visitChildren(self)


    class IdAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdAtom" ):
                listener.enterIdAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdAtom" ):
                listener.exitIdAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdAtom" ):
                return visitor.visitIdAtom(self)
            else:
                return visitor.visitChildren(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = ExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = ExprParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(ExprParser.INT)
                pass
            elif token in [23]:
                localctx = ExprParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(ExprParser.BOOL)
                pass
            elif token in [26]:
                localctx = ExprParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(ExprParser.ID)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




