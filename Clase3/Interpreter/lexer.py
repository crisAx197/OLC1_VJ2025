import ply.ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'NUMERO',
    'MAS',
    'MENOS',
)

# Reglas para tokens de un solo carácter
t_MAS   = r'\+'
t_MENOS = r'-'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)   #Casteo a int
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error léxico: caracter inesperado '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
