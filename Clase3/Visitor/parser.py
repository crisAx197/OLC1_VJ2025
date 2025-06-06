import ply.ply.yacc as yacc
from lexer import tokens
from nodes.ast_nodes import Numero, Suma, Resta

# Precedencia y asociatividad: suma y resta al mismo nivel
precedence = (
    ('left', 'MAS', 'MENOS'),
)

def p_expresion_numero(p):
    'expresion : NUMERO'
    # Crear nodo Numero con el valor entero
    p[0] = Numero(p[1])

def p_expresion_suma(p):
    'expresion : expresion MAS expresion'
    # p[1] y p[3] ya son nodos AST
    p[0] = Suma(p[1], p[3])

def p_expresion_resta(p):
    'expresion : expresion MENOS expresion'
    p[0] = Resta(p[1], p[3])

def p_error(p):
    if p:
        print(f"Error de sintaxis: token inesperado '{p.value}' en línea {p.lineno}")
    else:
        print("Error de sintaxis: fin de archivo inesperado")

# Construcción del parser
parser = yacc.yacc()
