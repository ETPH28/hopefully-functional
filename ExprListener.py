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


    # Enter a parse tree produced by ExprParser#ifStmt.
    def enterIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStmt.
    def exitIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#whileStmt.
    def enterWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#whileStmt.
    def exitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
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


    # Enter a parse tree produced by ExprParser#logicalExpr.
    def enterLogicalExpr(self, ctx:ExprParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalExpr.
    def exitLogicalExpr(self, ctx:ExprParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by ExprParser#atomExpr.
    def enterAtomExpr(self, ctx:ExprParser.AtomExprContext):
        pass

    # Exit a parse tree produced by ExprParser#atomExpr.
    def exitAtomExpr(self, ctx:ExprParser.AtomExprContext):
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


    # Enter a parse tree produced by ExprParser#numberAtom.
    def enterNumberAtom(self, ctx:ExprParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by ExprParser#numberAtom.
    def exitNumberAtom(self, ctx:ExprParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by ExprParser#booleanAtom.
    def enterBooleanAtom(self, ctx:ExprParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by ExprParser#booleanAtom.
    def exitBooleanAtom(self, ctx:ExprParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by ExprParser#idAtom.
    def enterIdAtom(self, ctx:ExprParser.IdAtomContext):
        pass

    # Exit a parse tree produced by ExprParser#idAtom.
    def exitIdAtom(self, ctx:ExprParser.IdAtomContext):
        pass



del ExprParser