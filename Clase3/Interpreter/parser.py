import ply.ply.yacc as yacc
from lexer import tokens
from nodes.ast_nodes import Numero, Suma, Resta

# Precedencia
precedence = (
    ('left', 'MAS', 'MENOS'),
    
)

def p_expresion_numero(p):
    'expresion : NUMERO'
    # Creamos un nodo hoja con el valor entero
    p[0] = Numero(p[1])

def p_expresion_suma(p):
    'expresion : expresion MAS expresion'
    # Creamos un nodo Suma con sus hijos
    p[0] = Suma(p[1], p[3])

def p_expresion_resta(p):
    'expresion : expresion MENOS expresion'
    p[0] = Resta(p[1], p[3])

def p_error(p):
    if p:
        print(f"Error de sintaxis: token inesperado '{p.value}' en línea {p.lineno}")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

# Construimos el parser
parser = yacc.yacc()
