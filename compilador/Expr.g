grammar Expr;

root : expr EOF ;
expr :  '(' expr ')'                        #parentheses
    | <assoc=right> expr EXP expr           #binary
    | expr (DIV | PROD | MOD) expr          #binary
    | expr (SUM | SUB) expr                 #binary
    | expr (TERNARY) expr                   #binary
    | expr (LESSEQ | LESS | GREATEREQ | GREATER) expr    #binary
    | expr (NOTEQ | EQ) expr
    | expr (AND) expr 
    | expr (OR) expr
    | NUM
    ;

stmt: 
    assignment
    | loop
    | conditional
    ;

loop: 
    'while' expr '{' stmt '}'
    | 'do' '{' stmt '}' 'while' expr 
    | 'for' '(' NUM ')' '{' stmt '}'                   
    ;

conditional:
    'if' '(' expr ')' '{' stmt '}'
    | 'if' '(' expr ')' '{' stmt '}' 'else' '{' stmt '}'
    ;
 
//AMBDOS DO WHILE I EL FOR(K) SON BUCLES QUE HE AFEGIT PER FER EL LLENGUATGE MES COMPLERT :) 




//call: MAJUS (MAJUS | MINUS)*  ;

SUM : '+';
SUB : '-';
PROD: '*';
DIV:  '/';
EXP:  '^';
MOD:  '%';
TERNARY: '<=>';
NOTEQ: '!=';
LESSEQ: '<=';
GREATEREQ: '>=';
LESS: '<';
GREATER: '>';
EQ: '=';
AND: '&&';  
OR: '||';

//PITO: ':-'; para el walter del futuro :- sobra tiempo





COMMENT: '#' (MAJUS | MINUS)* '\n';
WS : [ \n]+ -> skip ;
NUM : [0-9]+ ;
MAJUS: [A-Z];
MINUS: [a-z];


