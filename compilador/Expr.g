grammar Expr;

root : expr EOF ;
expr :  '(' expr ')'                     #unary                    
    | <assoc=right> expr EXP expr        #arithmetic
    | expr (DIV | PROD | MOD) expr       #arithmetic
    | expr (SUM | SUB) expr              #arithmetic
    | expr (TERNARY) expr                #logic
    | expr (LESSEQ | LESS | GREATEREQ | GREATER) expr   #logic
    | expr (NOTEQ | EQ) expr                            #logic        
    | expr (AND) expr                                   #logic
    | expr (OR) expr                                    #logic
    | expr IMPLIES expr                                 #logic
    | NOT expr                                          #logic 
    | NUM                                               #unary 
    ;

stmt:     
    'if'  expr  '{' stmt '}'                          #conditional
    | 'if'  expr  '{' stmt '}' 'else' '{' stmt '}'    #conditional
    |'while' expr '{' stmt '}'                        #loop
    | 'do' '{' stmt '}' 'while' expr                  #loop
    | 'for' '(' NUM ')' '{' stmt '}'                  #loop
    | ID '<-' expr                                    #assignment
    ;

//AMBDOS DO WHILE I EL FOR(K) SON BUCLES QUE HE AFEGIT PER FER EL LLENGUATGE MES COMPLERT :) 




//call: MAJUS (MAJUS | MINUS)*  ;

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




ID: MAJUS (MAJUS | MINUS | NUM)*;
COMMENT: '#' (MAJUS | MINUS)* '\n';
WS : [ \n]+ -> skip ;
NUM : [0-9]+ ;
MAJUS: [A-Z];
MINUS: [a-z];

