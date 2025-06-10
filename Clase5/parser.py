import ply.ply.yacc as yacc
from lexer import tokens
from nodes.ast_nodes import *

# Precedencia
precedence = (
    ('left', 'MAS', 'MENOS'),   
)

def p_init(p):
    '''init : instrucciones
    '''
    p[0] = Init(p[1])

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                    | instruccion
    '''
    if len(p) == 2:
        p[0] = Instrucciones(p[1])
    else:
        p[0] = Instrucciones(p[2], p[1])

def p_instruccion(p):
    '''instruccion : evaluacion
                  | asignacion
                  | declaracion
    '''
    p[0] = Instruccion(p[1])


def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PTC
    '''
    p[0] = Asignacion(p[1], p[3])

def p_declaracion(p):
    '''declaracion : INT ID IGUAL expresion PTC
    '''
    p[0] = Declaracion(p[1], p[2], p[4])

def p_evaluacion(p):
    '''evaluacion : REVAL CORIZQ expresion CORDER PTC
    '''
    p[0] = Eval(p[3])

def p_expresion_unaria(p):
    '''expresion : NUMERO
                 | ID
    '''
    token = p.slice[1]         
    if token.type == 'ID':
        p[0] = IdExp(p[1])
    else:
        p[0] = Numero(p[1])

def p_expresion_binaria(p):
    '''expresion : expresion MAS expresion
                 | expresion MENOS expresion
    '''
    if p[2] == '+':
        p[0] = Suma(p[1], p[3])
    elif p[2] == '-':
        p[0] = Resta(p[1], p[3])

def p_error(p):
    if p:
        print(f"Error de sintaxis: token inesperado '{p.value}' en línea {p.lineno}")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

parser = yacc.yacc()
