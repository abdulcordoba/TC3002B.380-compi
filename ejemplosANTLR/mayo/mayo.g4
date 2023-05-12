grammar mayo;

lenguaje : ( sentencia | declaracion)+;

declaracion :
    VAR ':' TIPO                               #vardecl
    | 'define' VAR ':' TIPO sentencia+ 'end'   #fundecl
    ;

sentencia :
    'do' sentencia 'while' exp                       #do
    | 'if' exp 'then' sentencia ('else' sentencia)?  #if
    | 'return' exp                                   #ret
    | exp                                            #expression
    ;

exp :
    exp '*' exp     #mult
    | exp '+' exp   #suma
    | literal       #lit
    | VAR           #var
    | VAR '<-' exp  #assign
    | '(' exp ')'   #parens
    | VAR '(' ')'   #call
    ;

literal : ENTERO | FLOTANTE
        ;

ENTERO : [0-9]+;
FLOTANTE : [0-9]+ '.' [0-9]+;
TIPO : 'int' | 'float';
VAR : [_a-zA-Z]+;
STRING : '"' [_a-zA-Z0-9]+ '"';
WS : [ \n\t\r]+ -> skip;
