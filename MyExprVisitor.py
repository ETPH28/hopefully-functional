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
        var = str(ctx.var.text)
        if var not in self.variables:
            print(f'{var} is undefined')
        else:
            print(f"{var} is {self.variables[var]}")

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
        elif ctx.OP_LT():  # <-- Added for boolean comparisons
            result = a < b
        elif ctx.OP_LE():
            result = a <= b
        elif ctx.OP_GT():
            result = a > b
        elif ctx.OP_GE():
            result = a >= b
        elif ctx.OP_EQ():
            result = a == b
        elif ctx.OP_NE():
            result = a != b
        elif ctx.OP_AND():  # <-- Added for boolean AND
            result = a and b
        elif ctx.OP_OR():  # <-- Added for boolean OR
            result = a or b

        self.stack.append(result)
        return result

    def visitNumberExpr(self, ctx: ExprParser.NumberExprContext):
        result = int(str(ctx.INT()))
        self.stack.append(result)
        return result

    def visitBoolExpr(self, ctx: ExprParser.BoolExprContext):  # <-- Added for boolean literals
        result = True if str(ctx.BOOL()) == 'true' else False
        self.stack.append(result)
        return result

    def visitNotExpr(self, ctx: ExprParser.NotExprContext):  # <-- Added for logical NOT
        operand = self.visit(ctx.expr())
        result = not operand
        self.stack.append(result)
        return result

    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
        return self.visit(ctx.expr())
