grammar Expr;

prog: stmts EOF;
//prog: expr EOF;

stmts: stmt+;
stmt: var=ID ASSIGN exp=expr ';' #assignStmt
    | 'print(' var=expr ')' ';' #printStmt
    | 'if' expr 'then' stmts ('elif' expr 'then' stmts)* ('else' stmts)? 'end'   #ifStmt
    | 'while' expr 'do' stmts 'end' #whileStmt
    ;

expr: left=expr op='^' right=expr         #infixExpr
    | left=expr op=('*'|'/') right=expr   #infixExpr
    | left=expr op=('+'|'-') right=expr   #infixExpr
    | left=expr op=('<'|'>'|'<='|'>='|'=='|'!=') right=expr   #comparisonExpr
    | left=expr op=(OP_AND|OP_OR) right=expr  #logicalExpr
    | '!' expr                            #notExpr
    | '(' expr ')'                        #parensExpr
    | atom                                 #atomExpr
    ;

atom
 : INT            #numberAtom
 | BOOL           #booleanAtom
 | ID             #idAtom
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

ASSIGN : '=';

BOOL: 'true' | 'false';

NEWLINE : [\r\n]+ ;
INT : [0-9]+ ;
ID : [a-z][a-z0-9]*;
WS : [ \t\r\n] -> channel(HIDDEN);