grammar CV;

cv: obj EOF;

obj
    : '{' pair (',' pair)* '}'
    ;

pair
    : STRING ':' value
    ;

array
    : '[' value (',' value)* ']'
    ;

value
    : STRING
    | NUMBER
    | obj
    | array
    | 'true'
    | 'false'
    | 'null'
    ;

// Lexer rules
STRING
    : '"' (ESC | ~["\\\r\n])* '"'
    ;

fragment ESC
    : '\\' (["\\/bfnrt] | UNICODE)
    ;

fragment UNICODE
    : 'u' HEX HEX HEX HEX
    ;

fragment HEX
    : [0-9a-fA-F]
    ;

NUMBER
    : '-'? INT ('.' [0-9]+)? EXP?
    ;

fragment INT
    : '0'
    | [1-9] [0-9]*
    ;

fragment EXP
    : [eE] [+\-]? [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;