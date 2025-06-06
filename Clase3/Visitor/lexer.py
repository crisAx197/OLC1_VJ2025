import ply.ply.lex as lex

# Definición de tokens
tokens = (
    'NUMERO',
    'MAS',
    'MENOS',
)

# Reglas simples para tokens con un solo carácter
t_MAS   = r'\+'
t_MENOS = r'-'

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)  # convertimos el lexema a int
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error léxico: caracter inesperado '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
