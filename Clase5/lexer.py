import ply.ply.lex as lex

reserved = {
    'eval':'REVAL',
    'int':'INT'
}

# Lista de nombres de tokens
tokens = [
    'NUMERO',
    'MAS',
    'MENOS',
    'ID',
    'CORDER',
    'CORIZQ',
    'IGUAL',
    'PTC'
]+list(reserved.values())

# Reglas para tokens de un solo carácter
t_MAS   = r'\+'
t_MENOS = r'-'
t_CORDER = r']'
t_CORIZQ = r'\['
t_IGUAL = r'='
t_PTC = r';'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)   #Casteo a int
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    t.value = t.value.lower()
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error léxico: caracter inesperado '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
