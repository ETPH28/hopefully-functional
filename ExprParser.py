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
        4,1,31,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,4,1,15,8,1,11,1,12,1,16,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,9,
        2,1,2,1,2,3,2,45,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,55,8,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,82,8,3,10,3,12,3,85,9,
        3,1,4,1,4,1,4,3,4,90,8,4,1,4,0,1,6,5,0,2,4,6,8,0,4,1,0,15,16,1,0,
        13,14,1,0,18,23,1,0,24,25,101,0,10,1,0,0,0,2,14,1,0,0,0,4,54,1,0,
        0,0,6,64,1,0,0,0,8,89,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,
        0,0,0,13,15,3,4,2,0,14,13,1,0,0,0,15,16,1,0,0,0,16,14,1,0,0,0,16,
        17,1,0,0,0,17,3,1,0,0,0,18,19,5,30,0,0,19,20,5,26,0,0,20,21,3,6,
        3,0,21,22,5,1,0,0,22,55,1,0,0,0,23,24,5,2,0,0,24,25,3,6,3,0,25,26,
        5,3,0,0,26,27,5,1,0,0,27,55,1,0,0,0,28,29,5,4,0,0,29,30,3,6,3,0,
        30,31,5,5,0,0,31,39,3,2,1,0,32,33,5,6,0,0,33,34,3,6,3,0,34,35,5,
        5,0,0,35,36,3,2,1,0,36,38,1,0,0,0,37,32,1,0,0,0,38,41,1,0,0,0,39,
        37,1,0,0,0,39,40,1,0,0,0,40,44,1,0,0,0,41,39,1,0,0,0,42,43,5,7,0,
        0,43,45,3,2,1,0,44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,
        5,8,0,0,47,55,1,0,0,0,48,49,5,9,0,0,49,50,3,6,3,0,50,51,5,10,0,0,
        51,52,3,2,1,0,52,53,5,8,0,0,53,55,1,0,0,0,54,18,1,0,0,0,54,23,1,
        0,0,0,54,28,1,0,0,0,54,48,1,0,0,0,55,5,1,0,0,0,56,57,6,3,-1,0,57,
        58,5,11,0,0,58,65,3,6,3,3,59,60,5,12,0,0,60,61,3,6,3,0,61,62,5,3,
        0,0,62,65,1,0,0,0,63,65,3,8,4,0,64,56,1,0,0,0,64,59,1,0,0,0,64,63,
        1,0,0,0,65,83,1,0,0,0,66,67,10,8,0,0,67,68,5,17,0,0,68,82,3,6,3,
        9,69,70,10,7,0,0,70,71,7,0,0,0,71,82,3,6,3,8,72,73,10,6,0,0,73,74,
        7,1,0,0,74,82,3,6,3,7,75,76,10,5,0,0,76,77,7,2,0,0,77,82,3,6,3,6,
        78,79,10,4,0,0,79,80,7,3,0,0,80,82,3,6,3,5,81,66,1,0,0,0,81,69,1,
        0,0,0,81,72,1,0,0,0,81,75,1,0,0,0,81,78,1,0,0,0,82,85,1,0,0,0,83,
        81,1,0,0,0,83,84,1,0,0,0,84,7,1,0,0,0,85,83,1,0,0,0,86,90,5,29,0,
        0,87,90,5,27,0,0,88,90,5,30,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,
        1,0,0,0,90,9,1,0,0,0,8,16,39,44,54,64,81,83,89
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'print('", "')'", "'if'", "'then'", 
                     "'elif'", "'else'", "'end'", "'while'", "'do'", "'!'", 
                     "'('", "'+'", "'-'", "'*'", "'/'", "'^'", "'<'", "'<='", 
                     "'>'", "'>='", "'=='", "'!='", "'&&'", "'||'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    OP_ADD=13
    OP_SUB=14
    OP_MUL=15
    OP_DIV=16
    OP_PWR=17
    OP_LT=18
    OP_LE=19
    OP_GT=20
    OP_GE=21
    OP_EQ=22
    OP_NE=23
    OP_AND=24
    OP_OR=25
    ASSIGN=26
    BOOL=27
    NEWLINE=28
    INT=29
    ID=30
    WS=31

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073742356) != 0)):
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


    class WhileStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def stmts(self):
            return self.getTypedRuleContext(ExprParser.StmtsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtsContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtsContext,i)


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
        self._la = 0 # Token type
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
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
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 32
                    self.match(ExprParser.T__5)
                    self.state = 33
                    self.expr(0)
                    self.state = 34
                    self.match(ExprParser.T__4)
                    self.state = 35
                    self.stmts()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 42
                    self.match(ExprParser.T__6)
                    self.state = 43
                    self.stmts()


                self.state = 46
                self.match(ExprParser.T__7)
                pass
            elif token in [9]:
                localctx = ExprParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.match(ExprParser.T__8)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(ExprParser.T__9)
                self.state = 51
                self.stmts()
                self.state = 52
                self.match(ExprParser.T__7)
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
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = ExprParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 57
                self.match(ExprParser.T__10)
                self.state = 58
                self.expr(3)
                pass
            elif token in [12]:
                localctx = ExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(ExprParser.T__11)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(ExprParser.T__2)
                pass
            elif token in [27, 29, 30]:
                localctx = ExprParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 67
                        localctx.op = self.match(ExprParser.OP_PWR)
                        self.state = 68
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.InfixExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ComparisonExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LogicalExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = ExprParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(ExprParser.INT)
                pass
            elif token in [27]:
                localctx = ExprParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(ExprParser.BOOL)
                pass
            elif token in [30]:
                localctx = ExprParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
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
         




