grammar Expr;

root : declaration* expr* EOF ;

expr :  '(' expr ')'                     #unary
    | '-' expr                             #unary
    | ID                                 #variable
    | 'true'                             #values
    | 'false'                            #values 
    |  NUM                               #unary
    | <assoc=right> expr EXP expr        #arithmetic
    | expr (DIV | PROD | MOD) expr       #arithmetic
    | expr (SUM | SUB) expr              #arithmetic
    | expr (LESSEQ | LESS | GREATEREQ | GREATER) expr   #logic
    | expr (NOTEQ | EQ) expr                            #logic
    | NOT expr                                          #logic         
    | expr (AND | OR | IMPLIES) expr                    #logic                                                                                
    | FUNCTIONID (FUNCTIONID | expr)*                   #call                                      
    ;                 

declaration: FUNCTIONID (ID | FUNCTIONID)* block;
block: '{' stmt+ '}';

stmt:  
    expr                                            #expression
    |ID '<-' expr                                    #assignment
    |'if'  expr  block                              #conditional
    | 'if'  expr  block 'else' block                #conditional
    | 'if'  expr  block 'else if' expr block        #conditional
    | 'if'  expr  block 'else if' expr block  'else' block  #conditional
    |'while' expr block                        #loop
    | 'do' block 'while' expr                  #loop
    | 'for' '(' ID '<-' expr 'to'  expr ')' block  #loop 
    | 'for' '(' ID '<-' expr 'downto'  expr ')' block #loop
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
COMMENT: '#' (MAJUS | MINUS | NUM | [ \t])* WS* -> skip;
WS : [ \n\r]+ -> skip ;
NUM : [0-9]+ ;

