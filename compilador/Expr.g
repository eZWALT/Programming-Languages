grammar Expr;

//OJO, CUANDO FUNCIONEN BIEN LAS FUNCIONES ESTO TENDRA QUE SER ROOT: DECLARATION* STMT? EOF
root : stmt* EOF ;
expr :  '(' expr ')'                     #unary
    | ID                                 #variable
    | <assoc=right> expr EXP expr        #arithmetic
    | expr (DIV | PROD | MOD) expr       #arithmetic
    | expr (SUM | SUB) expr              #arithmetic
    | expr (LESSEQ | LESS | GREATEREQ | GREATER) expr   #logic
    | expr (NOTEQ | EQ) expr                            #logic
    | NOT expr                                          #logic         
    | expr (AND | OR | IMPLIES) expr                    #logic
    | NUM                                               #unary 
    | ID expr*                                          #call
    ;

declaration: FUNCTIONID ID block;
block: '{' stmt+ '}';

stmt:     
     ID '<-' expr                                    #assignment
    |'if'  expr  block                              #conditional
    | 'if'  expr  block 'else' block                #conditional
    | 'if'  expr  block 'else if' expr block        #conditional
    | 'if'  expr  block 'else if' expr block  'else' block  #conditional
    |'while' expr block                        #loop
    | 'do' block 'while' expr                  #loop
    ;


IMPLIES: '-->' | ':-';
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
AND: '&&';  
OR: '||';
NOT: '!';


ID: MINUS (MAJUS | MINUS | NUM)*;
FUNCTIONID: MAJUS (MAJUS | MINUS | NUM)*;
MAJUS: [A-Z];
MINUS: [a-z];
COMMENT: '#' (MAJUS | MINUS)* '\n';
WS : [ \n]+ -> skip ;
NUM : [0-9]+ ;

