grammar Expr;

root : expr EOF ;
expr : <assoc=right> expr EXP expr  #
    | expr () expr
    | expr (SUM | SUB) expr
    | '(' expr ')'
    | NUM
    ;

stmt:

call: [A-Z] ([A-Z]* | [a-z]*)

SUM : '+';
SUB : '-';
PROD: '*';
DIV:  '/';
EXP:  '^';
MOD:  '%';
NOTEQ: '!=';
LESSEQ: '<=';
GREATEREQ: '>=';
LESS: '<';
GREATER: '>';
EQ: '=';

//PITO: ':-'; para el walter del futuro :- sobra tiempo
//AND: '&&';  
//OR: '||';





//COMMENT: 
WS : [ \n]+ -> skip ;
NUM : [0-9]+ ;
MAJUS: [A-Z];

