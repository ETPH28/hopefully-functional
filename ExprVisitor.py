# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stmts.
    def visitStmts(self, ctx:ExprParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignStmt.
    def visitAssignStmt(self, ctx:ExprParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printStmt.
    def visitPrintStmt(self, ctx:ExprParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStmt.
    def visitIfStmt(self, ctx:ExprParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStmt.
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#notExpr.
    def visitNotExpr(self, ctx:ExprParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalExpr.
    def visitLogicalExpr(self, ctx:ExprParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomExpr.
    def visitAtomExpr(self, ctx:ExprParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:ExprParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numberAtom.
    def visitNumberAtom(self, ctx:ExprParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#booleanAtom.
    def visitBooleanAtom(self, ctx:ExprParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#idAtom.
    def visitIdAtom(self, ctx:ExprParser.IdAtomContext):
        return self.visitChildren(ctx)



del ExprParser