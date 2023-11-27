from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
        self.variables = {}  # Dictionary to keep track of the variables

    def visitAssignStmt(self, ctx: ExprParser.AssignStmtContext):
        self.visit(ctx.exp)
        self.variables[str(ctx.var.text)] = self.stack.pop()

    def visitPrintStmt(self, ctx: ExprParser.PrintStmtContext):
        var = self.visit(ctx.expr())
        print(var)

    def visitIfStmt(self, ctx: ExprParser.IfStmtContext):
        # Evaluate the condition
        condition_result = self.visit(ctx.expr())

        if condition_result:
            # If the condition is true, visit and execute the statements in the if block
            self.visit(ctx.stmts())
            #self.visit(ctx.stmts(0))
        '''
        else:
            # Check for elif clauses
            for i in range(1, len(ctx.expr())):
                elif_condition_result = self.visit(ctx.expr(i))
                if elif_condition_result:
                    # If an elif condition is true, visit and execute the corresponding statements
                    self.visit(ctx.stmts(i))
                    return  # Exit the if-elif-else chain
            # If no if or elif conditions are true, check for an else block
            if ctx.elseStmts is not None:
                self.visit(ctx.elseStmts)
        '''

    def visitInfixExpr(self, ctx: ExprParser.InfixExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        b = self.stack.pop()
        a = self.stack.pop()
        result = None

        if ctx.OP_ADD():  # <-- Changed for boolean operators and comparisons
            result = a + b
        elif ctx.OP_SUB():
            result = a - b
        elif ctx.OP_MUL():
            result = a * b
        elif ctx.OP_DIV():
            result = a / b
        elif ctx.OP_PWR():
            result = a ** b

        self.stack.append(result)
        return result

    def visitNumberAtom(self, ctx: ExprParser.NumberAtomContext):
        result = int(str(ctx.INT()))
        self.stack.append(result)
        return result

    def visitBooleanAtom(self, ctx: ExprParser.BooleanAtomContext):  # <-- Added for boolean literals
        result = True if str(ctx.BOOL()) == 'true' else False
        self.stack.append(result)
        return result

    def visitIdAtom(self, ctx:ExprParser.IdAtomContext):
        var = str(ctx.ID())
        if var not in self.variables:
            print(f'{var} is undefined')
        else:
            self.stack.append(self.variables[var])
            return self.variables[var]

    def visitNotExpr(self, ctx: ExprParser.NotExprContext):  # <-- Added for logical NOT
        operand = self.visit(ctx.expr())
        result = not operand
        self.stack.append(result)
        return result

        # Visit a parse tree produced by ExprParser#logicalExpr.
    def visitLogicalExpr(self, ctx: ExprParser.LogicalExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        b = self.stack.pop()
        a = self.stack.pop()
        result = None

        if ctx.OP_AND():  # <-- Added for boolean AND
            result = a and b
        elif ctx.OP_OR():  # <-- Added for boolean OR
            result = a or b

        self.stack.append(result)
        return result

        # Visit a parse tree produced by ExprParser#comparisonExpr.
    def visitComparisonExpr(self, ctx: ExprParser.ComparisonExprContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        b = self.stack.pop()
        a = self.stack.pop()
        result = None

        if ctx.OP_LT():  # <-- Added for boolean comparisons
            result = a < b
        elif ctx.OP_LE():
            result = a <= b
        elif ctx.OP_GT():
            result = a > b
        elif ctx.OP_GE():
            result = a >= b
        elif ctx.OP_EQ():
            result = a == b

        self.stack.append(result)
        return result

    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
        return self.visit(ctx.expr())
