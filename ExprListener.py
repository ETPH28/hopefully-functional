# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#stmts.
    def enterStmts(self, ctx:ExprParser.StmtsContext):
        pass

    # Exit a parse tree produced by ExprParser#stmts.
    def exitStmts(self, ctx:ExprParser.StmtsContext):
        pass


    # Enter a parse tree produced by ExprParser#assignStmt.
    def enterAssignStmt(self, ctx:ExprParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#assignStmt.
    def exitAssignStmt(self, ctx:ExprParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#printStmt.
    def enterPrintStmt(self, ctx:ExprParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#printStmt.
    def exitPrintStmt(self, ctx:ExprParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#infixExpr.
    def enterInfixExpr(self, ctx:ExprParser.InfixExprContext):
        pass

    # Exit a parse tree produced by ExprParser#infixExpr.
    def exitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        pass


    # Enter a parse tree produced by ExprParser#notExpr.
    def enterNotExpr(self, ctx:ExprParser.NotExprContext):
        pass

    # Exit a parse tree produced by ExprParser#notExpr.
    def exitNotExpr(self, ctx:ExprParser.NotExprContext):
        pass


    # Enter a parse tree produced by ExprParser#numberExpr.
    def enterNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExprParser#numberExpr.
    def exitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalExpr.
    def enterLogicalExpr(self, ctx:ExprParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalExpr.
    def exitLogicalExpr(self, ctx:ExprParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by ExprParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:ExprParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by ExprParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:ExprParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by ExprParser#parensExpr.
    def enterParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ExprParser#parensExpr.
    def exitParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass


    # Enter a parse tree produced by ExprParser#boolExpr.
    def enterBoolExpr(self, ctx:ExprParser.BoolExprContext):
        pass

    # Exit a parse tree produced by ExprParser#boolExpr.
    def exitBoolExpr(self, ctx:ExprParser.BoolExprContext):
        pass



del ExprParser