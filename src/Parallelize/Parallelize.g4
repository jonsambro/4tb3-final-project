grammar Parallelize;

//Start rule
program: ('#'|.)*? (for_loop .*?)* EOF;

for_loop: FOR '('for_loop_header')' '{' (statement';')* '}';

for_loop_header: assignment ';' .*? ';' statement;

statement
    : declaration
    | assignment
    | self_assignment;

declaration: TYPE variable;

assignment: (declaration | lhs=variable) ASSIGNMENT rhs;

self_assignment
    : variable OP ASSIGNMENT rhs
    | variable INC_DEC;

rhs: (literal |variable) (OP (literal | variable))*;

literal: STRING_LITERAL | FLOAT_LITERAL | DOUBLE_LITERAL | INTEGER;

variable
    : (IDENT'['rhs']')
    | simple=IDENT;

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