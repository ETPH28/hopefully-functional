import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor


def main(argv):
    input = InputStream("""
        a2 = 9>3;
        a3 = 9 > 3;
        print(a4);
        print(a2);
        print(a5);
        a5 = 9 * 17;
        print(a5);
        """.replace("\n", " "))
    # input = InputStream("10 - 2 * 2 / 4")
    # input = StdinStream()
    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    res = MyExprVisitor().visitProg(tree) # Evaluate the expression

# print(input, '=', res)
if __name__ == '__main__':
    main(sys.argv)