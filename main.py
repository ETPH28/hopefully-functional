import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor


def main(argv):

    test = """
        a2 = 3 / 2;
        a2 = a2+1;
        a4 = true;
        if (false) then
            print(a2);
            print(!true);
        elif false && true then
            print(6);
        else 
            print(3-1);
        end
        """
    fibonacci = """
        n1 = 9;
        a1 = 0;
        a2 = 1;
        while n1>0 do
            t1 = a2;
            a2 = a1 + a2;
            a1 = t1;
            n1 = n1 - 1;
        end
        print(a1);
        """

    math_operations_test = """
        sum = 0;
        n = 10;
        i = 1;
        while i <= n do
            sum = sum + i;
            i = i + 1;
        end
        print(sum);

        num1 = 5;
        num2 = 2;
        res = num1 * num2 / 3;
        print(res);

        base = 2;
        exponent = 4;
        result = 1;
        i = 1;
        while i <= exponent do
            result = result * base;
            i = i + 1;
        end
        print(result);
        print(base^exponent);
        """

    invalid = """
    a = 5;
    b = 3;
    c = "test";
    if a > b
        print(a)
    """

    input = InputStream(test.replace("\n", " "))
    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    res = MyExprVisitor().visitProg(tree) # Evaluate the expression

# print(input, '=', res)
if __name__ == '__main__':
    main(sys.argv)