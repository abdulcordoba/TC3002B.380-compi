grammar lenguaje;

raiz : sentencia+;
sentencia : sujeto predicado;
sujeto :
    ARTICULO SUSTANTIVO_COMUN
    | SUSTANTIVO_PROPIO;
predicado : VERBO;

ARTICULO : 'el' | 'la';
SUSTANTIVO_COMUN: 'pato' | 'osa';
SUSTANTIVO_PROPIO: 'Jorge';
VERBO : 'camina' | 'corre';

NUMERO : [0-9]+;
WS : [ \n]+ -> skip;