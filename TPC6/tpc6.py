import re
import ply.lex as lex


tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'GREATER',
   'LESSER',
   'EQUALS',
   'L_BRACKET',
   'R_BRACKET',
   'L_S_BRACKET',
   'R_S_BRACKET',
   'FUNCTION',
   'PROGRAM',
   'COMMENT',
   'LINE_END',
   'CAST',
   'LOOP',
   'LONG_COMMENT',
   'VAR',
   'PERIOD',
   'COMMA',
   'LIST_S',
   'LIST'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATER = r'>'
t_LESSER = r'<'
t_EQUALS = r'='
t_L_BRACKET = r'\{'
t_R_BRACKET = r'\}'
t_L_S_BRACKET = r'\['
t_R_S_BRACKET = r'\]'
t_FUNCTION = r'function'
t_PROGRAM = r'program'
t_COMMENT = r'//.*'
t_LINE_END = r'\;'
t_LONG_COMMENT = r'/\*[\s\S]*?\*/'
t_VAR = r'\w+(?=\[)*'
t_PERIOD = r'\.'
t_COMMA = r','
t_LIST_S = r'\[.*(,.*)*\]'
t_LIST = r'\{.*(,.*)*\}'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CAST(t):
    r'int|float|string|long|char|bool|double'
    return t

def t_LOOP(t):
    r'while|for'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

ex1 = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''

ex2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''




lexer = lex.lex()

lexer.input(ex2)

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)