####  DEFINICION DE ANALISIS LEXICO -----------------------------------------------------------------
reserved = {
    'int' : 'INT',
    'evaluar': 'REVALUAR'
}
tokens  = [
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'DECIMAL',
    'ENTERO',
    'PTCOMA',
    'ID',
    'IGUAL'
] + list(reserved.values())

# Tokens
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PTCOMA    = r';'
t_IGUAL     = r'='

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    t.value = t.value.lower()
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
    
# Construyendo el analizador léxico
import ply.ply.lex as lex
from tabla_simbolos.instancia import symbol_table as st
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

#### DEFINICION DE GRAMATICA (ANALISIS SINTACTICO) ----------------------------------------------------------------------------
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''
    if len(t) == 2:
        st.print_table()

def p_instrucciones(t):
    '''instruccion : evaluacion
                   | asignacion
                   | declaracion
    '''

def p_evaluacion(t):
    '''evaluacion : REVALUAR CORIZQ expresion CORDER PTCOMA
    '''
    print(f'la respuesta es: {t[3]}')

def p_asignacion(t):
    '''asignacion : ID IGUAL expresion PTCOMA
    '''
    st.update_variable(t[1], t[3])

def p_declaracion(t):
    '''declaracion : INT ID IGUAL expresion PTCOMA
    '''
    st.add_variable(
        name=t[2],
        data_type=t[1],
        value=t[4],
        line=t.lineno(2),
        column=find_column(t.lexer.lexdata, t.slice[2])
    )

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    ##### Acciones semanticas ----------------------------------------------------------------------------
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL'''
    t[0] = t[1]

def p_expresion_id(t):
    '''expresion    : ID
    '''
    t[0] = st.get_variable(t[1])

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

## APLICACION ----------------------------------------------------------------------------
import ply.ply.yacc as yacc
parser = yacc.yacc()


f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)