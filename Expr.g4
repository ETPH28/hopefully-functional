grammar Expr;

prog: stmts EOF;
//prog: expr EOF;

stmts: stmt+;
stmt: var=ID '=' exp=expr ';' #assignStmt
    | 'print(' var=ID ')' ';' #printStmt
    ;

expr: left=expr op='^' right=expr         #infixExpr
    | left=expr op=('*'|'/') right=expr   #infixExpr
    | left=expr op=('+'|'-') right=expr   #infixExpr
    | left=expr op=('<'|'>'|'<='|'>='|'=='|'!=') right=expr   #comparisonExpr
    | left=expr op=('&&'|'||') right=expr  #logicalExpr
    | '!' expr                            #notExpr
    | BOOL                                #boolExpr
    | INT                                 #numberExpr
    | '(' expr ')'                        #parensExpr
    ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_PWR: '^';
OP_LT: '<';
OP_LE: '<=';
OP_GT: '>';
OP_GE: '>=';
OP_EQ: '==';
OP_NE: '!=';
OP_AND: '&&';
OP_OR: '||';

BOOL: 'true' | 'false';

NEWLINE : [\r\n]+ ;
INT : [0-9]+ ;
ID : [a-z][a-z0-9]*;
WS : [ \t\r\n] -> channel(HIDDEN);