grammar Parallelize;

//Start rule
program: .*? (for_loop .*? {print("Found a for loop!")})*? EOF;

for_loop: FOR '('for_loop_header')' '{' (statement';')* '}';

for_loop_header: .*? ';' .*? ';' statement;

statement
    : TYPE? IDENT
    | TYPE? IDENT '=' (literal |IDENT) (OP (literal | IDENT))*
    | IDENT op_assign (literal | IDENT)
    | IDENT INC_DEC;

literal: STRING_LITERAL | FLOAT_LITERAL | DOUBLE_LITERAL | INTEGER;

op_assign: ASSIGNMENT OP;

FOR : 'for';
TYPE: 'int' | 'double' | 'string' | 'float' | 'char';
COMPARE: '<' | '>' | '<=' | '>=' | '==' | '!=';
ASSIGNMENT: '=';
INC_DEC: '++' | '--';
OP: '+' | '-' | '*' | '/' | '%';

STRING_LITERAL: '"'.*?'"';
CHAR: '\''.'\'';
INTEGER: [0-9]+ ;
FLOAT_LITERAL: ([0-9]*[.])?[0-9]+'f' ;
DOUBLE_LITERAL: ([0-9]*[.])?[0-9]+ ;

IDENT: [a-zA-Z][a-zA-Z0-9]*;
WS : [ \t\n\r]+ -> skip;