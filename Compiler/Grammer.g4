grammar Grammer;

// Lexer rules
STRINGLIST : '"' (ESC | ~["\\\r\n])* '"' ;
ESC : '\\' . ;
INTEGER : '0' | [1-9] [0-9]*;
DOUBLE : INTEGER '.' [0-9]+ ([eE] [+\-]? [0-9]+)?;
ID :  [a-zA-Z_] [a-zA-Z_0-9]*;
 
prog : func_list ;

func_list : func_def func_list
          | func_def
          ;

func_def :data_type ID '(' param_list? ')' code_block
          ;

param_list : param ',' param_list
           |param
           | /* empty */
           ;

param : data_type ID ;

data_type : 'int' | 'double' | 'boolean' | 'void' ;

code_block : '{' stmt_list '}' ;

stmt_list : stmt stmt_list
          |  /* empty */
          ;

stmt : ';'
     | code_block
     | data_type var_list ';'
     | ID '=' expr ';'
     | ID '++' ';'
     | ID '--' ';'
     | 'return' ';'
     | 'return' expr ';'
     | loop_stmt
     | decide '(' expr ')' stmt ('else' stmt)?
     | expr ';'

     ;
decide : 'if' ;

loop_stmt : 'while' '(' expr ')' stmt
          ;
init_stmt : data_type ID '=' expr
          | ID '=' expr
          | /* empty */
          ;

post_stmt : ID '=' expr
          | ID '++'
          | ID '--'
          | /* empty */
          ;

var_list :var (',' var)*
         ;

var : ID
     |ID '=' expr
    ;
expr : number
     | ID
     | 'true'
     | 'false'
     | STRINGLIST
     | ID '(' args ')'
     | '(' expr ')'
     |unop expr
     |expr ( '*' | '/' | '%' ) expr
     |expr  ( '+' | '-' ) expr
     |expr ( '<' | '>' | '<=' | '>=' ) expr
     |expr ( '==' | '!=' ) expr
     |expr and expr
     |expr or expr
     ;
and : '&&' ;
or : '||';

args : expr ( ',' expr )*
     | /* empty */
     ;
unop : '-' | '!' ;
number : INTEGER | DOUBLE;



Whitespace: [ \t\r\n]+ -> skip ;
Newline: '\r'? '\n' -> skip ;
COMMENT : '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip;
